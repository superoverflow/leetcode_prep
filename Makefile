fmt:
	black ./src/ ./tests/
	isort ./src/ ./tests/

test:
	pytest -vv tests/