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

# Run flask
run:
  flask run

# Run ngrok
host:
  ngrok http --region=eu 5000
