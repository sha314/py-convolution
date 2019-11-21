
//Word.h


#ifndef __HEADER_MYARRAY_H_
#define __HEADER_MYARRAY_H_

// for 1d array
void convolve1d(
    double *data, int columns,
    int thread_count,
    double **data_out, int *dim_out);

// for 2d array
void convolve2d(
	double *data_in, int n_rows, int n_columns,
	int thread_count,
	double **data_out, int *dim1_out, int *dim2_out);


// for 1d array
void convolve1d_fast(
    double *data, int columns,
    int thread_count,
    double **data_out, int *dim_out, double threshold=1e-15);

// for 2d array
void convolve2d_fast(
	double *data_in, int n_rows, int n_columns,
	int thread_count,
	double **data_out, int *dim1_out, int *dim2_out, double threshold=1e-15);


#endif // WORD_H_ 