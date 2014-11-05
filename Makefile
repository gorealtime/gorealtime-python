.PHONY: requests publish html

requests:
	rm -fr spate/vendor/requests
	git clone https://github.com/kennethreitz/requests.git
	mv requests/requests spate/vendor
	rm -fr requests

publish:
	python setup.py register
	python setup.py sdist bdist_wheel upload

html:
	sphinx-build -Eb html docs docs/_build/
