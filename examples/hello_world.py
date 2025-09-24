#!/usr/bin/env python3
"""
Hello World example for test-project.

This script demonstrates basic hello world functionality.
"""

import sys
from pathlib import Path

# Add the src directory to the path for importing
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from test_project import TestProject, hello_world  # noqa: E402


def main() -> None:
    """Main function demonstrating hello world functionality."""
    print("🌟 test-project - Hello World Demo")
    print("=" * 50)

    # Using the standalone hello_world function
    print("\n1. Standalone function:")
    print(f"   {hello_world()}")
    print(f"   {hello_world('Alice')}")
    print(f"   {hello_world('Developer')}")

    # Using the class method
    print("\n2. Class method:")
    instance = TestProject()
    print(f"   {instance.hello_world()}")
    print(f"   {instance.hello_world('Bob')}")
    print(f"   {instance.hello_world('World')}")

    # With configuration
    print("\n3. With configuration:")
    config = {"greeting_style": "friendly"}
    configured_instance = TestProject(config)
    print(f"   {configured_instance.hello_world('Team')}")

    print("\n✅ Hello World demo completed!")


if __name__ == "__main__":
    main()
