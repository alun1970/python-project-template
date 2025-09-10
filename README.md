# {{PROJECT_NAME}}

A {{PROJECT_DESCRIPTION}}.

## Features

- Feature 1
- Feature 2  
- Feature 3

## Installation

### From Source (Development)

```bash
# Clone the repository
git clone https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_NAME}}.git
cd {{PROJECT_NAME}}

# Install in development mode
pip install -e .
```

### From Git Repository

```bash
pip install git+https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_NAME}}.git
```

### From PyPI (when published)

```bash
pip install {{PROJECT_NAME}}
```

## Quick Start

### Hello World Example

```python
from {{MODULE_NAME}} import hello_world

# Simple greeting
print(hello_world())  # "Hello, World! Welcome to {{PROJECT_NAME}}!"

# Personalized greeting  
print(hello_world("Alice"))  # "Hello, Alice! Welcome to {{PROJECT_NAME}}!"
```

### Basic Usage

```python
from {{MODULE_NAME}} import {{MAIN_CLASS}}, main_function, hello_world

# Using the hello world function
greeting = hello_world("Developer")
print(greeting)

# Using the main class
instance = {{MAIN_CLASS}}()
greeting = instance.hello_world("User")
print(greeting)

# Basic processing
result = main_function("example")
print(result)
```

## Usage

### Basic Usage

```python
from {{MODULE_NAME}} import {{MAIN_CLASS}}, hello_world

# Hello World functionality
print(hello_world())  # Basic greeting
print(hello_world("Developer"))  # Personalized greeting

# Using the main class
instance = {{MAIN_CLASS}}()
print(instance.hello_world("User"))  # Class method greeting

# Basic processing
result = instance.process("some data")
print(result)
```

### Advanced Usage

```python
from {{MODULE_NAME}} import (
    {{MAIN_CLASS}},
    configure_settings,
    utility_function,
    hello_world
)

# Configure settings
configure_settings({
    "setting1": "value1",
    "setting2": "value2"
})

# Advanced usage with configuration
config = {"greeting_style": "formal", "debug": True}
instance = {{MAIN_CLASS}}(config)

# Use hello world with configured instance
greeting = instance.hello_world("Administrator")
print(greeting)

# Advanced processing
result = instance.advanced_process(data, {"mode": "enhanced"})
```

## Development

### Setup Development Environment

```bash
# Clone and setup
git clone https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_NAME}}.git
cd {{PROJECT_NAME}}

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
make test

# Quick test of Hello World functionality (no venv needed)
make test-hello

# Run Hello World demo
make demo-hello

# Run with coverage
make test-coverage

# Run specific test file
python -m pytest tests/test_specific.py -v
```

### Quality Assurance

```bash
# Run full QA suite (tests, linting, formatting, type checking)
make qa

# Run individual checks
make lint      # Linting with ruff
make format    # Formatting with black
make typecheck # Type checking with mypy
```

### Building and Publishing

```bash
# Clean previous builds
make clean

# Build package
make build

# Publish to PyPI (requires authentication)
make publish
```

## Project Structure

```
{{PROJECT_NAME}}/
├── src/
│   └── {{MODULE_NAME}}/
│       ├── __init__.py
│       ├── core.py
│       ├── config.py
│       ├── utils.py
│       └── py.typed
├── tests/
│   ├── __init__.py
│   ├── test_{{MODULE_NAME}}.py
│   └── conftest.py
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
├── docs/
│   ├── API.md
│   └── USAGE.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── .copilot-instructions.md
├── pyproject.toml
├── Makefile
├── requirements-dev.txt
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the QA suite (`make qa`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a history of changes to this project.

## Support

- Documentation: [docs/](docs/)
- Issues: [GitHub Issues](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_NAME}}/issues)
- Discussions: [GitHub Discussions](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_NAME}}/discussions)
