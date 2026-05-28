# Python CI/CD Test

A sample Python package demonstrating CI/CD with GitHub Actions.

## Features
- Simple package with `greet()` and `add()` functions
- Automated tests with pytest
- CI/CD pipeline with GitHub Actions
- Code coverage reports
- Automated package building (wheel + sdist)

## Local Development

```bash
pip install -e .[dev]
pytest tests/ --verbose