@echo off

echo Активация виртуального окружения...
call .venv10\Scripts\activate
if errorlevel 1 (
    echo Ошибка при активации виртуального окружения.
    echo Нажмите любую клавишу, чтобы закрыть окно...
    pause
    exit /b 1
)

echo Запуск main.py...
python main.py
if errorlevel 1 (
    echo Ошибка при выполнении main.py.
    echo Нажмите любую клавишу, чтобы закрыть окно...
    pause
    exit /b 1
)

echo Завершение работы виртуального окружения...
deactivate

echo Нажмите любую клавишу, чтобы закрыть окно...
pause
