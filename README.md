myPage
======

My personal web site and blog, [mpiannucci.com](http://mpiannucci.com).

Created using the [web.py](https://github.com/webpy/webpy) framework for python 2.7 and the [Google App Engine](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/introduction).

**Dependencies:**
* Python 2.7
* Web.py
* Google App Engine

Getting the Python Dependencies
-----------------------

Download the Python dependencie:

    cd myPage/
    pip install web.py -t .
    pip install markdown -t .
    rm -r web.py-*
    rm -r markdown-*/


Running the Webapp
------------------

First, compile the templates used by `web.py`:

    ./CompileTemplates

Then, run the development web server

    dev_appserver.py app.yaml
