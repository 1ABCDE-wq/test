import cv2
import numpy as np


# RGB颜色空间颜色识别
def rgb_color_detection(image):
    # 将图像转换为RGB格式
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 定义颜色范围（RGB格式）
    color_ranges = {
        'white': ([200, 200, 200], [255, 255, 255]),
       'red': ([0, 0, 100], [100, 50, 255]),
        'blue': ([100, 0, 0], [255, 50, 50]),
        'yellow': ([0, 100, 100], [50, 255, 255]),
        'green': ([0, 100, 0], [50, 255, 50]),
        'black': ([0, 0, 0], [50, 50, 50])
    }

    detected_colors = []
    # 遍历颜色范围，进行颜色检测
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(rgb_image, lower, upper)
        if cv2.countNonZero(mask) > 0:
            detected_colors.append(color)
            print(f"在RGB颜色空间中检测到 {color}")
            # 展示识别结果
            result = cv2.bitwise_and(rgb_image, rgb_image, mask=mask)
            cv2.imshow(f"{color} 在RGB中", result)

    return detected_colors


# HSV颜色空间颜色识别
def hsv_color_detection(image):
    # 将图像转换为HSV格式
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义颜色范围（HSV格式）
    color_ranges = {
        'white': ([0, 0, 200], [180, 30, 255]),
       'red': ([0, 100, 100], [10, 255, 255]),
        'blue': ([100, 100, 50], [130, 255, 255]),
        'yellow': ([20, 100, 100], [30, 255, 255]),
        'green': ([40, 100, 50], [80, 255, 255]),
        'black': ([0, 0, 0], [180, 255, 50])
    }

    detected_colors = []
    # 遍历颜色范围，进行颜色检测
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv_image, lower, upper)
        if cv2.countNonZero(mask) > 0:
            detected_colors.append(color)
            print(f"在HSV颜色空间中检测到 {color}")
            # 展示识别结果
            result = cv2.bitwise_and(image, image, mask=mask)
            cv2.imshow(f"{color} 在HSV中", result)

    return detected_colors


if __name__ == "__main__":
    image = cv2.imread('0_cropped.jpg')  # 把这里替换成你的图片路径
    rgb_detected = rgb_color_detection(image)
    hsv_detected = hsv_color_detection(image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
