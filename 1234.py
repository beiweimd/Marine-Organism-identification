'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-10-10 18:16:44
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-10-10 18:16:54
FilePath: \git_demo\Marine-Organism-identification\1234.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PIL import Image, ImageDraw, ImageFont

# 车牌图片尺寸
plate_width = 440
plate_height = 140

# 车牌背景颜色（蓝色）
background_color = (0, 51, 153)  # RGB 值

# 车牌文字颜色（白色）
text_color = (255, 255, 255)  # RGB 值

def draw_license_plate(license_plate):
    # 创建空白图片
    image = Image.new("RGB", (plate_width, plate_height), background_color)
    draw = ImageDraw.Draw(image)

    # 加载字体（需要字体文件，如 simhei.ttf）
    try:
        font = ImageFont.truetype("simhei.ttf", 100)  # 使用黑体字体
    except IOError:
        print("字体文件 simhei.ttf 未找到，请确保字体文件存在。")
        return None

    # 计算文字位置（居中）
    text_width, text_height = draw.textsize(license_plate, font=font)
    text_x = (plate_width - text_width) // 2
    text_y = (plate_height - text_height) // 2

    # 绘制车牌号
    draw.text((text_x, text_y), license_plate, font=font, fill=text_color)

    return image

def main():
    # 获取用户输入的车牌号
    license_plate = input("请输入车牌号（例如：京A12345）：").strip()

    # 检查车牌号长度（通常为 7 位，如“京A12345”）
    if len(license_plate) != 7:
        print("车牌号长度不正确，应为 7 位（如：京A12345）。")
        return

    # 绘制车牌图片
    plate_image = draw_license_plate(license_plate)
    if plate_image:
        # 保存图片
        plate_image.save("license_plate.png")
        print(f"车牌图片已保存为 license_plate.png")
        # 显示图片
        plate_image.show()

if __name__ == "__main__":
    main()