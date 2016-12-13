"""Setup file for data structures assignment."""


from setuptools import setup


setup(
    name="echo",
    description="A project to build a basic echo server.",
    version=0.1,
    author="Patrick & Joey & Avery",
    author_email="",
    license="MIT",
    py_modules=['linked_list', 'stack'],
    package_dir={'': 'src'},
    install_requires=[''],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        # 'console_scripts': [
        #     "command = module_name:main",
        # ]
    }
)
