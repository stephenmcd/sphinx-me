
import sys
from shutil import rmtree
from setuptools import setup


if sys.argv[:2] == ["setup.py", "bdist_wheel"]:
    # Remove previous build dir when creating a wheel build,
    # since if files have been removed from the project,
    # they'll still be cached in the build dir and end up
    # as part of the build, which is unexpected.
    try:
        rmtree("build")
    except:
        pass


setup(
    name="sphinx-me",
    version=__import__("sphinx_me").__version__,
    author="Stephen McDonald",
    author_email="stephen.mc@gmail.com",
    description="Wraps your README-only projects in a dynamic Sphinx shell "
                "for hosting on http://readthedocs.org",
    long_description=open("README.rst").read(),
    license="BSD",
    url="http://github.com/stephenmcd/sphinx-me/",
    py_modules=["sphinx_me",],
    entry_points="""
        [console_scripts]
        sphinx-me=sphinx_me:install
    """,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Utilities",
    ]
)
