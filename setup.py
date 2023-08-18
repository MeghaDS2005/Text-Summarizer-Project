import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "MeghaDS2005"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "1998meghasharma2026@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=3.8,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)