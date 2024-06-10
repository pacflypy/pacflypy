version=$(shell cat .version)
cdir=$(shell pwd)
size=$(shell du -s $(cdir)/src | cut -f1)
debian-prefix=/lib/python3/dist-packages
termux-prefix=/data/data/com.termux/files/usr/lib/python3.11/site-packages
debian-install=$(cdir)$(debian-prefix)
termux-install=$(cdir)$(termux-prefix)
debian-package=python3-pacflypy_$(version)_all_debian.deb
termux-package=python-pacflypy_$(version)_all_debian.deb

.PHONY: all pypi deb-debian deb-termux

all: pypi deb-debian deb-termux

pypi:
	cd $(cdir)
	pyproject-build
	gh release create v.$(version) --title 'v.$(version)'  --notes-file INSTALL.md
	gh release upload v.$(version) dist/*
	twine upload dist/*
	rm -rf dist src/pacflypy.egg-info*

deb-debian:
	cd $(cdir)
	mkdir -p $(debian-install)
	pip install $(cdir) --target $(debian-install)
	rm -rf build dist
	tar -cJf data.tar.xz ./lib
	rm -rf lib
	echo 'Package: python3-pacflypy' > control
	echo 'Version: $(version)' >> control
	echo 'Section: utils' >> control
	echo 'Priority: optional' >> control
	echo 'Installed-Size: $(size)' >> control
	echo 'Maintainer: pacflypy <pacflypy@outlook.com>' >> control
	echo 'Architecture: all' >> control
	echo 'Depends: python3' >> control
	echo 'Description: A Python Module for Better Development' >> control
	echo '' >> control
	tar -cJf control.tar.xz ./control
	echo 2.0 > debian-binary
	ar rcs $(debian-package) debian-binary control.tar.xz data.tar.xz
	rm -rf debian-binary control.tar.xz data.tar.xz control
	gh release upload v.$(version) $(debian-package)

deb-termux:
	cd $(cdir)
	mkdir -p $(termux-install)
	pip install $(cdir) --target $(termux-install)
	rm -rf build dist
	tar -cJf data.tar.xz ./data
	rm -rf lib
	echo 'Package: python-pacflypy' > control
	echo 'Version: $(version)' >> control
	echo 'Section: utils' >> control
	echo 'Priority: optional' >> control
	echo 'Installed-Size: $(size)' >> control
	echo 'Maintainer: pacflypy <pacflypy@outlook.com>' >> control
	echo 'Architecture: all' >> control
	echo 'Depends: python' >> control
	echo 'Description: A Python Module for Better Development' >> control
	echo '' >> control
	tar -cJf control.tar.xz ./control
	echo 2.0 > debian-binary
	ar rcs $(termux-package) debian-binary control.tar.xz data.tar.xz
	rm -rf debian-binary control.tar.xz data.tar.xz control
	gh release upload v.$(version) $(termux-package)