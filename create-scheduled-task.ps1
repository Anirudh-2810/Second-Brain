<#
.SYNOPSIS
Creates a Task Scheduler task for obsidian-auto-commit.ps1 (compatible with PowerShell 5.1)
#>

$TaskName = "Second-Brain Auto-Commit"
$ScriptPath = "C:\Users\Vijaykumar\Second-Brain\Second-Brain\obsidian-auto-commit.ps1"
$PowerShellPath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$Arguments = "-ExecutionPolicy Bypass -File `"$ScriptPath`""

# Remove existing task
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Removed existing task: $TaskName"
}

# Create trigger using COM (supports delay)
$service = New-Object -ComObject Schedule.Service
$service.Connect()
$rootFolder = $service.GetFolder("\")
$taskDef = $service.NewTask(0)

# Trigger: At startup with 1-minute delay
$trigger = $taskDef.Triggers.Create(8)  # 8 = TASK_TRIGGER_BOOT
$trigger.Id = "AtStartupWithDelay"
$trigger.StartBoundary = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ss")
$trigger.Delay = "PT1M"  # 1 minute delay
$trigger.Enabled = $true

# Action: Run PowerShell
$action = $taskDef.Actions.Create(0)  # 0 = TASK_ACTION_EXEC
$action.Path = $PowerShellPath
$action.Arguments = $Arguments

# Settings
$taskDef.Settings.AllowDemandStart = $true
$taskDef.Settings.StartWhenAvailable = $true
$taskDef.Settings.RunOnlyIfNetworkAvailable = $true
$taskDef.Settings.Hidden = $true
$taskDef.Settings.DisallowStartIfOnBatteries = $false
$taskDef.Settings.StopIfGoingOnBatteries = $false

# Principal: Run as current user with highest privileges
$taskDef.Principal.LogonType = 3  # 3 = TASK_LOGON_INTERACTIVE_TOKEN
$taskDef.Principal.RunLevel = 1   # 1 = TASK_RUNLEVEL_HIGHEST
$taskDef.Principal.UserId = $env:USERNAME

# Register
$rootFolder.RegisterTaskDefinition($TaskName, $taskDef, 6, $null, $null, 3, $null)

Write-Host "Task created: $TaskName"
Write-Host "Run: Get-ScheduledTask -TaskName '$TaskName'"
Write-Host "Test run: Start-ScheduledTask -TaskName '$TaskName'"