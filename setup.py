from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

long_description = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="nastya-sort",
    version="0.1.0",
    description="Simple sort utility implemented in Python with Click",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/your-username/nastya-sort",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0",
    ],
    entry_points={
        "console_scripts": [
            # expose command 'nastya-sort' so user can run `nastya-sort` after pip install
            "nastya-sort = nastya_sort.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
