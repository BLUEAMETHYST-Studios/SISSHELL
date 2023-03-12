# EXECUTE THIS WITH POWERSHELL!

mkdir ~\AppData\Local\SISSHELL
Set-Location ~\AppData\Local\SISSHELL

Write-Host Downloading ...

$ProgressPreference = "SilentlyContinue"
Invoke-WebRequest -Uri "https://github.com/BLUEAMETHYST-Studios/SISSHELL/raw/B1.0/sis.exe" -OutFile "~\AppData\Local\SISSHELL\sis.exe"

Clear-Host

Set-Location ~\AppData\Local\SISSHELL

Write-Host Finishing ...

$FinalPath = [Environment]::GetEnvironmentVariable("PATH", "User") + ";" + $Pwd
[Environment]::SetEnvironmentVariable( "Path", $FinalPath, "User" )

Set-Location $InitPwd
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User") 


Clear-Host

Write-Host Installation completed!
Write-Host You may close this window now!

pause
