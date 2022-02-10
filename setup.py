import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_exp_rep",
    version="0.0.1",
    author="Ginan-Team",
    author_email="rmaj@frontiersi.com.au",
    description="Testing installation of External Package from GitHub repo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ronaldmaj/test_exp_rep",
    project_urls={"Bug Tracker": "https://github.com/ronaldmaj/test_exp_rep/issues"},
    license="MIT",
    packages=["test_exp_rep"],
    install_requires=["unlzw"],
)
