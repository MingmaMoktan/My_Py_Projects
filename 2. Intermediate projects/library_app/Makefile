PYTHON=python3
PIP=pip3

PYDOC=pydoc3
PYTEST=pytest

FOLDER_SRC=src
APP_ENTRYPOINT=$(FOLDER_SRC)/main.py

help: ## Prints these help pages
	$(info Commands available:)
	$(info )
	@grep '^[[:alnum:]_-]*:.* ##' $(MAKEFILE_LIST) \
		| sort | awk 'BEGIN {FS=":.* ## "}; {printf "%-25s %s\n", $$1, $$2};'

run: ## Run the code
	@$(PYTHON) $(APP_ENTRYPOINT)

test: ## Run tests in the tests/ folder. Outputs HTML results in folder htmlcov/
	$(PYTEST) -vv --cov=src --cov-report html
	$(PYTEST) -vv --cov=src

doc: ## Output pdoc HTML code documentation into folder docs/
	rm -rf ./docs
	PYTHONPATH="." pdoc $(FOLDER_SRC)/* -o docs --docformat google

clean: ## Remove all automatically generated files and folders
	rm -rf docs/
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm .coverage
	rm -rf __pycache__

install-deps: ## Install all required pip packages
	$(PIP) install -r requirements.txt