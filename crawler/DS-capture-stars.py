import io

import requests
from PIL.Image import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# 配置参数
keyword = "王楚然"  # 明星名字
save_folder = "./weibo_images/"
os.makedirs(save_folder, exist_ok=True)

# 启动浏览器（需下载ChromeDriver）
driver = webdriver.Chrome()
driver.get(f"https://s.weibo.com/weibo?q={keyword}&type=image")

# 模拟滚动加载（微博图片需滚动页面触发加载）
for _ in range(5):  # 控制滚动次数
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # 防止被封IP

# 提取图片链接
count = 0  # 成功下载计数器
images = driver.find_elements(By.CSS_SELECTOR, "img[src*='large']")

for img in images:
    img_url = img.get_attribute("src")
    try:
        # 下载图片数据
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
        img_data = response.content

        # 验证图片尺寸
        with Image.open(io.BytesIO(img_data)) as img_pil:
            width, height = img_pil.size

            # 竖屏判定标准：高度 > 宽度 且 高度 ≥ 800px
            if height > width and height >= 800:
                # 保存合格图片
                with open(f"{save_folder}/{keyword}_{count}.jpg", "wb") as f:
                    f.write(img_data)
                print(f"成功下载：{img_url} ({width}x{height})")
                count += 1
            else:
                print(f"跳过非竖屏/低清：{img_url} ({width}x{height})")

    except Exception as e:
        print(f" 失败：{img_url} - {str(e)}")
driver.quit()
