# Building efind from source

**efind** uses [GNU Make](https://www.gnu.org/software/make/) as build system.
Installation options can be customized in the Makefile.

Please ensure that [GNU Bison](https://www.gnu.org/software/bison/),
[GNU Flex](https://www.gnu.org/software/flex/), [Python 2.7](https://www.python.org/)
and [libffi](https://sourceware.org/libffi/) are installed on your
system before you build **efind**.

If you want to install all dependencies on a Debian based distribution and checkout
the source code type in the following commands:

```
$ sudo apt-get install build-essential git pkg-config gettext \
  bison flex libpython2.7-dev libffi-dev
$ git clone --recursive https://github.com/20centaurifux/efind.git
```

On other distributions the required packages may have different names.

If your system is prepared you can compile and install **efind**:

```
$ cd efind
$ make && sudo make install
```

Change file locations and build tools by setting the desired variables before
running make:

```
$ CC=clang LIBDIR=/usr/lib make && sudo make install
```
