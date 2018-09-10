#include "sort.h"

// fast sort partion
INT32 _SortPartion(FLT64 a[], INT32 left, INT32 right, BOOLEAN cmp(FLT64, FLT64))
{
	FLT64 pivot = a[left];
	INT32 pivot_idx = left;
	FLT64 tmp;

	while (left < right){
		// find left > pivot and right < pivot
		while (left < right && cmp(pivot, a[right])){
			right--;
		}
		while (left < right && cmp(a[left], pivot)){
			left++;
		}
		// swap these two
		tmp = a[right];
		a[right] = a[left];
		a[left] = tmp;
	}
	// swap pivot(left) to 'middle'
	tmp = a[pivot_idx];
	a[pivot_idx] = a[left];
	a[left] = tmp;
	return left; // to be new pivot
}

// quick sort
void _SortQuick(FLT64 a[], INT32 left, INT32 right, BOOLEAN cmp(FLT64, FLT64))
{
	// terminate condition
	if (left >= right){
		return;
	}

	INT32 pivot_idx = _SortPartion(a, left, right, cmp);
	// recursion
	_SortQuick(a, left, pivot_idx - 1, cmp);
	_SortQuick(a, pivot_idx + 1, right, cmp);
}

// fast sort
void SortQuick(FLT64 a[], INT32 n)
{
	_SortQuick(a, 0, n - 1, compare);
}