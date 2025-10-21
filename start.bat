@echo off
echo 🤖 HubSpot AI Automation Agent
echo ========================================
echo.

:: Check if config exists
if not exist "config\api_config.json" (
    echo ❌ Configuration file not found!
    echo 💡 Please create config\api_config.json with your API keys
    echo 💡 Run: python setup.py for help
    pause
    exit
)

:: Run the application
python main.py
pause