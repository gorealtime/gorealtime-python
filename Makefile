requests:
	rm -fr gorealtime/vendor/requests
	git clone https://github.com/kennethreitz/requests.git
	mv requests/requests gorealtime/vendor
	rm -fr requests

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
