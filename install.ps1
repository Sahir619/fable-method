param(
    [ValidateSet("claude", "codex")]
    [string]$Target = "claude",
    [string]$Destination
)

# Standalone skill installer for Windows PowerShell.
# Usage: .\install.ps1 [-Target claude|codex] [-Destination PATH]
$ErrorActionPreference = "Stop"
$src = $PSScriptRoot

if ($Destination) {
    $dst = $Destination
    $product = if ($Target -eq "codex") { "Codex" } else { "Claude Code" }
} elseif ($Target -eq "codex") {
    $codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
    $dst = Join-Path $codexHome "skills"
    $product = "Codex"
} else {
    $dst = Join-Path $HOME ".claude\skills"
    $product = "Claude Code"
}

New-Item -ItemType Directory -Force -Path $dst | Out-Null
$skills = @("fable-method", "fable-loop", "fable-judge", "fable-domain")
foreach ($skill in $skills) {
    Copy-Item (Join-Path $src "skills\$skill") $dst -Recurse -Force
}

Write-Host "Installed: $($skills -join ' ') -> $dst"
Write-Host "The skills will be available to $product in a new turn."
