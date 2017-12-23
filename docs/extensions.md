# Extensions

## What are extensions?

Extensions make it possible to filter search results by custom functions. They can be written in C or Python.

Custom functions always return a whole number. The *image\_width()* function from the [gdk-pixbuf extension]((http://github.com/20centaurifux/efind-gdkpixbuf)) is a good example. You can search for JPEG files wider than 800 pixels with the following command:

	$ efind . 'name="*.jpg" and image_width()>800'

**efind** translates the first part of the expression and runs GNU find with the following arguments:

	$ find . -name "*.jpg"

Then each found file is filtered by evaluating the second part of the expression.

A function can have optional arguments. Non-zero values evaluate to true. The *artist\_matches()* function from the [taglib extension](http://github.com/20centaurifux/efind-taglib) returns a non-zero value if the specified artist name matches the corresponding ID3 tag:

	$ efind . 'name="*.mp3" and artist_matches("the cure")'

To print a list with available functions run

	$ efind --print-extensions

Extensions can be installed globally in */usr/lib/efind/extensions* or locally in *~/.efind/extensions*. You may want to specify wildcard patterns in a personal blacklist (*~/.efind/blacklist*) to prevent extensions from being loaded. To disable all global Python extensions, for instance, add the following line to your blacklist:  

	/usr/lib/efind/extensions/*.py

Lines starting with an hash (#) are ignored. To display blacklisted extensions type in

	$ efind --print-blacklist

## Available extensions

### gdk-pixbuf

Filter search results by image properties.

[http://github.com/20centaurifux/efind-gdkpixbuf](http://github.com/20centaurifux/efind-gdkpixbuf)

### py-path

Filter search results by file extension and mime-type.

[http://github.com/20centaurifux/efind-py-path](http://github.com/20centaurifux/efind-py-path)

### py-mail

Filter emails by headers and body.

[http://github.com/20centaurifux/efind-py-mail](http://github.com/20centaurifux/efind-py-mail)

### taglib

Filter search results by audio tags and properties.

[http://github.com/20centaurifux/efind-taglib](http://github.com/20centaurifux/efind-taglib)

### text-tools

Filter text files by content.

[http://github.com/20centaurifux/efind-text-tools](http://github.com/20centaurifux/efind-text-tools)
