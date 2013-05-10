Kokako
======

Identify sounds in a sound file
-------------------------------

This module defines detctors for identifying sounds in sound clips.  Detectors are defined, with each
detector returning a numerical score that may subsequently be used to classify the clip by whether
or not it contains a particular sound.


Installation
------------

This is a python project

1. Get the code `git clone git://github.com/dragonfly-science/kokako.git`
2. Install the dependencies (numpy, matplotlib)
2. Change to the `kokako` directory
3. Run `python setup.py install`

Usage
-----

`python kokako.py --help`

Provides help on how to use `kokako`

`python kokako.py --list`

List available detectors

`python kokako.py <detector name> [<detector version>] [-o <filename>] <path>`

Score sound files. To score a file specify which detector to use (<detector name>), an optional version (<detector version>),
and a path (<path>). If path is a `wav` file then `kokako` will return a single score. If path is a directory, then `kokako` 
will recursively walk that directory scoring all the `wav` files that it finds.


Contribute
----------

You are welcome to contrbute better detectors, or detectors for the sound that you would like to identify. 
Please fork the code on github. 

License
-------

Kokako is released under the  GPL license. In  essence, you are free to use and modify this code, provided that
any changes you make are contributed back to the project.


Songscope
---------

This is the engine of the songscape project (http://wwww.songscape.org), which aims to use machine learning to
analyse sounds in large volumes of sound data.
