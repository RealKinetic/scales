unit: clean
	nosetests -A "speed!='slow'" ${ARGS}

clean:
	find . -name "*.py[co]" -delete
