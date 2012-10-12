save-ipython-variables
======================

You use IPython.  It's pretty great.  But things happen!  Your computer
crashes, your IPython shell crashes (in theory), your computer runs out of
memory and the process becomes unreachable.  You can lose your whole session,
and potentially hours of work.

Sure, you can work out of a file, using `%edit` to keep your code on disk, but
the variables that can take hours to build up -- whether it's through querying
databases, scraping the web, or long-running algorithms -- can just vanish.

This is where this module comes into play: `save-ipython-variables` lets you do
just that -- save your global IPython variables to disk easily, and load them
back into the global namespace when you need them again, even in a whole new
IPython session.

Example Usage
-------------
#TODO
