#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - A function to print basic information about
 * a Python list
 * @p: PyObject representing a Python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, x;
	PyObject *piece;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocatted = %ld\n", allocated);

	for (x = 0; x < size; ++x)
	{
		piece = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPe(piece)->to_name);
	}
}
