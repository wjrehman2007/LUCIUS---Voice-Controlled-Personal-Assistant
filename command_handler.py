"""
Command Handler Module
Parses natural language commands and routes them to appropriate actions
Uses intent matching and parameter extraction
"""

import re
import logging
from actions import ActionExecutor
from logger_config import setup_logger

logger = setup_logger("CommandHandler")


class CommandHandler:
    """
    Parses user commands and delegates to ActionExecutor.
    Supports flexible natural language input.
    """

    def __init__(self):
        """Initialize command handler and action executor."""
        logger.info("Initializing Command Handler...")
        self.action_executor = ActionExecutor()
        self.commands = self._define_commands()
        logger.info("✓ Command Handler initialized")

    def _define_commands(self):
        """
        Define all supported commands with regex patterns and metadata.
        
        Returns:
            dict: Command definitions with patterns, intents, and handlers
        """
        commands = {
            # System commands
            "shutdown": {
                "patterns": [
                    r"(shut\s?down|power\s?off|turn\s?off)",
                    r"(shut\s?down the|power\s?off the) ?(pc|computer|system|machine)",
                ],
                "intent": "system_shutdown",
                "requires_confirmation": True,
            },
            "restart": {
                "patterns": [
                    r"(restart|reboot)",
                    r"(restart|reboot) (the|your) ?(pc|computer|system|machine)",
                ],
                "intent": "system_restart",
                "requires_confirmation": True,
            },
            "time": {
                "patterns": [
                    r"(what\s+is\s+the\s+)?time",
                    r"tell\s+me\s+the\s+time",
                    r"current\s+time",
                    r"what\s+time\s+is\s+it",
                ],
                "intent": "get_time",
                "requires_confirmation": False,
            },
            # Browser/Search commands
            "search": {
                "patterns": [
                    r"search\s+(?:for\s+)?(.+)",
                    r"google\s+(?:for\s+)?(.+)",
                    r"look\s+up\s+(.+)",
                    r"find\s+(.+)",
                ],
                "intent": "web_search",
                "requires_confirmation": False,
                "capture_group": 1,
            },
            "open_chrome": {
                "patterns": [
                    r"(open|start|launch)\s+(chrome|google|browser)",
                    r"(please\s+)?(open|start|launch)\s+(chrome|google|browser)",
                ],
                "intent": "open_application",
                "requires_confirmation": False,
                "app": "chrome",
            },
            "open_edge": {
                "patterns": [
                    r"(open|start|launch)\s+(edge|microsoft\s+edge)",
                ],
                "intent": "open_application",
                "requires_confirmation": False,
                "app": "edge",
            },
            # Text automation
            "open_notepad": {
                "patterns": [
                    r"(open|start|launch)\s+notepad",
                    r"(please\s+)?(open|start|launch)\s+notepad",
                ],
                "intent": "open_application",
                "requires_confirmation": False,
                "app": "notepad",
            },
            "write_text": {
                "patterns": [
                    r"(open notepad and )?(write|type)\s+(.+)",
                    r"(please\s+)?(write|type)\s+(.+)",
                    r"(add|open notepad and add)\s+(.+)",
                ],
                "intent": "write_text",
                "requires_confirmation": False,
                "capture_group": 2,  # or 3 depending on pattern
            },
            # Information
            "weather": {
                "patterns": [
                    r"what\s+is\s+the\s+weather",
                    r"weather",
                    r"how\s+is\s+the\s+weather",
                ],
                "intent": "get_weather",
                "requires_confirmation": False,
            },
            "help": {
                "patterns": [
                    r"(help|what\s+can\s+you\s+do|what\s+commands|available\s+commands)",
                ],
                "intent": "show_help",
                "requires_confirmation": False,
            },
        }

        return commands

    def parse_command(self, text):
        """
        Parse natural language command text.
        
        Args:
            text (str): User command as text
            
        Returns:
            tuple: (action, parameters) where action is command type and parameters is dict
        """
        if not text or not isinstance(text, str):
            logger.warning("Invalid command text provided")
            return "no_action", {"message": "No valid command detected"}

        text_lower = text.lower().strip()
        logger.debug(f"Parsing command: {text_lower}")

        # Try to match against defined commands
        for command_name, command_def in self.commands.items():
            patterns = command_def.get("patterns", [])

            for pattern in patterns:
                match = re.search(pattern, text_lower)
                if match:
                    logger.info(f"✓ Matched command: {command_name}")

                    # Extract parameters if needed
                    parameters = {"intent": command_def["intent"]}

                    # Add confirmation requirement
                    if command_def.get("requires_confirmation"):
                        parameters["requires_confirmation"] = True

                    # Extract captured groups
                    if "capture_group" in command_def:
                        try:
                            captured = match.group(command_def["capture_group"])
                            parameters["query"] = captured.strip()
                        except (IndexError, AttributeError):
                            pass

                    # Add app name if present
                    if "app" in command_def:
                        parameters["app"] = command_def["app"]

                    # Return specific action based on intent
                    action = self._intent_to_action(command_def["intent"], parameters)
                    return action, parameters

        # No command matched
        logger.warning(f"Unknown command: {text_lower}")
        return "unknown", {"message": "I didn't understand that command"}

    def _intent_to_action(self, intent, parameters):
        """
        Convert intent to specific action.
        
        Args:
            intent (str): Intent type
            parameters (dict): Command parameters
            
        Returns:
            str: Action identifier
        """
        action_map = {
            "system_shutdown": "system_shutdown",
            "system_restart": "system_restart",
            "get_time": "get_time",
            "web_search": "web_search",
            "open_application": "open_application",
            "write_text": "write_text",
            "get_weather": "get_weather",
            "show_help": "show_help",
        }

        return action_map.get(intent, "unknown")

    def execute_command(self, action, parameters):
        """
        Execute the parsed command.
        
        Args:
            action (str): Action to execute
            parameters (dict): Action parameters
            
        Returns:
            str: Response message to speak
        """
        logger.info(f"Executing action: {action}")

        try:
            # Handle confirmation required commands
            if parameters.get("requires_confirmation"):
                logger.info(f"Action requires confirmation: {action}")
                # In a real scenario, you'd ask for confirmation
                # For now, we proceed (you could implement two-way confirmation)

            # Delegate to action executor
            response = self.action_executor.execute(action, parameters)
            return response

        except Exception as e:
            logger.error(f"Error executing action {action}: {str(e)}")
            return f"There was an error executing the command: {str(e)}"
