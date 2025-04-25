.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Sets up the local environment (e.g. install git hooks)
	scripts/local-setup.sh

.PHONY: add-package
add-package: ## Add package to the project ex: make add-package package=XX
	poetry add $(package)

.PHONY: install
install:    ## Run the app
	poetry run poetry install --no-root

.PHONY: up
up:    ## Run the app
	poetry run fastapi dev

.PHONY: update
update: ## Updates the app packages
	poetry update

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	poetry run mypy .

.PHONY: check-format
check-format: ## Checks the code format
	poetry run yapf --diff --recursive **/*.py

.PHONY: check-style
check-style: ## Checks the code style
	poetry run ruff check **/*.py

.PHONY: reformat
reformat:  ## Format python code
	poetry run yapf --parallel --recursive -ir .

.PHONY: test
test: ## Run all the tests
	PYTHONPATH=. poetry run pytest -n auto tests -ra

.PHONY: watch
watch: ## Run all the tests
	PYTHONPATH=. poetry run ptw --runner "pytest -n auto tests -ra"

.PHONY: pre-commit
pre-commit: check-format check-typing check-style test

