lint:
	pylint ./app

typecheck:
	mypy ./app

test:
	python3 -m unittest discover ./app -m

