BASEDIR=./PyChat
TESTDIR=./PyChat/tests

all : clean tests

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
tests :
	@python3 ./main_tests.py
build :
	python setup.py sdist
upload :
  python setup.py sdist upload
