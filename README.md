HOW TO INSTALL AND USE THE PACKAGE
----------------------
This package is best used in a jupyter notebook!

Two installation methods:

Jupyter notebook installation (recomended):
1. "Go to examples/usage_examples"/ and run the first cell of installation.ipynb to check the jupyter notebook environment.
2. Using the terminal in the highest level of the CHEME599_Amphiphilphile- repository, outside of the python environment, run the following command:

"your_path setup.py install"/n
Where "your_path" is the path produced in the first cell of installation.ipynb. 

For example if your path is "C:\\Users\\bubbl\\Anaconda3\\envs\\py36\\python.exe" then your command is "C:\\Users\\bubbl\\Anaconda3\\envs\\py36\\python.exe setup.py install".
3. Run the remaining cell in installation.ipynb to confirm that the package can be imported successfully. 

Terminal/command line installation:
1. Outside of the python environment in CHEME599_Amphiphilphile run the command "python setup.py install".
2. To confirm that the package is installed run "import amph" in your python environment in the terminal.

To understand package usage, please see the other notebooks in the "examples" directory. There is a notebook for each class as described in the package orgnaization below.

PACKAGE DETAILS
---------------

The purpose of this project is to distinguish aqueous from oil phase droplets, along with "lenses" where one type of droplet may be formed over the other. The two goals of the project will be to count the number of each type of droplet and quantify their brightness over time. 

Use cases:
Our current set of functions are designed to detect bright circles from a dark background.  In our case, we use these functions for the following purposes:
1) to detect regions of aqueous dye encapsulated by a membrane.
2) by first inverting the image intensity values, we hope to use these functions to detect oil droplets (dye-free regions) from a dye-free background.

More generally, this code could be used to:
1) detect dyed emulsions from a dye-free background
2) detect stars in the night sky

PACKAGE ORGANIZATION
--------------------

The package is split into three clases:
1. blob_detection class has functions which use the blob_detection method built into scipy. Does not work across a series of images.
2. segementaion class has functions which use a segmentation method build from scratch using scipy modules. Does not work across a series of images.
3. time_series has functions which can work across a series of images.
