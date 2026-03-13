from setuptools import setup

setup(
    name="MRP",
    version="0.0.1",
    install_requires=[
        "requests",
        'importlib-metadata; python_version<"3.10"',
        "pandas",
        "jsonschema",
    ],
)
