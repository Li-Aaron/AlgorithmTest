#include "sort.h"

void SortInsert(FLT64 a[], INT32 n)
{
	FLT64 target;
	INT32 j;
	for (INT32 i = 1; i < n; i++){
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