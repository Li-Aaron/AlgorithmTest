#include <sort.h>

#define LEN 9

INT32 main(){
	FLT64 a[LEN] = { 1.1,3.5,2.8,9.5,4.3,6.4,3.5,7.9,2.6 };
	INT32 i;
	for (i = 0; i < LEN; i++) {
		printf("%0.2f, ", a[i]);
	}
	printf("\n");

	SortMerge(a, LEN);
	for (i = 0; i < LEN; i++) {
		printf("%0.2f, ", a[i]);
	}
	printf("\n");
	system("pause");
	
}

