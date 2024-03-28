# Makefile

# Define the Python interpreter
PYTHON = python3.8

# Define the path to the requirements file
REQUIREMENTS_FILE = requirements.txt
REQUIREMENTS_FILE_1 = requirements_torch.txt
LINT_TARGET := bot/ tests/
MYPY_TARGET := bot/ tests/


.PHONY: install clean run_local activate test


# Target to install packages from requirements file
install:
	@echo "Installing packages from $(REQUIREMENTS_FILE_1)..."
	@pip install -r requirements/$(REQUIREMENTS_FILE_1) -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
	@echo "Installing packages from $(REQUIREMENTS_FILE)..."
	@pip install -r requirements/$(REQUIREMENTS_FILE)
	@echo "Installation complete."


run_local:
	@python3 -m bot

test_all:
	pytest --cov

test_models:
	pytest --cov -m models

test_bot:
	pytest  --cov -m asyncio

test_utils:
	pytest  --cov -m utils
all: venv 


.PHONY: format
# target: format - Format the code according to the coding styles
format: format-black format-isort


.PHONY: format-black
format-black:
	@black ${LINT_TARGET}


.PHONY: format-isort
format-isort:
	@isort ${LINT_TARGET}

.PHONY: lint
# target: lint - Check source code with linters
lint: lint-isort lint-black lint-flake8 lint-mypy lint-pylint


.PHONY: lint-black
lint-black:
	@${PYTHON} -m black --check --diff ${LINT_TARGET}


.PHONY: lint-flake8
lint-flake8:
	@${PYTHON} -m flake8 --statistics ${LINT_TARGET}


.PHONY: lint-isort
lint-isort:
	@${PYTHON} -m isort.main --df -c ${LINT_TARGET}


.PHONY: lint-mypy
lint-mypy:
	@${PYTHON} -m mypy ${MYPY_TARGET}


.PHONY: lint-pylint
lint-pylint:
	@${PYTHON} -m pylint --rcfile=.pylintrc --errors-only ${LINT_TARGET}