"""Setup file for data structures assignment."""


from setuptools import setup


setup(
    name="echo",
    description="A project to build a basic echo server.",
    version=0.1,
    author="Regenal & Joey",
    author_email="regenal@mac.com, joeyderosa11.jd@gmail.com",
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
