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
	docker compose run --rm --no-deps capitals poetry add $(package)
	make build

.PHONY: up
up:    ## Run the app
	docker compose up --build capitals

.PHONY: down
down: ## Stop and remove all the Docker services, volumes and networks
	docker compose down -v --remove-orphans

.PHONY: build
build: ## Builds the app
	docker build --no-cache -t capitals .

.PHONY: update
update: ## Updates the app packages
	docker compose run --rm --no-deps capitals poetry update

.PHONY: install
install: ## Installs a new package in the app. ex: make install package=XXX
	docker compose run --rm --no-deps capitals poetry add $(package)
	docker build --no-cache -t capitals .

.PHONY: run
run: ## Runs the app
	docker compose run --rm --no-deps capitals

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	docker compose run --rm --no-deps capitals poetry run mypy .

.PHONY: check-format
check-format: ## Checks the code format
	docker compose run --rm --no-deps capitals poetry run yapf --diff --recursive **/*.py

.PHONY: check-style
check-style: ## Checks the code style
	docker compose run --rm --no-deps capitals poetry run ruff check **/*.py

.PHONY: reformat
reformat:  ## Format python code
	docker compose run --rm --no-deps capitals poetry run yapf --parallel --recursive -ir .

.PHONY: test
test: ## Run all the tests
	docker compose run --rm --no-deps capitals poetry run pytest -n auto tests -ra

.PHONY: watch
watch: ## Run all the tests
	docker compose run --rm --no-deps capitals poetry run ptw --runner "pytest -n auto tests -ra"

.PHONY: pre-commit
pre-commit: check-format check-typing check-style test

