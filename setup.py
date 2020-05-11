import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="glowingbike",  # Replace with your own username
    version="1.0.3",
    author="Marco",
    author_email=None,
    description="Upgrade your bike with LEDs, raibows and turn signals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcoEDU/The-Glowing-Bike-Project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'neopixel-plus',
        'keyboard'
    ]
)
