README
==========================================
Welcome to the inventory automater v 0.01
Author: Jack Frate

This program can be used to automate the input of inventory
information from one file (usually excel) to a destination that one
would otherwise have to enter by hand.

==========================================
Instructions
==========================================

Please speak with whoever set up the program to ensure that the
program is set up properly for your needs.

Support can be found from: jcf9588@rit.edu

==========================================
stuff for nerds:
==========================================
the inventory entering script is built in python

As of v 0.01, it uses two classes, a reader and a writer.

Each reader uses (usually) the openpyxl library to read from
a file containing all of the inventory information

Each writer (usually) uses selenium to automate the input of data
into a web form

The contract between readers and writers as of v 0.01 will be a
python dictionary, with the name of the product as the key, and
a product object as the value.

The product object contains any relevant columns of information pertaining
to the item.

The reader then uses selenium to input them into the browser

==========================================
planned features:
==========================================
support for the BRIM inventory
support for the ONE POS cloud inventory management system
GUI support for easier use by clients, as well as dynamic switching
between different modules
