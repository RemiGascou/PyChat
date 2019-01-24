BASEDIR=./PyChat
TESTDIR=./PyChat/tests

all : clean tests

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
tests :
	@python3 ${BASEDIR}/main_tests.py
build :
	python3 setup.py sdist
upload :
	python3 setup.py sdist upload
