from setuptools import setup

test_dependencies = [
    "pytest==5.3.2"
]

lint_dependencies = ["flake8==3.7.9"]

setup(
    name="ms_corona",
    description="Get Corona Data for Munster",
    version="1.0.0",
    url="https://github.com/bjuli/ms-corona",
    maintainer="bjuli",
    maintainer_email="juliaboschan@gmail.com",
    packages=["ms_corona"],
    install_requires=[
        "bs4==0.0.1",
        "beautifulsoup4==4.9.0",
        "pandas==1.0.3",
        "requests==2.23.0",
        "lxml==4.5.0",
        "click==7.1.1"
    ],
    extras_require={
        "test": test_dependencies,
        "lint": lint_dependencies,
        "dev": test_dependencies + lint_dependencies
    }
)
