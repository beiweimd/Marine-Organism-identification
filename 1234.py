'''
Author: shiming422 1611813195@qq.com
Date: 2025-10-10 18:16:44
LastEditors: shiming422 1611813195@qq.com
LastEditTime: 2025-10-11 13:24:48
FilePath: \git_demo\Marine-Organism-identification\1234.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

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