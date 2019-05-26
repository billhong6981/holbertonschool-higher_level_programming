#include <Python.h>
#include <object.h>
#include <bytesobject.h>
#include <listobject.h>
#include <unicodeobject.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_string - a function prints unicode string
 * @p: python object pointer
 * Return: void
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len = 0;
	char *str = NULL;

	printf("[.] string object info\n");
	if(!PyUnicode_CheckExact(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		fflush(stdout);
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		str = "compact ascii";
	else
		str = "compact unicode object";
	len = PyUnicode_GET_SIZE(p);
	printf("  type: %s\n", str);
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
	fflush(stdout);
}
