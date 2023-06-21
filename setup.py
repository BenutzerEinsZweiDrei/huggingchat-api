from setuptools import setup, find_packages

setup(
    name="hugchat_api",
    version="0.1.0",
    author="ogios",
    author_email="2134692955@qq.com",
    description="Hugging chat web api, use for chat with an Open-Assistant language model, 'Search Web' supported.",
    url="https://github.com/ogios/huggingchat-api",
    packages=find_packages("hugchat_api"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    exclude_package_data={
        "bandwidth_reporter": ["*.json"],
    },
    install_requires=[
        "requests",
    ],
    extras_require=[
        "pycurl",
    ],
    license="GNU General Public License v3.0",
    long_description=open("./README.md", "r").read(),
    long_description_content_type='text/markdown',
)