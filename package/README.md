HOW TO USE THE PACKAGE
----------------------

If you are able to run a local jupyter notebook, you can simply run the test.ipynb notebook as is in this repository.
If you are unable to run a local jupyter notebook and wish to use jupyter lab, upload the 'amph' directory and 'test.ipynb' notebook to your jupyter server. Make sure that the python notebook is directly above the 'amph' directory in the file tree.

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

Currently the package is split into two modules, each with one class.
1) blob_detection which uses the prebuilt blob_detection package.
2) other_methods which uses built-from scratch methods.
