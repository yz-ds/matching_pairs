.PHONY: format
format:
	poetry run pysen run format

.PHONY: lint
lint:
	poetry run pysen run lint

.PHONY: install
install:
	poetry install --no-root

.PHONY: run
run:
	poetry run python -m src.main
