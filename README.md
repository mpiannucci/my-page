myPage
======

My personal web site and blog.

Created Using the web.py framework for python 2.7 and the Google App Engine.

Dependencies: <br/>
	* python 2.7 <br/>
	* web.py module <br/>
	* GAE

Getting the Python Dependencies
-----------------------

Download the web.py Python module:

    cd myPage/
    pip install web.py -t .
    rm -r web.py-0.37.egg-info/

Running the Webapp
------------------

First, compile the templates used by web.py:

    ./CompileTemplates

Then, run the development web server

    dev_appserver.py app.yaml