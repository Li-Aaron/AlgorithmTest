#include "sort.h"

void _Merge(FLT64 a[], INT32 left, INT32 middle, INT32 right, BOOLEAN cmp(FLT64, FLT64))
{
  INT32 idx = 0;
  INT32 idxL = left;
  INT32 idxR = middle;
  INT32 len = right - left;
  
  // generate a memory space for merge
  FLT64 *a_temp;
  if (NULL == (a_temp = (FLT64*)malloc(len * sizeof(FLT64))))
  {
    perror("error...");
    exit(1);
  }
  memset(a_temp, 0, len * sizeof(FLT64));

  // main process of merge
  while (idxL < middle && idxR < right){
    // left < right then append left
    // right < left then append right
    if (cmp(a[idxL], a[idxR])){
      a_temp[idx] = a[idxL];
      idxL++;
    } else {
      a_temp[idx] = a[idxR];
      idxR++;
    }
    idx++;
  }

  // padding the rest part
  if (idxL < middle){
    memcpy(&a_temp[idx], &a[idxL], (middle - idxL)*sizeof(FLT64));
  } else if (idxR < right){
    memcpy(&a_temp[idx], &a[idxR], (right - idxR)*sizeof(FLT64));
  }

  // re copy to input array and free memory space
  memcpy(&a[left], &a_temp[0], len*sizeof(FLT64));
  free(a_temp);
}

void _SortMerge(FLT64 a[], INT32 left, INT32 right, BOOLEAN cmp(FLT64, FLT64))
{
  if (right - left <= 1){
    // Terminate Condition
    // if right - left <= 0, when right - left = 1, the
    // middle will always be left
    return;
  }

  INT32 middle = (left + right) / 2;
  _SortMerge(a, left, middle, cmp);
  _SortMerge(a, middle, right, cmp);
  _Merge(a, left, middle, right, cmp);
}


void SortMerge(FLT64 a[], INT32 n)
{
  _SortMerge(a, 0, n, compare);
}