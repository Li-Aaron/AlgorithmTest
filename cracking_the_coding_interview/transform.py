'''
有一副由NxN矩阵表示的图像，这里每个像素用一个int表示，请编写一个算法，在不占用额外内存空间的情况下(即不使用缓存矩阵)，将图像顺时针旋转90度。

给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵,保证N小于等于500，图像元素小于等于256。
'''


class Transform:
  def transformImage(self, mat, n):
    # write code here
    return list(zip(*mat[::-1]))

#testcase
mat = [[1,2,3],[4,5,6],[7,8,9]]
n = 3
print(Transform().transformImage(mat, n) == [[7,4,1],[8,5,2],[9,6,3]])