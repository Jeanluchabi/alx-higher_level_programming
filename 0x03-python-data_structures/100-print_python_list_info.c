#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int x;
	PyListObject *ob = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", ob->allocated);
	for (x = 0; x < size; x++)
		printf("Element %x: %s\n", x, Py_TYPE(ob->ob_item[x]->tp_name);
}
