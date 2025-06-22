Here are important commands for the uv package manager:

## Project Management
- `uv init` - Initialize a new Python project with pyproject.toml
- `uv init --lib` - Initialize a library project
- `uv add <package>` - Add a dependency to the project
- `uv add --dev <package>` - Add a development dependency
- `uv remove <package>` - Remove a dependency
- `uv sync` - Install dependencies from lockfile
- `uv lock` - Update the lockfile without installing

## Python Installation & Management
- `uv python install <version>` - Install a specific Python version
- `uv python list` - List available Python installations
- `uv python find` - Find Python installations on the system

## Virtual Environment Management
- `uv venv` - Create a virtual environment
- `uv venv --python <version>` - Create venv with specific Python version
- `uv venv <name>` - Create named virtual environment

## Package Installation
- `uv pip install <package>` - Install packages (like pip)
- `uv pip install -r requirements.txt` - Install from requirements file
- `uv pip install -e .` - Install current project in editable mode
- `uv pip list` - List installed packages
- `uv pip freeze` - Output installed packages in requirements format

## Running Code
- `uv run <script>` - Run a Python script in the project environment
- `uv run python` - Start Python interpreter in project environment
- `uv run --with <package> <script>` - Run script with additional temporary dependencies

## Tool Management
- `uv tool install <package>` - Install a tool globally
- `uv tool run <tool>` - Run a tool without installing it
- `uv tool list` - List installed tools
- `uv tool uninstall <package>` - Uninstall a global tool

## Cache Management
- `uv cache clean` - Clear the package cache
- `uv cache dir` - Show cache directory location

## Utility Commands
- `uv --version` - Show uv version
- `uv help` - Show help information
- `uv tree` - Display dependency tree
- `uv export` - Export dependencies to requirements.txt format

These commands cover the core functionality of uv for managing Python projects, dependencies, environments, and tools efficiently.


Here are the uv commands for exporting to requirements.txt:

## Basic Export
```bash
uv export --format requirements-txt > requirements.txt
```

## Export Options
```bash
# Export only production dependencies (exclude dev dependencies)
uv export --format requirements-txt --no-dev > requirements.txt

# Export with hashes for security
uv export --format requirements-txt --generate-hashes > requirements.txt

# Export without URLs (cleaner format)
uv export --format requirements-txt --no-emit-project > requirements.txt

# Export development dependencies only
uv export --format requirements-txt --only-dev > requirements-dev.txt

# Export to a specific file directly
uv export --format requirements-txt --output-file requirements.txt
```

## Alternative Method
You can also use the traditional pip approach within uv:
```bash
uv pip freeze > requirements.txt
```

## Key Differences
- `uv export` uses the lockfile (uv.lock) and respects dependency groups
- `uv pip freeze` shows currently installed packages in the environment
- `uv export` is generally preferred for reproducible builds as it's based on the resolved dependencies

The `uv export --format requirements-txt` command is the recommended approach as it ensures consistency with your project's dependency resolution.

***

Here are the uv commands for exporting to requirements.txt:

## Basic Export
```bash
uv export --format requirements-txt > requirements.txt
```

## Export Options
```bash
# Export only production dependencies (exclude dev dependencies)
uv export --format requirements-txt --no-dev > requirements.txt

# Export with hashes for security
uv export --format requirements-txt --generate-hashes > requirements.txt

# Export without URLs (cleaner format)
uv export --format requirements-txt --no-emit-project > requirements.txt

# Export development dependencies only
uv export --format requirements-txt --only-dev > requirements-dev.txt

# Export to a specific file directly
uv export --format requirements-txt --output-file requirements.txt
```

## Alternative Method
You can also use the traditional pip approach within uv:
```bash
uv pip freeze > requirements.txt
```

## Key Differences
- `uv export` uses the lockfile (uv.lock) and respects dependency groups
- `uv pip freeze` shows currently installed packages in the environment
- `uv export` is generally preferred for reproducible builds as it's based on the resolved dependencies

The `uv export --format requirements-txt` command is the recommended approach as it ensures consistency with your project's dependency resolution.