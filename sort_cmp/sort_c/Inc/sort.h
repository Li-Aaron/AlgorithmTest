#ifndef SORT_H
#define SORT_H

#include <stdio.h>
#include <math.h>

#include "typedef.h"

#define EXPORT __declspec(dllexport)

extern BOOLEAN compare(FLT64 a, FLT64 b);

EXPORT void SortBubble(FLT64 a[], INT32 n);
EXPORT void SortInsert(FLT64 a[], INT32 n);
EXPORT void SortQuick(FLT64 a[], INT32 n);
EXPORT void SortQuick2(FLT64 a[], INT32 n);

#endif