********************* About Module ***********************

This is a module in python 3.0 that contains 2 functions.

1. search4letter(arg1,arg2)
	This returns a set of letters that are common from string arg1 and string arg2.


2. search4vowel(arg1)
	This returns a set of vowels that are present in string arg1.

****************** How to install the module into site packages *********************

In order to install the module you need to perform the following tasks:(but before that
make sure that python 3+ is installed in your system and the Environmental variables 
are set. Also for step 4 check the extension of you distro file and modify the command
accordingly.)

	a. Open cmd prompt.
	
	b. Change directory to the folder having setup.py and vsearch.py files.
	
	c. type the following command :
		py -3 setup.py sdist
	   A distribution file will be created now change directory to the dist file
	
	d. type the following command :
		py -3 -m pip install vsearch-1.0.tar.gz
	   Module will be installed into your site packages.
