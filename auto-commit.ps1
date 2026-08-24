<# 
.SYNOPSIS
Auto-commit and push changes to Second-Brain repo

.DESCRIPTION
Checks for uncommitted changes, commits with timestamp, pushes to origin/main.
Run manually, via Task Scheduler, or as a file watcher.
#>

param(
    [string]$RepoPath = "C:\Users\Vijaykumar\Second-Brain\Second-Brain",
    [string]$CommitPrefix = "auto",
    [switch]$Force
)

Set-Location $RepoPath

# Check for changes
$status = git status --porcelain
if (-not $status -and -not $Force) {
    Write-Host "No changes to commit"
    exit 0
}

# Stage all changes
git add -A

# Generate commit message
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$filesChanged = (git diff --cached --name-only).Count
$commitMsg = $CommitPrefix + ": " + $timestamp + " - " + $filesChanged + " file(s) updated"

# Commit
git commit -m $commitMsg

# Push
git push origin HEAD:main

Write-Host ("Committed and pushed: " + $commitMsg)