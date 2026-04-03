@echo off
setlocal enabledelayedexpansion

:: ============================================
:: MEWEN Installer для Windows
:: ============================================

echo.
echo ========================================
echo   MEWEN - ИИ-ассистент
echo   Установка...
echo ========================================
echo.

:: Проверка Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ОШИБКА] Python не найден!
    echo Установите Python 3.8+ с https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python найден
echo.

:: Определение пути установки
set "MEWEN_PATH=%USERPROFILE%\.mewen"

echo Установка в: %MEWEN_PATH%
echo.

:: Создание директории
if not exist "%MEWEN_PATH%" (
    mkdir "%MEWEN_PATH%"
    echo [OK] Создана директория %MEWEN_PATH%
)

:: Копирование файлов
echo Копирование файлов...
xcopy /E /I /Y "%~dp0*" "%MEWEN_PATH%" >nul
echo [OK] Файлы скопированы
echo.

:: Установка зависимостей
echo Установка зависимостей...
pip install -r "%MEWEN_PATH%\requirements.txt"
if %errorlevel% neq 0 (
    echo [ОШИБКА] Не удалось установить зависимости
    pause
    exit /b 1
)
echo [OK] Зависимости установлены
echo.

:: Создание ярлыка команды
echo Создание команды "Mewen"...

:: Добавление в PATH
set "PATH=%MEWEN_PATH%;%PATH%"

:: Создание батника для запуска
echo @echo off > "%MEWEN_PATH%\Mewen.bat"
echo python "%MEWEN_PATH%\mewen.py" %%* >> "%MEWEN_PATH%\Mewen.bat"

:: Добавление в системный PATH (для постоянного доступа)
echo Добавление в PATH...
reg add "HKCU\Environment" /v PATH /t REG_EXPAND_SZ /d "%PATH%" /f >nul 2>&1

echo [OK] Команда "Mewen" создана
echo.

:: Готово
echo ========================================
echo   Установка завершена!
echo ========================================
echo.
echo Теперь вы можете запустить Mewen командой:
echo   Mewen
echo.
echo Или закройте это окно и откройте новое,
echo затем введите: Mewen
echo.
pause
