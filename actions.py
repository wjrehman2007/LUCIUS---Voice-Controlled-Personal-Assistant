"""
Actions Module
Implements the actual execution logic for all commands.
Handles system control, web automation, text input, etc.
"""

import os
import sys
import subprocess
import webbrowser
import pyautogui
import logging
from datetime import datetime
import time
import threading
from logger_config import setup_logger

logger = setup_logger("ActionExecutor")

# Add small delay between key presses for reliable text input
pyautogui.PAUSE = 0.05


class ActionExecutor:
    """
    Executes all system commands and actions.
    Clean separation between command parsing and execution.
    """

    def __init__(self):
        """Initialize action executor."""
        logger.info("Initializing Action Executor...")
        self.action_map = {
            "system_shutdown": self.shutdown_pc,
            "system_restart": self.restart_pc,
            "get_time": self.get_time,
            "web_search": self.web_search,
            "open_application": self.open_application,
            "write_text": self.write_text,
            "get_weather": self.get_weather,
            "show_help": self.show_help,
        }
        logger.info("✓ Action Executor initialized")

    def execute(self, action, parameters):
        """
        Execute an action with parameters.
        
        Args:
            action (str): Action to execute
            parameters (dict): Parameters for the action
            
        Returns:
            str: Response message
        """
        if action not in self.action_map:
            logger.warning(f"Unknown action: {action}")
            return "I don't know how to do that."

        try:
            handler = self.action_map[action]
            response = handler(parameters)
            logger.info(f"✓ Action {action} completed")
            return response
        except Exception as e:
            logger.error(f"Error executing action {action}: {str(e)}")
            return f"Error: {str(e)}"

    # =====================================================================
    # SYSTEM CONTROL ACTIONS
    # =====================================================================

    def shutdown_pc(self, params):
        """
        Shutdown the PC.
        
        Args:
            params (dict): Action parameters
            
        Returns:
            str: Response message
        """
        logger.warning("Shutdown command initiated")
        response = "Shutting down your PC. Goodbye!"

        # Schedule shutdown after speaking response (gives TTS time to finish)
        def schedule_shutdown():
            time.sleep(2)
            try:
                os.system("shutdown /s /t 10 /c 'Shutdown initiated by LUCIUS'")
                logger.info("Shutdown command sent to OS")
            except Exception as e:
                logger.error(f"Failed to shutdown: {str(e)}")

        shutdown_thread = threading.Thread(target=schedule_shutdown, daemon=True)
        shutdown_thread.start()

        return response

    def restart_pc(self, params):
        """
        Restart the PC.
        
        Args:
            params (dict): Action parameters
            
        Returns:
            str: Response message
        """
        logger.warning("Restart command initiated")
        response = "Restarting your PC."

        def schedule_restart():
            time.sleep(2)
            try:
                os.system("shutdown /r /t 10 /c 'Restart initiated by LUCIUS'")
                logger.info("Restart command sent to OS")
            except Exception as e:
                logger.error(f"Failed to restart: {str(e)}")

        restart_thread = threading.Thread(target=schedule_restart, daemon=True)
        restart_thread.start()

        return response

    # =====================================================================
    # INFORMATION ACTIONS
    # =====================================================================

    def get_time(self, params):
        """
        Get current time in Pakistan timezone.
        
        Args:
            params (dict): Action parameters
            
        Returns:
            str: Current time response
        """
        try:
            # Get current time in Pakistan (PKT is UTC+5)
            now = datetime.now()
            time_str = now.strftime("%I:%M %p")
            date_str = now.strftime("%A, %B %d, %Y")

            response = f"The current time is {time_str}. Today is {date_str}."
            logger.info(f"Time requested: {response}")
            return response

        except Exception as e:
            logger.error(f"Error getting time: {str(e)}")
            return "Sorry, I couldn't get the current time."

    def get_weather(self, params):
        """
        Get weather information.
        Note: Requires internet connection. Currently returns placeholder.
        
        Args:
            params (dict): Action parameters
            
        Returns:
            str: Weather information
        """
        logger.info("Weather information requested")
        # In production, you would call a weather API here
        # For now, return a helpful message
        response = "To get weather information, please check a weather website or open a browser."
        return response

    def show_help(self, params):
        """
        Show available commands.
        
        Args:
            params (dict): Action parameters
            
        Returns:
            str: Help message
        """
        help_text = (
            "I can help you with: "
            "opening applications like Chrome and Notepad, "
            "searching the web, "
            "typing text, "
            "telling you the time, "
            "and shutting down or restarting your computer. "
            "Try saying 'search for something' or 'open chrome'."
        )
        logger.info("Help requested")
        return help_text

    # =====================================================================
    # BROWSER AND SEARCH ACTIONS
    # =====================================================================

    def web_search(self, params):
        """
        Open Chrome and search Google for a query.
        
        Args:
            params (dict): Action parameters containing 'query'
            
        Returns:
            str: Response message
        """
        query = params.get("query", "").strip()

        if not query:
            return "Please provide a search query."

        logger.info(f"Searching for: {query}")

        try:
            # Build Google search URL
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

            # Open in default browser (usually Chrome)
            response = f"Searching for {query}. Opening Chrome."
            logger.info(f"Opening search URL: {search_url}")
            webbrowser.open(search_url)
            return response

        except Exception as e:
            logger.error(f"Error during web search: {str(e)}")
            return f"Sorry, I couldn't perform the search: {str(e)}"

    # =====================================================================
    # APPLICATION CONTROL ACTIONS
    # =====================================================================

    def open_application(self, params):
        """
        Open a specified application.
        
        Args:
            params (dict): Action parameters containing 'app'
            
        Returns:
            str: Response message
        """
        app = params.get("app", "").lower().strip()

        logger.info(f"Opening application: {app}")

        try:
            if app in ["chrome", "google"]:
                self._open_chrome()
                return "Opening Google Chrome."

            elif app in ["edge", "microsoft edge"]:
                self._open_edge()
                return "Opening Microsoft Edge."

            elif app == "notepad":
                self._open_notepad()
                return "Opening Notepad."

            else:
                return f"I don't know how to open {app}."

        except Exception as e:
            logger.error(f"Error opening application {app}: {str(e)}")
            return f"Sorry, I couldn't open {app}: {str(e)}"

    @staticmethod
    def _open_chrome():
        """Open Google Chrome browser."""
        try:
            # Try common Chrome installation paths
            paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ]

            for path in paths:
                if os.path.exists(path):
                    subprocess.Popen(path)
                    logger.info("Chrome opened successfully")
                    return

            # If no path found, use webbrowser (default browser)
            webbrowser.open("https://www.google.com")
            logger.info("Chrome opened via webbrowser")

        except Exception as e:
            logger.error(f"Error opening Chrome: {str(e)}")
            raise

    @staticmethod
    def _open_edge():
        """Open Microsoft Edge browser."""
        try:
            paths = [
                r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            ]

            for path in paths:
                if os.path.exists(path):
                    subprocess.Popen(path)
                    logger.info("Edge opened successfully")
                    return

            # Fallback
            subprocess.Popen("msedge.exe")
            logger.info("Edge opened via subprocess")

        except Exception as e:
            logger.error(f"Error opening Edge: {str(e)}")
            raise

    @staticmethod
    def _open_notepad():
        """Open Notepad application."""
        try:
            subprocess.Popen("notepad.exe")
            logger.info("Notepad opened successfully")
        except Exception as e:
            logger.error(f"Error opening Notepad: {str(e)}")
            raise

    # =====================================================================
    # TEXT AUTOMATION ACTIONS
    # =====================================================================

    def write_text(self, params):
        """
        Open Notepad and type the specified text.
        
        Args:
            params (dict): Action parameters containing 'query' (text to type)
            
        Returns:
            str: Response message
        """
        text_to_write = params.get("query", "").strip()

        if not text_to_write:
            return "Please specify what you want me to type."

        logger.info(f"Writing text: {text_to_write}")

        try:
            # Open Notepad
            self._open_notepad()
            time.sleep(1.5)  # Wait for Notepad to fully open

            # Type the text
            logger.debug(f"Typing: {text_to_write}")
            pyautogui.typewrite(text_to_write, interval=0.02)

            response = f"I've typed '{text_to_write}' in Notepad."
            logger.info("Text typed successfully")
            return response

        except Exception as e:
            logger.error(f"Error writing text: {str(e)}")
            return f"Sorry, I couldn't type the text: {str(e)}"
