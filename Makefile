.PHONY: check lint install type-check

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

check:
	find . -name "*.py" -type f -exec python -m py_compile {} +

type-check:
	mypy --config-file=mypy.ini .

all: install lint check type-check
