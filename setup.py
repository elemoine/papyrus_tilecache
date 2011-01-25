import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = ['pyramid', 'WebError', 'TileCache']

setup(name='papyrus_tilecache',
      version='0.1',
      description='papyrus_tilecache',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Eric Lemoine',
      author_email='eric.lemoine@gmail.com',
      url='http://github.com/elemoine/papyrus_tilecache',
      keywords='web geospatial papyrus tilecache pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="papyrus_tilecache",
      entry_points = """\
      [paste.app_factory]
      main = papyrus_tilecache:main
      """,
      paster_plugins=['pyramid'],
      )
