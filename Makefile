.PHONY: test tdd

test:
	nosetests tests/*.py

tdd:
	nosyd -1
