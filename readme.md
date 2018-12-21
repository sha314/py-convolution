# SWIG, Numpy, C++ 

https://docs.scipy.org/doc/numpy-1.13.0/reference/swig.interface-file.html

https://scipy-cookbook.readthedocs.io/items/SWIG_NumPy_examples.html

https://stackoverflow.com/questions/16377503/use-swig-to-wrap-c-vector-as-python-numpy-array

https://scipy-cookbook.readthedocs.io/items/SWIG_Memory_Deallocation.html


# Pointer
if pointer or reference for an array is needed use naked array.

arr must be a naked array. otherwise error occurs. 
	reason -> python internally tries to free up memories
