# CHEME_599_Amphiphiliphile-

The purpose of this project is to distinguish aqueous from oil phase droplets, along with "lenses" where one type of droplet may be formed over the other. The two goals of the project will be to count the number of each type of droplet and quantify their brightness over time. 


Use cases:
Our current set of functions are designed to detect bright circles from a dark background.  In our case, we use these functions for the following purposes:
1) to detect regions of aqueous dye encapsulated by a membrane.
2) by first inverting the image intensity values, we hope to use these functions to detect oil droplets (dye-free regions) from a dye-free background.

More generally, this code could be used to:
1) detect dyed emulsions from a dye-free background
2) detect stars in the night sky
