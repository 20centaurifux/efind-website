# Home

## Overview

**efind** (extendable find) searches for files in a directory hierarchy.

Basically it's a wrapper for [GNU find](https://www.gnu.org/software/findutils/)
providing an easier and more intuitive expression syntax. It can be extended
by custom functions to filter search results.

## Examples

Let's assume you want to find all writable source and header files of a C project
that were modified less than two days ago. That's no problem with **efind's**
self-explanatory expression syntax:

```
$ efind . '(name="*.h" or name="*.c") and type=file and writable and mtime<2 days'
```

Additionally **efind** extensions make it possible to filter search results by details
like audio tags and properties:

```
$ efind ~/music 'name="*.mp3" \
  and artist_matches("David Bowie") and audio_length()>200'
```

## Differences to GNU find

Sometimes GNU find doesn't behave in a way an average user would expect. The following
expression finds all documents in the current folder with a file size less or equal than
1G because every file with at least one byte is rounded up:

```
$ find . -size 1G
```

**efind** converts file sizes to byte to avoid this confusing behaviour:

```
$ efind . "size=1G" --print
$ find . -size 1073741824c
```

## Usage

Running **efind** without any argument the search expression is read from *stdin*
and files are searched in the user's home directory. A different directory and
expression can be specified with the *--dir* and *--expr* options:

```
$ efind --dir=/tmp --expr="size>1M and type=file"
```

**efind** tries to handle the first two arguments as path and expression. It's
valid to run **efind** the following way:

```
$ efind ~/foobar "type=dir"
```

If you want to show the translated arguments without running GNU find use the
*--print* option. To quote special shell characters append *--quote*:

```
$ efind ~/tmp/foo 'iname="*.py" and (mtime<30 days or size>=1M)' --print --quote
```

**efind** is shipped with a manpage, of course.

```
$ man efind
```

## Expression Syntax

A search expression consists of at least one comparison or file flag to test. Multiple
expressions can be evaluated by using conditional operators:

| Operator | Description                                                                                                                                                   |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| and      | If an expression returns logical false it returns that value and doesn't evaluate the next expression. Otherwise it returns the value of the last expression. |
| or       | If an expression returns logical true it returns that value and doesn't evaluate the next expression. Otherwise it returns the value of the last expression.  |

Expressions are evaluated from left to right. Use parentheses to force precedence.

The following operators can be used to compare a file attribute to a value:

| Operator | Description      |
| :------- | :--------------- |
| =        | equals to        |
| >        | greater than     |
| >=       | greater or equal |
| <        | less than        |
| <=       | less or equal    |

A value must be of one of the data types listed below:

| Type          | Description                                                                                                            |
| :------------ | :--------------------------------------------------------------------------------------------------------------------- |
| string        | Quoted sequence of characters.                                                                                         |
| number        | Natural number.                                                                                                        |
| time interval | Time interval (number) with suffix. Supported suffixes are "minute(s)", "hour(s)" and "day(s)".                        |
| file size     | Units of space (number) with suffix. Supported suffixes are "byte(s)", "kilobyte(s)", "megabyte(s)" and "gigabyte(s)". |
| file type     | "file", "directory", "block", "character", "pipe", "link" or "socket".                                                 |

The following file attributes are searchable:

| Attribute | Description                       | Type            | Example     |
| :-------- | :-------------------------------- | :-------------- | :---------- |
| name      | case sensitive filename pattern   | string          | "*.txt"     |
| iname     | case insensitive filename pattern | string          | "Foo.bar"   |
| atime     | last access time                  | time interval   | 1 minute    |
| ctime     | last file status change           | time interval   | 15 hours    |
| mtime     | last modification time            | time interval   | 30 days     |
| size      | file size                         | size            | 10 megabyte |
| group     | name of the group owning the file | string          | "users"     |
| gid       | id of the group owning the file   | number          | 1000        |
| user      | name of the user owning the file  | string          | "john"      |
| uid       | id of the user owning the file    | number          | 1000        |
| type      | file type                         | file type       | pipe        |

Additionally you can test these flags:

| Flag       | Description                             |
| :--------- | :-------------------------------------- |
| readable   | the file can be read by the user        |
| writable   | the user can write to the file          |
| executable | the user is allowed to execute the file |

## Extensions

Extensions are custom functions used to filter find results. A function can
have optional arguments and returns always an integer. Non-zero values evaluate to true.

You are only allowed to use extensions *after* the find expression. 

At the current stage **efind** supports functions loaded from shared libraries.
It's planned to support scripting languages like [Python](https://www.python.org/)
or [GNU Guile](https://www.gnu.org/software/guile/) in the future.

To print a list with available functions found in all installed extensions run

```
$ efind --list-extensions
```

## Getting efind

You can [build](#build-from-source) **efind** from source code or [download](/downloads)
a package for your distribution. If you should miss a package type or if you want to
support **efind** don't hesitate to [contact](/contact) me. Any help is
much appreciated :)

## Build from source

**efind** uses [GNU Make](https://www.gnu.org/software/make/) as build system.
Installation options can be customized in the Makefile.

Please ensure that [GNU Bison](https://www.gnu.org/software/bison/) and
[GNU Flex](https://www.gnu.org/software/flex/) is installed on your system before
you build **efind**.

If you want to install all dependencies on a Debian based distribution and checkout
the source code type in the following commands:

```
$ sudo apt-get install build-essential git bison flex
$ git clone --recursive https://github.com/20centaurifux/efind.git
```

On other distributions the required packages may have different names.

If your system is prepared you can compile and install **efind**:

```
$ cd efind
$ make && sudo make install
```

## Planned features

* scripting support (e.g. Python) for custom functions
* extension blacklist (to avoid naming clashes with globally installed extensions)
* optional caching of find results
* sorting support
* support for grouping results
