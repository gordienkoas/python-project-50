install:
	poetry install
test:
	poetry run pytest
lint:
	poetry run ruff check .
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml