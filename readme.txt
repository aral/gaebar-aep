Gaebar (Google App Engine Backup and Restore) Beta 3
====================================================

A Naklab™ production sponsored by the <head> web conference - http://headconference.com

Copyright (c) 2009 Aral Balkan. http://aralbalkan.com

Released under the GNU GPL v3 License. See license.txt for the full license or read it here:
http://www.gnu.org/licenses/gpl-3.0-standalone.html

Gebar app-engine-patch for Django Test App
------------------------------------------

Functional tests for Gaebar running on app-engine-patch-based Django app.

INSTALLATION
============

1. If you downloaded the release build, skip to Step 3.

2. If you cloned the Git repository, don't forget to init and update your submodules:

git submodule init
git submodule update

3. IMPORTANT: Follow the installation instructions in the Gaebar project (gaebar/readme.txt).


USAGE
=====

1. Start a new server on port 8000:

./manage.py runserver 8000

2. Start a new server on port 8080:

./manage.py runserver 8080

3. Hit http://localhost:8080 in your browser and follow the instructions to run the tests.


LINUX USERS
===========

Don't forget to add a soft link in this project to the local SDK before running the app:

ln -s /path/to/google_appengine/ .google_appengine


FAQ
===

Q. I'm getting the following error:

<class 'django.template.TemplateSyntaxError'> . . . No module named gaebar.

A. You forgot to init and update the gaebar submodule after cloning from the Git respository (see installation section, above).


Q. I'm getting the following error:

AttributeError at /populate-datastore/
'module' object has no attribute 'old_remove'

You didn't patch your copy of dev_appserver.py as instructed in the Gaebar installation instructions (see http://aralbalkan.com/1440, and make sure you follow the Gaebar installation instructions in gaebar/readme.txt).
