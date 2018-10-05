from PIL import Image

filepath = 'D:\\Code_python\\SVM\\Pictures\\' #输入文件路径
outpath = 'D:\\Code_python\\SVM\\new_pics\\'  #输出图片储存路径
each_number = 35  #每种图片提取数量
for i in range(3): #三种图片依次提取35张
    for j in range(each_number):

        infile_name = filepath+str(i) + '_' + str(j)+ '.jpg' #输入图片的名称;储存路径+种类+下划线+序号+图像格式
        outfile_name = outpath + str(i) + '_' + str(j)+ '.jpg'#输出文件的名称；输出路径+种类+种类+下划线+序号+图像格式
        pil_im = Image.open(infile_name)#打开图片
        out = pil_im.resize((92, 112))#重置大小
        out.save(outfile_name)#储存
print 'done!'
