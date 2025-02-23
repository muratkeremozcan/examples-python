.PHONY: check lint install

install:
	pip install flake8

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

check:
	find . -name "*.py" -type f -exec python -m py_compile {} +

all: install lint check
