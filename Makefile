VENV=example_env

# works with mkvirtualenv
all: init info

init:
	virtualenv -p /usr/bin/python2.7 ~/.virtualenvs/$(VENV)
	~/.virtualenvs/$(VENV)/bin/pip install -r requirements.txt

info:
	@echo '>>> Type "workon example_env" in the terminal to use the virtualenv'


test:
	python -m pytest -v -s

clean:
	rm -f *.pyc *~
	rm -f tests/*.pyc tests/*~
	rm -rf __pycache__ 
	rm -rf tests/__pycache__ 

.PHONY: all init test info
