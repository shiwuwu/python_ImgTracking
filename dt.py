import cv2
import pytesseract as pytesseract


def get_words(bean,image):
    GaussianBlur = int(bean.GaussianKernelforword)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(GaussianBlur,GaussianBlur),0)

    canny = cv2.Canny(gray,250,250,255)
    dilate = int(bean.MorphClose)
    canny = cv2.dilate(canny,None,iterations=dilate,borderValue=3)

    return canny


def get_current_words(self,cnt,image,LOG):

    """
    使用ocr进行识别
    :param cnt: 处理后的识别域中图片
    :param image: 识别的图片
    :param LOG: 日志
    :return:
    """
    LOG.info('[get_current_words] start work')
    # 得到识别域中的一个对象轮廓
    (x,y,w,h) = cv2.boundingRect(cnt)
    # 截取图片
    crop_img = image[y:y+h,x:x+w]
    # 将图片放大两倍
    crop_img = cv2.resize(crop_img,(0,0),fx=2,fy=2)
    # 调用ocr进行识别
    pytesseract.pytesseract.tesseract_cmd = self.bean.ocr_path
    current_num = pytesseract.image_to_string(crop_img,'chi_sim')

    LOG.info(f"[get_current_words]current=={current_num}")


    LOG.info('[match_img] start work')
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # 使用matchTemplate对原始灰度图片和图像模板进行匹配



