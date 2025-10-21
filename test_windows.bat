@echo off
echo ================================================
echo   ТЕСТ КАЛЬКУЛЯТОРА 2025 (Windows)
echo ================================================
echo.

REM Проверка Python
echo [1/3] Проверка установки Python...
python --version
if errorlevel 1 (
    echo ОШИБКА: Python не найден!
    echo Установите Python с https://www.python.org/downloads/
    pause
    exit /b 1
)
echo OK!
echo.

REM Запуск примеров
echo [2/3] Запуск примеров использования...
echo.
python examples.py
if errorlevel 1 (
    echo ОШИБКА при запуске примеров!
    pause
    exit /b 1
)
echo.

REM Интерактивный тест
echo [3/3] Быстрый интерактивный тест...
echo.
echo Введите несколько команд для теста:
echo   2 + 2
echo   sqrt(144)
echo   sin(pi/2)
echo   quit
echo.
python calculator2025.py

echo.
echo ================================================
echo   ТЕСТ ЗАВЕРШЕН
echo ================================================
pause
