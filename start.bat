@echo off

echo ��������� ������������ ���������...
call .venv10\Scripts\activate
if errorlevel 1 (
    echo ������ ��� ��������� ������������ ���������.
    echo ������� ����� �������, ����� ������� ����...
    pause
    exit /b 1
)

echo ������ main.py...
python main.py
if errorlevel 1 (
    echo ������ ��� ���������� main.py.
    echo ������� ����� �������, ����� ������� ����...
    pause
    exit /b 1
)

echo ���������� ������ ������������ ���������...
deactivate

echo ������� ����� �������, ����� ������� ����...
pause
