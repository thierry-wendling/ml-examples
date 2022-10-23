PYTHON_VERSION=3.10.4
VENV_PATH =.venv
VENV_BIN = $(VENV_PATH)/bin

.PHONY: help
.DEFAULT_GOAL := help

#help: @ Lists all available commands
help:
	@grep -E '[a-zA-Z\.\-]+:.*?@ .*$$' $(MAKEFILE_LIST) --no-filename | tr -d '#' | awk 'BEGIN {FS = ":.*?@ "}; \
	{printf "\033[36m%-35s\033[0m %s\n", $$1, $$2}' | sort

#env.setup: @ Installs environment dependencies, creates virtual environment and install dev python packages
env.setup: e.install-environment-dependencies e.create-virtualenv e.install-python-dependencies

#env.delete: @ Removes the current environment
env.delete:
	rm -rf $(VENV_PATH)

export HOMEBREW_NO_AUTO_UPDATE = 1
e.install-environment-dependencies:	
	-brew install pyenv
	-bash -c 'pyenv install $(PYTHON_VERSION)' 
	-pip3 install virtualenv

e.create-virtualenv:
	virtualenv -p ~/.pyenv/versions/$(PYTHON_VERSION)/bin/python $(VENV_PATH)

#env.install-python-dependencies: @ Installs development python dependencies
e.install-python-dependencies:
	$(VENV_BIN)/pip install -r requirements.txt
    
run.local:
	$(VENV_BIN)/streamlit run app.py