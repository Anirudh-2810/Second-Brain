<#
.SYNOPSIS
File watcher that auto-commits on changes (debounced)

.DESCRIPTION
Watches the vault for file changes, debounces by 30 seconds, then auto-commits.
Run in a terminal and keep open, or run via Task Scheduler at login.
#>

param(
    [string]$RepoPath = "C:\Users\Vijaykumar\Second-Brain\Second-Brain",
    [int]$DebounceSeconds = 30
)

Set-Location $RepoPath

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $RepoPath
$watcher.IncludeSubdirectories = $true
$watcher.Filter = "*.*"
$watcher.NotifyFilter = [IO.NotifyFilters]::LastWrite -bor [IO.NotifyFilters]::FileName -bor [IO.NotifyFilters]::DirectoryName

$timer = $null
$pending = $false

$action = {
    if ($timer) { $timer.Dispose() }
    $timer = New-Object System.Timers.Timer($DebounceSeconds * 1000)
    $timer.AutoReset = $false
    $timer.Elapsed += {
        $timer.Dispose()
        $pending = $false
        # Run commit
        & "$RepoPath\auto-commit.ps1" -Force
    }
    $timer.Start()
    $pending = $true
}

Register-ObjectEvent -InputObject $watcher -EventName Changed -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName Created -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName Deleted -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName Renamed -Action $action | Out-Null

$watcher.EnableRaisingEvents = $true

Write-Host "Watching $RepoPath for changes (debounce: ${DebounceSeconds}s)..."
Write-Host "Press Ctrl+C to stop"

try {
    while ($true) { Start-Sleep 10 }
}
finally {
    $watcher.EnableRaisingEvents = $false
    $watcher.Dispose()
    if ($timer) { $timer.Dispose() }
    Get-EventSubscriber | Unregister-Event -Force
    Write-Host "Stopped watching"
}