from setuptools import setup

setup(
	name = "simpleRenamer",
	description = "A simple renamer written in Python with some nice options.",
	long_description = "A simple renamer written in Python. simpleRenamer will rename the files of a directory sequentially, that is they will be numbered serially.",
	version = "v.1.1",
	license = "MIT-License",
	author = "Karsten Koenig",
	author_email = "KarstenKoenig@gmx.net",
	url = 'http://www.github.com/raymontag/simpleRenamer',
	download_url = 'http://www.github.com/downloads/raymontag/simpleRenamer/simpleRenamer-v.1.0.tar.gz',
	scripts = ['src/simplerenamer'],
	platforms = "Linux"
)
