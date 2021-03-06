# Home

## Overview

**efind** (extendable find) searches for files in a directory hierarchy.

Basically it's a wrapper for [GNU find](https://www.gnu.org/software/findutils/)
providing an easier and more intuitive expression syntax. It can be extended
by custom functions to filter search results. Furthermore, it has built-in
sort and range functionality.

Watch this screencast to get a brief overview:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ayrJS86nr4o" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Usage

Running **efind** without any argument the search expression is read from
*standard input (stdin)* and files are searched in the user's home directory.
A different directory and expression can be specified with the *--dir*
and *--expr* options:

	$ efind --dir=/tmp --expr="size>1M and type=file"

**efind** tries to handle the first arguments as path(s) and expression. It's
valid to run **efind** the following way:

	$ efind ~/git ~/code "type=file and name='CHANGELOG'"

**efind** is shipped with a manpage, of course.

	$ man efind

## Examples

Print five largest files.

	efind . "type=file" \
	        --order-by "-{bytes}" \
	        --printf " %-10{kb} | %{path}\n" \
	        --limit 5

Find first text document containing a string and stop immediately.

	efind . "name='*.txt' and text_contains('find me')" --limit 1

Filter audio files by artist and convert them to WAV:

	efind ~/Music \
	      "extension_in('.mp3, .ogg') and artist_matches('David Bowie')" \
	      --exec sox "%{filename}" tmp/"%{name}.wav" \;

## Expression Syntax

A search expression consists of at least one comparison or file flag to test. Multiple
expressions can be evaluated by using conditional operators:

| Operator | Description                                                                                                                                                   |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| and      | If an expression returns logical false it returns that value and doesn't evaluate the next expression. Otherwise it returns the value of the last expression. |
| or       | If an expression returns logical true it returns that value and doesn't evaluate the next expression. Otherwise it returns the value of the last expression.  |

Expressions are evaluated from left to right. Use parentheses to force precedence.

The following operators can be used to compare a file attribute to a value:

| Operator                 | Description      |
| :----------------------- | :--------------- |
| =, equal, equals         | equals to        |
| >, greater than, greater | greater than     |
| >=, at least             | greater or equal |
| <, less than, less       | less than        |
| <=, at most              | less or equal    |

A value must be of one of the data types listed below:

| Type          | Description                                                                                                            |
| :------------ | :--------------------------------------------------------------------------------------------------------------------- |
| string        | Quoted sequence of characters.                                                                                         |
| number        | Whole number.                                                                                                          |
| time interval | Time interval (number) with suffix. Supported suffixes are "minute(s)", "hour(s)" and "day(s)".                        |
| file size     | Units of space (number) with suffix. Supported suffixes are "byte(s)", "kilobyte(s)", "megabyte(s)" and "gigabyte(s)". |
| file type     | "file", "directory", "block", "character", "pipe", "link" or "socket".                                                 |

The following file attributes are searchable:

| Attribute  | Description                           | Type            | Example     |
| :--------- | :------------------------------------ | :-------------- | :---------- |
| name       | case sensitive filename pattern       | string          | "*.txt"     |
| iname      | case insensitive filename pattern     | string          | "Foo.bar"   |
| regex      | case sensitive regular expression     | string          | ".*\\.html" |
| iregex     | case insensitive regular expression   | string          | ".*\\.TxT"  |
| atime      | last access time                      | time interval   | 1 minute    |
| ctime      | last file status change               | time interval   | 15 hours    |
| mtime      | last modification time                | time interval   | 30 days     |
| size       | file size                             | size            | 10 megabyte |
| group      | name of the group owning the file     | string          | "users"     |
| gid        | id of the group owning the file       | number          | 1000        |
| user       | name of the user owning the file      | string          | "john"      |
| uid        | id of the user owning the file        | number          | 1000        |
| type       | file type                             | file type       | pipe        |
| filesystem | name of the filesystem the file is on | string          | "ext4"      |

Additionally you can test these flags:

| Flag       | Description                                                   |
| :--------- | :------------------------------------------------------------ |
| readable   | the file can be read by the user                              |
| writable   | the user can write to the file                                |
| executable | the user is allowed to execute the file                       |
| empty      | the file is empty and is either a regular file or a directory |

## Differences to GNU find

Sometimes GNU find doesn't behave in a way an average user would expect. The following
expression finds all documents in the current folder with a file size less or equal than
1G because every file with at least one byte is rounded up:

	$ find . -size 1G

**efind** converts file sizes to byte to avoid this confusing behaviour:

	$ efind . "size=1G" --print
	$ find . -size 1073741824c

**efind's** *--printf* option is not fully compatible with GNU find:

* In contrast to GNU find numeric values like file size or group id are *not* converted
  to string. This means that all number related flags work with **efind**.
* Width and precision are interpreted exactly the same way as the printf C function does.
* The fields %a, %c and %t print the timestamp in seconds.
* Date format strings are not limited to a single field. The string "%AHMS" prints hour,
  minute and second of the last file access, for example.
* **efind's** printf format supports user-friendly field names like "{path}" or "{group}".
* When printing an undefined escape sequence (e.g. "\P") only the character following the
  backslash is printed.

## Getting efind

You can [build](/howto-build) **efind** from source code or [download](/downloads)
a package for your distribution. If you should miss a package type or if you want to
support **efind** don't hesitate to [contact](/contact) me. Any help is
much appreciated :)
