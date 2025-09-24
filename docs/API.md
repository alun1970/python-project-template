# API Reference

## Core Classes

### TestProject

The main class for test-project.

```python
from test_project import TestProject

instance = TestProject(config=None)
```

#### Parameters

- `config` (dict, optional): Configuration dictionary

#### Methods

##### `process(data)`

Process data using the configured settings.

**Parameters:**
- `data`: Input data to process

**Returns:**
- Processed data

**Example:**
```python
instance = TestProject()
result = instance.process("Hello, World!")
```

##### `advanced_process(data, options=None)`

Advanced processing with additional options.

**Parameters:**
- `data`: Input data to process
- `options` (dict, optional): Additional processing options

**Returns:**
- Processed data with advanced features

**Example:**
```python
instance = TestProject()
options = {"mode": "advanced"}
result = instance.advanced_process("data", options)
```

## Functions

### `main_function(data)`

Main function for simple operations.

**Parameters:**
- `data`: Input data

**Returns:**
- Processed result

**Example:**
```python
from test_project import main_function

result = main_function("Hello, World!")
```

### `configure_settings(config)`

Configure global settings.

**Parameters:**
- `config` (dict): Configuration dictionary to merge with defaults

**Example:**
```python
from test_project import configure_settings

configure_settings({
    "setting1": "value1",
    "debug": True
})
```

### `get_settings()`

Get current configuration settings.

**Returns:**
- Current configuration dictionary

**Example:**
```python
from test_project import get_settings

current_config = get_settings()
```

## Utility Functions

### `utility_function(data)`

A utility function that processes data.

**Parameters:**
- `data`: Input data to process

**Returns:**
- Processed string representation

### `helper_function(items, transform=False)`

Helper function to process a list of items.

**Parameters:**
- `items` (list): List of items to process
- `transform` (bool): Whether to apply transformation

**Returns:**
- Processed list of items

## Exceptions

### `test_projectError`

Base exception for test-project.

### `ConfigurationError`

Raised when there's a configuration error.

### `ProcessingError`

Raised when processing fails.

## Configuration Options

The following configuration options are available:

- `setting1`: Description of setting 1
- `setting2`: Description of setting 2  
- `debug`: Enable debug mode (boolean)
