# Settings
set shell := ["bash", "-c"]

# Variables
src_dir := "src"
test_dir := "src/tests"
app_entry := "src/app/main:app"

# Default recipe
default: list

# List all the commands in this file
list:
    @just --list

# Install dependencies (sync with uv.lock)
install:
    uv sync

# Format code (modifies files)
fmt:
    uv run ruff format {{src_dir}}

# Lint code (checks only - good for CI)
lint:
    uv run ruff check {{src_dir}}
    uv run ruff format --check {{src_dir}}

# Fix linting issues and format code
fix: fmt
    uv run ruff check --fix {{src_dir}}

# Run tests
test:
    uv run pytest {{test_dir}}

# Run tests with coverage report
coverage:
    uv run pytest --cov={{src_dir}} --cov-report=term-missing {{test_dir}}

# Run tests against multiple Python versions
test-all:
    uv run --python 3.11 pytest {{test_dir}}
    uv run --python 3.12 pytest {{test_dir}}
    uv run --python 3.13 pytest {{test_dir}}

# Run the application in debug mode
debug:
    uv run flask --app {{app_entry}} run --debug

# Run the application
run:
    uv run flask --app {{app_entry}} run

# Clean up cache files
clean:
    rm -rf .ruff_cache .pytest_cache .coverage
    find . -type d -name "__pycache__" -exec rm -rf {} +
