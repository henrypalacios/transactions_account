.ONESHELL:
all: install

PYTHON_VENV = .venv
REQUIREMENT = requirements.txt


install: venv 
	. $(PYTHON_VENV)/bin/activate && \
	pip install --upgrade pip && \
	pip install -r $(REQUIREMENT) 

venv:
	@echo "🕵 Checking virtual enviroment..."
	@echo $(shell [ -d $(PYTHON_VENV) ] || \
	echo "Creating $(PYTHON_VENV)"; \
	python3 -m venv $(PYTHON_VENV);)

clean:
	rm -rf "./$(PYTHON_VENV)"
