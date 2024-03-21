# Makefile

# Define the virtual environment name
VENV_NAME = .venv

# Define the Python interpreter
PYTHON = python3.8

# Define the path to the requirements file
REQUIREMENTS_FILE = requirements.txt
REQUIREMENTS_FILE_1 = requirements_torch.txt

.PHONY: venv install clean run_local activate test

# Target to create the virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)


# Target to install packages from requirements file
install:
	@echo "Installing packages from $(REQUIREMENTS_FILE_1)..."
	@pip install -r requirements/$(REQUIREMENTS_FILE_1) -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
	@echo "Installing packages from $(REQUIREMENTS_FILE)..."
	@pip install -r requirements/$(REQUIREMENTS_FILE)
	@echo "Installation complete."

# Target to clean up the virtual environment
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV_NAME)

run_local:
	@python3 -m bot

test_all:
	pytest --cov

test_models:
	pytest --cov -m models

test_bot:
	pytest  --cov -m asyncio

test_utis:
	pytest  --cov -m utils
all: venv 
