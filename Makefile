.PHONY: install

archive.html:
	immaterial-digital-labor-html < archive.csv > archive.html

archive.csv:
	immaterial-digital-labor-archive > archive.csv

install:
	sudo python3 setup.py
