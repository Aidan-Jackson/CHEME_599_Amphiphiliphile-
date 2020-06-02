import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()

        setuptools.setup(
                name="cheme599amph", # Replace with your own username
            version="0.0.1",
            author="Aiden Jackson, Miwako Ito, Zack Cohen, Heidi Spears, and Chantelle Leveille",
            author_email="ito.miwa@yahoo.com",
            description="A package for detecting blobs!",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/Aidan-Jackson/CHEME_599_Amphiphiliphile-",
            packages=setuptools.find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            python_requires='>=3.6',
        )
