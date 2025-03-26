import cv2
import numpy as np
from pyzbar.pyzbar import decode


# 调整图像亮度模拟强光和弱光环境
def adjust_brightness(image, alpha):
    new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    return new_image


def qr_code_detection(image):
    detected_codes = []
    decoded_objects = decode(image)
    for obj in decoded_objects:
        detected_codes.append(obj.data.decode('utf-8'))
        print(f"检测到二维码，内容为: {obj.data.decode('utf-8')}")
    return detected_codes


if __name__ == "__main__":
    image = cv2.imread('12345.png')  # 替换为实际的二维码图片路径

    # 二维码识别 - 弱光环境
    weak_light_image = adjust_brightness(image, 0.5)
    print("弱光环境下 - 二维码识别：")
    qr_detected_weak = qr_code_detection(weak_light_image)

    # 二维码识别 - 强光环境
    strong_light_image = adjust_brightness(image, 2)
    print("强光环境下 - 二维码识别：")
    qr_detected_strong = qr_code_detection(strong_light_image)

    # 模拟光照不均匀
    height, width = image.shape[:2]
    gradient = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            gradient[y, x] = int(255 * x / width)
    gradient = cv2.applyColorMap(gradient, cv2.COLORMAP_JET)
    uneven_light_image = cv2.addWeighted(image, 0.7, gradient, 0.3, 0)

    # 二维码识别 - 光照不均匀环境
    print("光照不均匀环境下 - 二维码识别：")
    qr_detected_uneven = qr_code_detection(uneven_light_image)