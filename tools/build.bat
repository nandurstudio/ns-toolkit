@echo off
title NS Toolkit - Smart Build System
color 0A

echo.
echo ========================================================
echo    NS Toolkit - Smart Build System
echo    "Develop Once, Distribute Everywhere!"
echo ========================================================
echo.

echo [INFO] Running smart build for all platforms...
cd /d "%~dp0"
python smart_build.py --platform all

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo    [SUCCESS] All packages built successfully!
    echo ========================================================
    echo.
    echo Ready for distribution:
    echo - Blender Extensions: releases/blender_extensions/*.zip
    echo - Gumroad Commercial: releases/gumroad_commercial/*.zip
    echo.
    echo Next steps:
    echo 1. Submit Blender package to: extensions.blender.org
    echo 2. Upload Gumroad package to marketplace
    echo.
) else (
    echo.
    echo ========================================================
    echo    [FAILED] Build process failed!
    echo ========================================================
    echo.
)

pause