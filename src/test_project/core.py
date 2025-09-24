"""
Core functionality for test-project.

This module contains the main classes and functions for the package.
"""

from typing import Any


class TestProject:
    """Main class for test-project."""

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        """Initialize TestProject.

        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}

    def hello_world(self, name: str | None = None) -> str:
        """Return a Hello World greeting.

        Args:
            name: Optional name to include in greeting

        Returns:
            Hello World greeting string
        """
        if name:
            return f"Hello, {name}! Welcome to test-project!"
        return "Hello, World! Welcome to test-project!"

    def process(self, data: Any) -> Any:
        """Process data using the configured settings.

        Args:
            data: Input data to process

        Returns:
            Processed data
        """
        # Implementation here
        return f"Processed: {data}"

    def advanced_process(self, data: Any, options: dict[str, Any] | None = None) -> Any:
        """Advanced processing with additional options.

        Args:
            data: Input data to process
            options: Additional processing options

        Returns:
            Processed data with advanced features
        """
        options = options or {}
        # Implementation here
        return f"Advanced processed: {data} with options {options}"


def hello_world(name: str | None = None) -> str:
    """Return a Hello World greeting.

    Args:
        name: Optional name to include in greeting

    Returns:
        Hello World greeting string
    """
    if name:
        return f"Hello, {name}! Welcome to test-project!"
    return "Hello, World! Welcome to test-project!"


def main_function(data: Any) -> Any:
    """Main function for simple operations.

    Args:
        data: Input data

    Returns:
        Processed result
    """
    instance = TestProject()
    return instance.process(data)


class test_projectError(Exception):
    """Base exception for test-project."""

    pass


class ConfigurationError(test_projectError):
    """Raised when there's a configuration error."""

    pass


class ProcessingError(test_projectError):
    """Raised when processing fails."""

    pass
