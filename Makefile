.PHONY: install

archive.csv:
	immaterial-digital-labor-archive > archive.csv

install:
	sudo python3 setup.py
