from setuptools import setup, find_packages


__version__ = "1.0.1"


setup(
    # package name in pypi
    name="wagtail-extendedsearch",
    # extract version from module.
    version=__version__,
    description="Add some more functionality to the wagtail elasticsearch search backend",
    long_description="...",
    classifiers=[],
    keywords="",
    author="Lars van de Kerkhof",
    author_email="no@way.why",
    url="https://github.com/specialunderwear/wagtail-extendedsearch",
    license="GPL v2.1",
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    namespace_packages=[],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=["setuptools", "wagtail"],
    # mark test target to require extras.
    extras_require={"test": []},
)
