#include <Python.h>

/**
 * print_python_list_info - Print basic information.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int sizz;
	int T = 0;
	int ALLOC;
	PyObject *obj;

	sizz = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sizz);
	printf("[*] Allocated = %d\n", ALLOC);

	for (; T < sizz; T++)
	{
		printf("Element %d: ", T);

		obj = PyList_GetItem(p, T);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
