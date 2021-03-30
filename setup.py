import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jekyll_tag_gen",
    version="0.0.1",
    author="xunto",
    author_email="xunto.orlov@yandex.ru",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=["pyyaml==5.4"],
    scripts=['bin/jekyll_tag_gen'],
    python_requires='>=3.6',
)
