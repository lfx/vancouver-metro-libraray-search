alias tests := test

# List all the commands in this file
list:
    just -l

# Format and lint code
lint:
    uv run ruff check src
    uv run ruff format src

# Run all the tests against multiple Python versions
test:
    uv run --python 3.11 pytest src/tests/
    uv run --python 3.12 pytest src/tests/
    uv run --python 3.13 pytest src/tests/

# Run the application in debug mode
debug:
    uv run flask --app src/app/main:app run --debug

# Run the application
run:
    uv run flask --app src/app/main:app run
