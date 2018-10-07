# encoding:utf-8

from __future__ import print_function
from PIL import Image
from numpy import *
import numpy as np

def ImageToMatrix(filename):
    # 读取图片
    im = Image.open(filename)
    im = im.convert("L")
    data = im.getdata()
    data = np.matrix(data,dtype="float")/255
    data = data.tolist()
    return data
filepath = 'D:\\Code_python\\SVM\\new_pics\\'
savepath = "D:\\Code_python\\SVM\\pic_matrix\\"
picsize = 92*112
picnum = 2*34  #在这里你取出来了两类，没敢做三分类，为了简单，你试了试二分类。一类是-1，一类是1，每类取出来34张图片，
data_all = np.zeros(shape=(picsize,picnum))
n = 0
for j in range(34):
    for i in range(2):
        filename =  filepath + str(i) + "_" + str(j) +".jpg"
        data = ImageToMatrix(filename)
        data_single = []
        for k in range(len(data)):
            data_single.append(data[k])
        data_all[:,n] = list(data[0])
        n = n+1
#print data_all
path = 'D:\\Code_python\\SVM\\pic_matrix\\pic_matrix.txt'   #你将所有图片读入的矩阵放在了这里
np.savetxt(path, data_all)

traindata = data_all[:,0:34]
testdata = data_all[:,34:68]

dp = [-1,1] * 17   #在这里你取出来了两类，没敢做三分类，为了简单，你试了试二分类。一类是-1，一类是1，每类的训练集取出来17张图片，测试集17张，这里的dp是训练集老师
trainNum=len(dp)
sigma=0.5
kMatrix = np.zeros((34,34))
Multimatrix = np.zeros((34,34))
for i in range(34):
    for j in range(34):

        a = np.array(traindata[:, i] - traindata[:, j]) ** 2 #  高斯核函数：讲每一列的数据循环减去所有列，得到的数值平方再相加

        kMatrix[i, j] = exp(-(sum(list(a))) / (2*sigma**2))  # 加到的和除以方差的平方，再除以2，得到的值作为指数函数的系数。
        print ("kMtrix",kMatrix[i,j])
        Multimatrix[i,j] = dp[i]*dp[j]*kMatrix[i,j]

inverse_Multimatrix = mat(Multimatrix).I     #这一步就是矩阵求逆！mat函数将数组转换成矩阵，小数点加上I是矩阵求逆。
print(inverse_Multimatrix)
e = mat(np.ones((1, trainNum)))
alpha =inverse_Multimatrix * e.T    #这里报错的原因是你的矩阵不可逆，也就求不出来alpha，之前咱们求出来了alpha是1，但是我想这可能是因为上次正好很特殊每类取了10张图，矩阵不可逆是因为这个矩阵的行列式为0，下面报错的singular matrix也是这个意思
print("alpha",alpha)

#注意注意，这是你的测试代码，你做了1-6步，你将两类的图片，每类读了34张，一半训练，一半测试，产生出来alpha了，他们肯定问，你C明明是3分类，怎么现在变成了2分类，你说我就是试试，3分类更加简单。