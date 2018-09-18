#include "sort.h"

void _ShiftDown(FLT64 a[], INT32 parent, INT32 boundary, BOOLEAN cmp(FLT64, FLT64))
{
  // index start with 0
  INT32 child1 = parent * 2 + 1;
  INT32 child2 = parent * 2 + 2;
  INT32 child_large;
  // both 2 values in boundary
  if (child2 <= boundary){
    if (cmp(a[parent], a[child1]) || cmp(a[parent], a[child2]))
    {
      // find larger child
      child_large = cmp(a[child1], a[child2])? child2 : child1;
      if (cmp(a[parent], a[child_large])){
        swap(a, parent, child_large);
      }
    }
  } else if (child1 <= boundary) {
    // only 1 value in boundary
    if (cmp(a[parent], a[child1])){
        swap(a, parent, child1);
    }
  }
}

// build big root heap
void _BuildHeap(FLT64 a[], INT32 start, INT32 stop, BOOLEAN cmp(FLT64, FLT64))
{
  INT32 parent;
  for (parent = stop/2; parent > start - 1; parent--){
    _ShiftDown(a, parent, stop, cmp);
  }
}

// heap sort
void SortHeap(FLT64 a[], INT32 n)
{
  INT32 stop;
  for (stop = n-1; stop > 0; stop--){
    // Building Big Root Heap
    _BuildHeap(a, 0, stop, compare);
    // Make First Node Down
    swap(a, 0, stop);
  }
}