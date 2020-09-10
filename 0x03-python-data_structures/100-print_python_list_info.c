#include <stdlib.h>
#include <Python.h">
void print_python_list_info(PyObject *p)
{
    unsigned int i = 0;
    printf("[*] Size of the Python List = %ld", pyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject*)(p))->allocated);
    for(i = 0; i < PySize; i++)
    {
        printf("Element %i: %s\n", i, (PyType(PyList_Getitem(p, i))->tp_name));
    }
}