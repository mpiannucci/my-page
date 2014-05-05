myPage
======

My personal web site and blog.

Created Using the web.py framework for python 2.7 and the Google App Engine.

Dependencies: <br/>
	- python 2.7 <br/>
	- web.py module <br/>
	- GAE

Running the Webapp
------------------

First, compile the templates used by web.py:

    ./CompileTemplates

Then, run the development web server

    dev_appserver.py app.yaml

Updating the Webapp
--------------------

Simply use the following command to upload the newest version of the app to the App Engine. But first, dont forget to update your templates!!

    ./CompileTemplates
    appconfig.py update .

