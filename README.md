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

`kokako --help`

Provides help on how to use `kokako`

`kokako --list`

List available detectors

`kokako <detector name> [<detector version>] [-o <filename>] <path>`

Score sound files. To score a file specify which detector to use (<detector name>), an optional version (<detector version>),
and a path (<path>). If path is a `wav` file then `kokako` will return a single score. If path is a directory, then `kokako` 
will recursively walk that directory scoring all the `wav` files that it finds.


Contribute
----------

You are welcome to contrbute better detectors, or detectors for the sound that you would like to identify. 
Please fork the code on github. 


Songscape
---------

Kokako is used by the songscape project (http://www.songscape.org), which aims to use machine learning to
analyse sounds in large volumes of sound data.



Licence
-------

Copyright (C) 2013  Dragonfly Science

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
