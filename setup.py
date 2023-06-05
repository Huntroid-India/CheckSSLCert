import setuptools

setuptools.setup(
    name='CheckSSLCert',
    version='0.1.1',
    url='https://github.com/Huntroid-India/CheckSSLCert',
    project_urls={
        "Bug Tracker": "https://github.com/Huntroid-India/CheckSSLCert/issues",
    },
    license='MIT',
    author='Srimath',
    author_email='srimath8@gmail.com',
    description='CheckSSLCert is a Python library that allows you to check the SSL certificate status.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    package_dir={'': "src"},
    packages=setuptools.find_packages("src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    python_requires='>=3.6'
)
