@echo off
title Lanzador de Marketing AI Suite
cls

echo ===================================================
echo   🚀 INICIANDO MARKETING AI SUITE...
echo ===================================================
echo.

echo [1/2] Verificando e instalando dependencias...
echo ---------------------------------------------------
python -m pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo.
    echo ❌ ERROR: Hubo un problema instalando las librerias.
    echo Asegurate de tener instalado Python y el archivo requirements.txt.
    pause
    exit /b
)
echo ✅ Dependencias listas.
echo.

echo [2/2] Lanzando aplicacion en el navegador...
echo ---------------------------------------------------
echo (Esta ventana debe permanecer abierta mientras uses la App)
echo.

:: Lanzamos streamlit
python -m streamlit run app.py

pause