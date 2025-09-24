"""
test-project - A test Python project

This package provides [brief description of functionality].

Key features:
- Feature 1
- Feature 2
- Feature 3
"""

from .config import (
    configure_settings,
    get_settings,
)
from .core import (
    TestProject,
    hello_world,
    main_function,
)
from .utils import (
    helper_function,
    utility_function,
)

__version__ = "0.1.0"
__author__ = "Test Author"
__email__ = "test@example.com"

__all__ = [
    # Core functionality
    "TestProject",
    "main_function",
    "hello_world",
    # Configuration
    "configure_settings",
    "get_settings",
    # Utilities
    "utility_function",
    "helper_function",
]
