from PIL import Image

filepath = 'D:\\Code_python\\SVM\\pick_pictures\\'
outpath = 'D:\\Code_python\\SVM\\new_pics\\'
each_number = 35
for i in range(3):
    for j in range(each_number):
        infile_name = filepath+str(i) + '_' + str(j)+ '.jpg'
        outfile_name = outpath + str(i) + '_' + str(j)+ '.jpg'
        pil_im = Image.open(infile_name)
        out = pil_im.resize((92, 112))
        out.save(outfile_name)
print 'done!'
