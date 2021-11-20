# Format and lint
default: fmt lint

# Format the code
fmt:
  isort *.py
  black *.py

# Lint the code
lint:
  flake8 *.py
