# coding:utf-8
import time

import pylab
import imageio
# 注释的代码执行一次就好，以后都会默认下载完成
# imageio.plugins.ffmpeg.download()
import skimage
import numpy as np
import os
path = os.getcwd()
# 视频的绝对路径
filename = path+'/1.mp4'
print(filename)
# 可以选择解码工具
vid = imageio.get_reader(filename, 'ffmpeg')
for im in vid:
    # image的类型是mageio.core.util.Image可用下面这一注释行转换为arrary
    print(im.mean())
    image = skimage.img_as_float(im).astype(np.float64)
    fig = pylab.figure()
    pylab.imsave(path+'/jpg/'+str(int(time.time()*1000))+'.jpg',im)
print("执行完毕")