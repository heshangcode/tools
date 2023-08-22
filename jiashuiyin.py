from PIL import Image
import os

def add_image(image_path, watermark_path):
    # 打开图像文件
    with Image.open(image_path) as img:
        # 获取图像大小
        width, height = img.size

        # 打开水印图像文件
        with Image.open(watermark_path) as watermark:
           # 调整水印图像的大小以适应原始图像的大小
            ratio = min(width / watermark.width, height / watermark.height) / 4
            new_size = (int(watermark.width * ratio), int(watermark.height * ratio))
            watermark = watermark.resize(new_size)

            # 计算水印图像的位置
            x = (width - new_size[0]) / 2
            y = height - new_size[1]

            # 将水印图像粘贴到原始图像上
            img.paste(watermark, (int(x), int(y)), watermark)

    # 保存带有水印的新图像
    img.save(os.path.join(os.path.dirname(image_path), 'watermarked_' + os.path.basename(image_path)))
    print(f"已添加水印：{image_path}")

# 指定操作文件夹路径
user_root = os.path.expanduser("~")
desktop_path = os.path.expanduser(user_root+"/Pictures")
folder_path = os.path.join(desktop_path, "tupian")
watemark_path = user_root + "/Pictures/iPhone.png"


# 遍历文件夹中的PNG图片并添加水印
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        image_path = os.path.join(folder_path, filename)
        add_image(image_path,watemark_path)