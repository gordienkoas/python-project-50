install:
	uv sync
lint:
	uv run ruff check gendiff
build:
	uv build
package-install:
	uv tool install dist/*.whl
test:
	uv run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml