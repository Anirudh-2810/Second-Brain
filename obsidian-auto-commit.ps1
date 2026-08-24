<#
.SYNOPSIS
Auto-commit watcher that runs only while Obsidian is open

.DESCRIPTION
Monitors Obsidian process. Starts file watcher when Obsidian opens, stops when Obsidian closes.
Run this script at Windows startup (Task Scheduler or Startup folder).
#>

param(
    [string]$RepoPath = "C:\Users\Vijaykumar\Second-Brain\Second-Brain",
    [int]$DebounceSeconds = 30,
    [int]$PollIntervalSeconds = 5
)

Set-Location $RepoPath

$watcher = $null
$timer = $null
$watchJob = $null

function Start-Watcher {
    global $watcher, $timer, $watchJob
    
    if ($watcher) { return }  # Already running
    
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Obsidian detected — starting file watcher..."
    
    $watcher = New-Object System.IO.FileSystemWatcher
    $watcher.Path = $RepoPath
    $watcher.IncludeSubdirectories = $true
    $watcher.Filter = "*.*"
    $watcher.NotifyFilter = [IO.NotifyFilters]::LastWrite -bor [IO.NotifyFilters]::FileName -bor [IO.NotifyFilters]::DirectoryName

    $action = {
        if ($timer) { $timer.Dispose() }
        $timer = New-Object System.Timers.Timer($DebounceSeconds * 1000)
        $timer.AutoReset = $false
        $timer.Elapsed += {
            $timer.Dispose()
            # Run commit in background
            Start-Job -ScriptBlock {
                param($RepoPath)
                Set-Location $RepoPath
                $status = git status --porcelain
                if ($status) {
                    git add -A
                    $ts = Get-Date -Format "yyyy-MM-dd HH:mm"
                    $fc = (git diff --cached --name-only).Count
                    $msg = "auto: $ts - $fc file(s) updated"
                    git commit -m $msg
                    git push origin HEAD:main
                    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Committed: $msg"
                }
            } -ArgumentList $RepoPath | Out-Null
        }
        $timer.Start()
    }

    Register-ObjectEvent -InputObject $watcher -EventName Changed -Action $action | Out-Null
    Register-ObjectEvent -InputObject $watcher -EventName Created -Action $action | Out-Null
    Register-ObjectEvent -InputObject $watcher -EventName Deleted -Action $action | Out-Null
    Register-ObjectEvent -InputObject $watcher -EventName Renamed -Action $action | Out-Null

    $watcher.EnableRaisingEvents = $true
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] File watcher active (debounce: ${DebounceSeconds}s)"
}

function Stop-Watcher {
    global $watcher, $timer, $watchJob
    
    if (-not $watcher) { return }  # Not running
    
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Obsidian closed — stopping file watcher..."
    
    $watcher.EnableRaisingEvents = $false
    Get-EventSubscriber | Where-Object { $_.SourceObject -eq $watcher } | Unregister-Event -Force
    $watcher.Dispose()
    if ($timer) { $timer.Dispose() }
    $watcher = $null
    $timer = $null
    
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] File watcher stopped"
}

function Test-ObsidianRunning {
    $proc = Get-Process -Name "Obsidian" -ErrorAction SilentlyContinue
    return $proc -ne $null
}

# Main loop
$wasRunning = $false
Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Obsidian auto-commit monitor started"
Write-Host "Watching for Obsidian process... (Ctrl+C to stop)"

try {
    while ($true) {
        $isRunning = Test-ObsidianRunning
        
        if ($isRunning -and -not $wasRunning) {
            Start-Watcher
        } elseif (-not $isRunning -and $wasRunning) {
            Stop-Watcher
        }
        
        $wasRunning = $isRunning
        Start-Sleep -Seconds $PollIntervalSeconds
    }
}
finally {
    Stop-Watcher
    Get-Job | Remove-Job -Force
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Monitor stopped"
}