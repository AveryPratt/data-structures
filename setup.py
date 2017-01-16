"""Setup file for data structures assignment."""


from setuptools import setup


setup(
    name="data_structures",
    description="Classic data structures implemented in Python.",
    version=0.1,
    author="Patrick & Joey & Avery & Claire & Benny",
    author_email="",
    license="MIT",
    py_modules=['linked_list', 'stack'],
    package_dir={'': 'src'},
    install_requires=[''],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
)
