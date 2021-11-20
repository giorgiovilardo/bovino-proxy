set dotenv-load := false

# Format and lint
default: fmt lint

# Format the code
fmt:
  isort *.py
  black *.py

# Lint the code
lint:
  flake8 --ignore=E501,E722 *.py
