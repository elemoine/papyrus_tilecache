import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

install_requires = [
    'pyramid',
    'WebError',
    'TileCache'
    ]

setup_requires = [
    'nose'
    ]

tests_require = install_requires + [
    'coverage'
    ]

setup(name='papyrus_tilecache',
      version='0.2',
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
      install_requires=install_requires,
      setup_requires=setup_requires,
      tests_require=tests_require,
      test_suite="papyrus_tilecache.tests",
      entry_points = """\
      [paste.app_factory]
      main = papyrus_tilecache:main
      """,
      paster_plugins=['pyramid'],
      )
