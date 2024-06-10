version=$(shell date)

pypi:
	pyproject-build
	gh release create v.$(version)
	gh release upload v.$(version) dist/*
	twine upload dist/*
	rm -rf dist src/pacflypy.egg-info*
