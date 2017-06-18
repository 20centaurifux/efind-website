# How to write extensions

In this tutorial we're going to write a custom function to test file extensions of found files:

```
int check_extension(extension, icase) # pseudo code
```

The first parameter (*extension*) is a string that specifies the extension we're looking for. The second one (*icase*) is a number which allows us to enable case insensitive string comparison.

## Writing extensions in C

To make all required types and function prototypes available include the [extension-interface.h](https://github.com/20centaurifux/efind/blob/master/extension-interface.h) header into your source file. In this tutorial we create a file named *c-example.c*:

```
$ mkdir c-example && cd ./c-example
$ wget https://raw.githubusercontent.com/20centaurifux/efind/master/extension-interface.h
$ echo '#include "extension-interface.h"' > c-example.c
```

At first you should implement the *registration* function to make your extension available. Please specify name, version and a brief description by calling the given registration callback:

```
void
registration(RegistrationCtx *ctx, RegisterExtension fn)
{
	fn(ctx, "example extension", "0.1.0", "An example extension written in C.");
}
```

The *discover* function exports the functions provided by our extension. Please specify name, number of parameters and parameter types.  Parameters can be strings or integers.

```
void
discover(RegistrationCtx *ctx, RegisterCallback fn)
{
	fn(ctx, "c_check_extension", 2, CALLBACK_ARG_TYPE_STRING, CALLBACK_ARG_TYPE_INTEGER);
}
```

In the example above a function named *c_check_extension* is exported. It has two parameters: a string and an integer.

Now we implement the function:

```
int
c_check_extension(const char *filename, int argc, void *argv[])
{
	const char *offset;
	int result = 0;

	/* find extension */
	if((offset = strrchr(filename, '.')))
	{
		/* first argument: extension to test */
		char *extension = argv[0];

		/* second argument: compare mode */
		int icase = *((int *)argv[1]);

		if(extension && strlen(offset) == strlen(extension))
		{
			result = 1;

			while(*offset && result)
			{
				if(icase)
				{
					result = tolower(*offset) == tolower(*extension);
				}
				else
				{
					result = *offset == *extension;
				}

				++offset, ++extension;
			}
		}
	}

	return result;
}
```

The first parameter is always the name of the found file. *argc* specifies the number function arguments provided by the array *argv*. Please keep in mind that you receive a *pointer* to an integer, not the integer value.

Build the source file into a shared library and copy it into your local extension directory:

```
$ gcc -Wall -O2 -fPIC -nostartfiles -shared ./c-example.c -o ./c-example.so
$ mkdir -p ~/.efind/extensions
$ cp ./c-example.so ~/.efind/extensions
```

Now you can use the function in **efind**:

```
$ efind . 'c_check_extension(".c", 1)'
```

You find this example in the [examples](https://github.com/20centaurifux/efind/tree/master/examples/c) folder.

## Writing extensions in Python 2

**efind** can load custom functions from Python scripts. Please consider that your script is imported by its module name and not by filename. As a consequence the import may fail if there's a shared library having the same name as your script in one of the extension folders.

Your script has to define the strings *EXTENSION_NAME*, *EXTENSION_VERSION* and *EXTENSION_DESCRIPTION* to export name, version and a brief description:

```
EXTENSION_NAME="example extension"
EXTENSION_VERSION="0.1.0"
EXTENSION_DESCRIPTION="An example extension written in Python."
```

In our example we want to write a function to test the extension of a filename. It could be implemented the following way:

```
def py_check_extension(filename, extension, icase):
    result = 0

    _, ext = os.path.splitext(filename)

    if len(ext) > 0:
        if icase == 0:
            result = ext == extension
        else:
            result = ext.lower() == extension.lower()

    return result
```

The first parameter is always the name of the found file. Our example function has two optional arguments. To register the function properly the data types of these arguments have to be declared by adding a *\_\_signature\_\_* attribute to your *callable*:

```
py_check_extension.__signature__=[str, int]
```

The *EXTENSION_EXPORT* array exports your custom function(s) to **efind**:

```
EXTENSION_EXPORT=[py_check_extension]
```

After copying your script into your local extension folder (*~/.efind/extensions*) your custom function is available in **efind**:

```
$ efind . 'py_check_extension(".py", 1)'
```

You find this example in the [examples](https://github.com/20centaurifux/efind/tree/master/examples/python) folder.
