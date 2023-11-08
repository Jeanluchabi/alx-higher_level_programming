#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This function prints bytes information 
 *
 * @p: the object of python
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, n, lmt;

	print("[.] bytes object info\n");

	if (!PyBytes_check(p))
	{
		pritn(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	siz = ((PyVarObject *)(p)P->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;


	print(" size: %ld\n", size);
	print(" trying string: %s\n", str;
	
	if (size >= 10)
	         lmt = 10;
	else
	         lmt = size + 1;

	print(" first %ld bytes:", lmt);

	for (n = 0; n < lmt; n++)
	if (str[x] >= 0)
	       print(" %02x", str[n]);
	       else
	              print(" %02x", 256 + str[n]);
	print("\n")
}

/**
 * print_python_list - thes function prints list information
 * @p: the object of python
 */

void print_python_list(PyObject *p)
{
	long int size, n;
	PyListObjext *list;
	PyObject *ob;

	size = ((PyVarObject *)(p))-ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	print("[*] Alocated = %ld\n", list->allocated);

	for (n = 0; n < size; n++)
	{
		ob = ((PyListObject *)p)->ob_item[n];
		print("Elemt %ld: %s\n", n, ((obj)->ob_type)->tp_name);
		if (PyBytes_check(ob))
			print_python_bytes(ob)
	}
}
