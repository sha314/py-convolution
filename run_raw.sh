# build.sh

# generating wrapping source files
echo generating wrapping source files ..............
swig -python -c++ convolution.i

# compiling
echo compiling......................................
# g++ -fPIC -c -std=c++11 convolution.cpp convolution_wrap.cxx  -I/usr/include/python3.6m -I/home/shahnoor/.local/lib/python3.6/site-packages/numpy/core/include/
g++ -fPIC -c -std=c++11 -O3 -fopenmp src/convolution.cpp convolution_wrap.cxx  -I/usr/include/python3.6m -I/home/shahnoor/.local/lib/python3.6/site-packages/numpy/core/include/

# or
#-I/home/shahnoor/software/anaconda3/include/python3.7m/

# linking
echo linking .........................................
# -o modulename.so
g++ -O3 -fopenmp -shared  convolution.o convolution_wrap.o -o _statmechtools.so -lstdc++


echo removing redundant files.........................
rm *_wrap*
rm *.o
