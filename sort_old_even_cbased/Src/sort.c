#include "sort.h"

/*********************
*     function 1     *
**********************/
// put *podd before peven, other move right one pos
void swap(int *podd, int *peven)
{
	int tmp = *podd;
	while (podd > peven)
	{
		*podd = *(podd - 1);
		podd--;
	}
	*podd = tmp;
}

// function using pointers (not a good way)
void sort_odd_even(int a[], int n)
{
	int *podd = a;
	int *peven = a;
	// locate peven to first even number
	while ((*peven & 1) != 0 && peven < a + n){
		peven++;
	}
	while (1)
	{
		// locate podd to first odd number after peven
		while (((*podd & 1) == 0 || podd <= peven) && podd < a + n){
			podd++;
		}
		// terminate condition
		if (podd >= a + n){
			break;
		}
		swap(podd, peven);
		// peven directly to next value 1[2]4 5 6 -> 1 5[2]4 6
		peven++;
	}
}

/*********************
*     function 2     *
**********************/
// compare condition (important)
int compare(int a, int b)
{
	if ((a & 1) == (b & 1)){
		return (a <= b); // same parity, little first
	}
	else {
		return ((a & 1) > (b & 1)); // different parity, odd first
	}
}

// insert sort
void sort_odd_even_insert(int a[], int n)
{
	int target, j;
	for (int i = 1; i < n; i++){
		target = a[i];
		j = i;
		// using compare instead of a <= b
		while (j>0 && compare(target, a[j - 1])){
			a[j] = a[j - 1];
			j--;
		}
		a[j] = target;
	}
}

// fast sort partion
int sort_partion(int a[], int left, int right, int cmp(int, int))
{
	int pivot = a[left];
	int pivot_idx = left;
	int tmp;

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

// fast sort
void sort_fast(int a[], int left, int right, int cmp(int, int))
{
	// terminate condition
	if (left >= right){
		return;
	}

	int pivot_idx = sort_partion(a, left, right, cmp);
	// recursion
	sort_fast(a, left, pivot_idx - 1, cmp);
	sort_fast(a, pivot_idx + 1, right, cmp);
}

// fast sort
void sort_odd_even_fast(int a[], int n)
{
	sort_fast(a, 0, n - 1, compare);
}

