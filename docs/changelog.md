## 2017-12-23 - version 0.4.0 (Magellan)

* FEATURE: support multiple starting points/search paths
* FEATURE: allow user-friendly field names in expressions and sort strings (e.g. "%{path}" instead of "%p")
* FEATURE: new test suite
* CHANGE: search extensions in /usr/lib/efind instead of /etc/efind
* CHANGE: renamed --list-extensions option to --print-extensions
* CHANGE: renamed --show-blacklist option to --print-blacklist
* CHANGE: don't abort import of extensions if a single import fails
* CHANGE: enable colored log messages by default
* CHANGE: the fields %a, %c and %t print the timestamp in seconds
* FIX: recognize regex and iregex attributes
* FIX: allow filter functions as first function argument (e.g. "foo(bar(1, 2), 3)")
* FIX: always return error code if "find" child process fails
* FIX: integer overflow on x86 when calculating sparseness of files greater than 2G

## 2017-10-31 - version 0.3.1

* FEATURE: not-operator
* FEATURE: search additional extensions in directories specified in EFIND\_EXTENSION\_PATH variable

## 2017-08-15 - version 0.3.0 (Leif Erikson)

* FEATURE: --order-by option
* FEATURE: GNU gettext support
* FEATURE: German translation

## 2017-07-16 - version 0.2.2

* FEATURE: --show-blacklist option to print blacklisted extensions
* CHANGE: replaced libavcall with libffi

## 2017-07-04 - version 0.2.1

* FEATURE: --log-level option to enable logging with different verbosities
* FEATURE: --enable-log-color option to print colored log messages
* FEATURE: "empty" flag to test if a regular file or directory is empty
* FEATURE: "filesystem" property to test the filesystem a file is on
* CHANGE: renamed --maxdepth option to --max-depth
* FIX: initialize all getline() parameters properly when reading from standard input

## 2017-06-24 - version 0.2.0 (Jean Malaurie)

* FEATURE: Python 2 support for extensions
* FEATURE: regular expression support (regex & iregex attribute)
* FEATURE: added --printf option
* FEATURE: increased maximum allowed expression length

## 2017-05-13 - version 0.1.1

* FEATURE: blacklist support (make it possible to exclude extensions from being loaded)
* FIX: don't import same module twice

## 2017-05-06 - version 0.1.0 (Belzoni)
* first release
