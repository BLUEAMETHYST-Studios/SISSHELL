@echo off

cd %localappdata%/SISSHELL

del *

cd ..

rmdir SISSHELL

echo SISSHELL was removed from your device, if you want to remove its Environment Variable, you'll need to do that manually due to limitations!

pause