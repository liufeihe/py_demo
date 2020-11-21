import numpy as np
import cv2


def connected_components_demo():
    src = cv2.imread("e:/ying.jpg")
    cv2.imshow("input1", src)

    src = cv2.GaussianBlur(src, (3,3), 0)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)

    output = cv2.connectedComponents(binary, connectivity=8, ltype=cv2.CV_32S)
    num_labels = output[0]
    labels = output[1]
    colors = []
    for  i in range(num_labels):
        b = np.random.randint(0, 255)
        g = np.random.randint(0, 255)
        r = np.random.randint(0, 255)
        colors.append((b, g, r))

    colors[0] = (0,0,0)
    h, w = gray.shape
    image = np.zeros((h, w, 3), dtype=np.uint8)
    for row in range(h):
        for col in range(w):
            image[row, col] = colors[labels[row, col]]

    cv2.imshow("colored label", image)
    print("total:", num_labels - 1)

    output_more = cv2.connectedComponentsWithStats(binary, connectivity=8, ltype=cv2.CV_32S)
    num_labels = output_more[0]
    labels = output_more[1]
    stats = output_more[2]
    centers = output_more[3]
    image_stats = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    for i in range(num_labels):
        cx, cy = centers[i]
        x, y, w, h, area = stats[i]
        print("area ", i, ": ", area)
        cv2.rectangle(image_stats, (x, y), (x+w, y+h), (0,0,255), 2, 8, 0)
        cv2.circle(image_stats, (np.int(cx), np.int(cy)), 3, (255,0,0), 2, 8, 0 )
    cv2.imshow("stat", image_stats)

def find_contours_demo():
    src = cv2.imread("e:/rice.jpg")
    cv2.imshow("input1", src)

    src = cv2.GaussianBlur(src, (3,3), 0)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)
    #在Opencv4.0中 cv2.findContours()的返回值以从三个变为二个
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("total number:", len(contours))

    # for i in range(len(contours)):
        # cv2.drawContours(src, contours, i, (0,0,255), 2, 8)

    for c in contours:

        x, y, w, h = cv2.boundingRect(c)

        #传入一个轮廓图像，返回 x y 是左上角的点， w和h是矩形边框的宽度和高度

        cv2.rectangle(src, (x, y), (x+w, y+h), (0, 255, 0), 2, 8, 0)
        """
        画出矩形
            img 是要画出轮廓的原图
            (x, y) 是左上角点的坐标
            (x+w, y+h) 是右下角的坐标
            0,255,0）是画线对应的rgb颜色
            2 是画出线的宽度
        """

        # 获得最小的矩形轮廓 可能带旋转角度((质心)，（长宽），角度)
        rect = cv2.minAreaRect(c)
        # print("rect:", rect[0], rect[1],rect[2])
        # 计算最小区域的坐标可获取该矩形的四个顶点坐标
        box = cv2.boxPoints(rect)
        # 坐标规范化为整数
        box = np.int0(box)
        # 画出轮廓
        cv2.drawContours(src, [box], 0, (0, 0, 255), 3)

        # 计算最小封闭圆形的中心和半径
        (x, y), radius = cv2.minEnclosingCircle(c)
        # 转换成整数
        center = (int(x), int(y))
        radius = int(radius)
        print("center: %d, %d radius:%d "%(center(0),center(1),radius))
        # 画出圆形
        img = cv2.circle(src, center, radius, (255, 0, 0), 2)

        
    cv2.imshow("contours:", src)

def measure_contours(image):
    # src = cv2.imread("e:/rice.jpg")
    src = image
    # cv2.imshow("input",src)
    src = cv2.GaussianBlur(src, (3,3), 0)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    # cv2.imshow("binary", binary)


    #结构元素(15, 15)，控制腐蚀程度
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    #erode
    dst = cv2.erode(binary, kernel)
    cv2.imshow("erode_demo", dst)

    contours, hierachy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print("total number:", len(contours))
    position = (10,50)
    text = "total number: %d" %len(contours)
    cv2.putText(
        src, #numpy array on which text is written
        text,#%(len(contours)), #text
        position, #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        1, #font size
        (209, 80, 0, 255), #font color
        3) #font stroke

    for i in range(len(contours)):

        area = cv2.contourArea(contours[i])
        arclen = cv2.arcLength(contours[i], True)
        x, y, w, h = cv2.boundingRect(contours[i])
        print("x: %d, y: %d, area: %d, arclen: %d"%(x,y,area,arclen))
        if area > 2020 or arclen <20 :
            continue
        # ration = 0.1 #np.minimum(w,h) / np.maximum(w,h)
        # if ration < 0.8:
        cv2.drawContours(src, contours, i, (0,255,0), 2, 8)    

    # for c in contours :

    #     area = cv2.contourArea(c)
    #     arclen = cv2.arcLength(c, True)
    #     x, y, w, h = cv2.boundingRect(c)
    #     print("area: %d, arclen: %d"%(area,arclen))
    #     cv2.drawContours(src, c, -1, (0,0,255), 2, 8)

    cv2.imshow("contours-demo:", src)


def face_detect_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #CascadeClassifier
    face_detector = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")
    #detectMultiScale 在多个尺度空间查找，检测不出人脸就设置小一些
    faces = face_detector.detectMultiScale(gray, 1.1, 2)

    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2, 8, 0)
    cv2.imshow("result", image)

def line_detection(image):
    #转化灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #canny边缘检测apertureSize是sobel算子大小，只能为1,3,5􀒅7
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    #cv2.HoughLines函数输出[float, float]形式ndarray
    # 其中每个值表示检测到的线(ρ , θ)中浮点参数
    #函数将通过步长为1的半径和步长为π/180的角度来搜索所有可能的直线
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    for line in lines:
        print(type(lines)) #多维数组
        rho, theta = line[0] #获取ρ，θ
        a = np.cos(theta) #获取cos
        b = np.sin(theta) #获取sin
        x0 = a * rho #
        y0 = b * rho
        #求直线4点
        x1 = int(x0+1000*(-b)) #直线最大值x1
        y1 = int(y0+1000*(a)) #直线最大值y1
        x2 = int(x0-1000*(-b)) #直线最小值x2
        y2 = int(y0-1000*(a)) #直线最小值y2 *1000是内部规则
        #绘制线到原图上
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("image-lines", image)

def line_detect_possible_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    #HoughLinesP 函数的返回值就是直线的起点和终点
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)
    for line in lines:
        print(type(line))#多维数组
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("line_detect_possible_demo", image)

def detect_circles_demo(image):
    # 高斯双边模糊，不好调节，霍夫噪声敏感，先消除噪声
    # dst = cv2.bilateralFilter(image, 0, 150, 5)
    # 使用高斯模糊，修改卷积核ksize也可以检测出
    #dst = cv2.GaussianBlur(image, (13, 15), 15)
    # 均值迁移，EPT边缘保留滤波，霍夫噪声敏感，先消除噪声

    dst = cv2.pyrMeanShiftFiltering(image, 1, 10)

    cimage = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    # cimage1 = cv2.fastNlMeansDenoising(cimage, None, 5, 10, 10)

    #cv2.HOUGH_GRADIENT 基于比例/去重复，梯度,点数
    circles = cv2.HoughCircles(cimage, cv2.HOUGH_GRADIENT, 1, 30, param1=100, param2=35, minRadius=5, maxRadius=50)

    if circles is not None:
            # around四舍五入
        circles = np.uint16(np.around(circles))   
        for i in circles[0, :]:
            #圆
            # redius = np.int16(i[2])
            cv2.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
            #圆心
            cv2.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv2.imshow("circles", image)    

if __name__ == "__main__":


    capture = cv2.VideoCapture(0) #
        #cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)

    # bgfg = cv2.createBackgroundSubtractorMOG2()
    while(True):
        ret, frame = capture.read()
        # frame = cv2.flip(frame, 1)
        # face_detect_demo(frame)
        # measure_contours(frame)
        line_detection(frame)
        # detect_circles_demo(frame)
        c = cv2.waitKey(10)
        if c == 27: # ESC
            break

    # measure_contours()
    # cv2.waitKey(0)
    capture.release()
    cv2.destroyAllWindows()
