import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutorenable_courseware_mfe", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-enable_courseware_mfe",
    version=ABOUT["__version__"],
    url="https://github.com/myusername/tutor-contrib-enable_courseware_mfe",
    project_urls={
        "Code": "https://github.com/myusername/tutor-contrib-enable_courseware_mfe",
        "Issue tracker": "https://github.com/myusername/tutor-contrib-enable_courseware_mfe/issues",
    },
    license="AGPLv3",
    author="Lawrence McDaniel",
    description="enable_courseware_mfe plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor"],
    entry_points={
        "tutor.plugin.v1": ["enable_courseware_mfe = tutorenable_courseware_mfe.plugin"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
