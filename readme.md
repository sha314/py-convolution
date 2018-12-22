# SWIG, Numpy, C++ 

https://docs.scipy.org/doc/numpy-1.13.0/reference/swig.interface-file.html

https://scipy-cookbook.readthedocs.io/items/SWIG_NumPy_examples.html

https://stackoverflow.com/questions/16377503/use-swig-to-wrap-c-vector-as-python-numpy-array

https://scipy-cookbook.readthedocs.io/items/SWIG_Memory_Deallocation.html


# numpy.i
https://github.com/numpy/numpy


# Pointer
if pointer or reference for an array is needed use naked array.

arr must be a naked array. otherwise error occurs. 
	reason -> python internally tries to free up memories



use of vector and then converting it to a pointer by taing the address of the
first element for return value leads to error since python also tries to 
free up memories that are already freed by vector. solution : use naked array
in such case.

# module name
changed to "statmechtools" for statistical mechanics tools

# Docstring is included
http://www.swig.org/Doc2.0/Python.html#Python_nn65


# Install python modules to the system
https://www.osc.edu/resources/getting_started/howto/howto_install_your_own_python_modules
