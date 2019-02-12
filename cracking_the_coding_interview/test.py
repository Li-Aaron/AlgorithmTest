A = [1, 21, 24, 100]
B = [9, 29, 70]

tmp = -1
for a in A:
  for b in B:
    if abs(a-b) < tmp or tmp == -1:
      tmp = abs(a-b)
print (tmp)

print(min([min([abs(a-b) for a in A]) for b in B]))
