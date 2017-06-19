# Extensions

## What are extensions?

Extensions are custom functions that can be used to filter search results. Hence, you are only allowed to use these functions *after* the search expression.

Custom functions return always a whole number. The "image_width" function from the [gdk-pixbuf extension]((http://github.com/20centaurifux/efind-gdkpixbuf)) is a good example. You can search for JPEG files wider than 800 pixels with the following command:

	$ efind . 'name="*.jpg" and image_width()>800'

**efind** translates the first part of the expression and runs GNU find with the following arguments:

	$ find . -name "*.jpg"

Then each file found by GNU find is filtered by evaluating the second part of the expression.

A function can have optional arguments. Non-zero values evaluate to true. The "artist_matches" function from the [taglib extension](http://github.com/20centaurifux/efind-taglib) returns a non-zero value if the specified artist name matches the artist found in the ID3 tags of the file:

	$ efind . 'name="*.mp3" and artist_matches("the cure")'

To print a list with available functions from installed extensions run

	$ efind --list-extensions

Extensions can be installed globally in */etc/efind/extensions* or localy in *~/.efind/extensions*. Users can specifiy wildcard patterns in a personal blacklist (*~/.efind/blacklist*) to  prevent  extensions from being loaded. To disable all global extensions, for instance, add the following line to your blacklist:  

	/etc/efind/extensions/*

Lines starting with an hash (#) are ignored.

## Available extensions

### py-path

Filter search results by file extension and mime-type.

[http://github.com/20centaurifux/efind-py-path](http://github.com/20centaurifux/efind-py-path)

### taglib

Filter search results by audio tags and properties.

[http://github.com/20centaurifux/efind-taglib](http://github.com/20centaurifux/efind-taglib)

### gdk-pixbuf

Filter search results by image properties.

[http://github.com/20centaurifux/efind-gdkpixbuf](http://github.com/20centaurifux/efind-gdkpixbuf)
