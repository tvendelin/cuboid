.ONESHELL:

VENV := v
PYTHON=${VENV}/bin/python

all: venv test build

venv:
	python3 -m venv ${VENV}
	. ${VENV}/bin/activate
	pip install build
	pip install .

test: tests ${VENV}
	${PYTHON} -m unittest discover -s tests -b 2> tests.log

build: tests.log
	${PYTHON} -m build

clean:
	rm -rf ${VENV} 
	find . -name '__pycache__' -exec rm -r '{}' \;

	
