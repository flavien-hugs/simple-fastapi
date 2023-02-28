MANAGE := python

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	pipenv shell

freeze: ## Pin current dependencies
	pipenv requirements > requirements.txt

.PHONY: install
install: ## Install or update dependencies
	pip install -r requirements.txt

.PHONY: runserver
runserver: ## Run the server
	uvicorn core.main:app --port 8070 --reload

.PHONY: kill-process
kill-process: ## Kill process the server
	sudo lsof -t -i tcp:8000 | xargs kill -9
