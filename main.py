import cv2

# 使用opencv按一定间隔截取视频帧，并保存为图片

video_data = cv2.VideoCapture('./1.mp4')  # 读取视频文件
c = 0
print("------------")
if video_data.isOpened():  # 判断是否正常打开
    print("yes")
    rval, frame = video_data.read()
else:
    rval = False
    print("false")

time_frame = config_json['frame'] # 视频帧计数间隔频率
try:
    while rval:  # 循环读取视频帧
        rval,frame = video_data.read()
        print(c,time_frame,c%time_frame)
        if (c % time_frame == 0):# 每隔time_frame帧进行存储操作
            print("write...")
            cv2.imwrite('./jpg/' + str(c)+ '.jpg', frame)  # 存储为图像
            print("success!")
        c = c + 100000
    cv2.waitKey(1)
    video_data.release()
except:
    pass
print("完成")
print("==================================")