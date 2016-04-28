from setuptools import setup, find_packages

setup(
    name="py_poormans_db",
    version="0.1.0",
    packages=find_packages(),
    package_dir={"": "src"},
    entry_points={
        "poormans_db.some_data": "some_data = some_data:build"},
)
