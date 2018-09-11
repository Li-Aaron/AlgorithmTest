#include "sort.h"

// compare condition (important)
BOOLEAN compare(FLT64 a, FLT64 b)
{
	return a <= b;
}

inline void swap(FLT64 a[], INT32 x, INT32 y)
{
	FLT64 tmp = a[x];
	a[x] = a[y];
	a[y] = tmp;
}