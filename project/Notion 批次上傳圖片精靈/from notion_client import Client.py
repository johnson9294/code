from notion_client import Client
import os

# 初始化 Notion 客戶端
notion = Client(auth="secret_SWehVJeLU7FUG0QujwuzG6Oz2kf0HBeS4Mc55bph4Sc")

# 定義你的資料庫ID
database_id = "cf3218a9c2da48c89503d8e888a8a2f2"

# 取得圖片目錄
image_dir = r"C:\Users\johns\圖片\20240825STFC\選\未命名的轉存"

# 批次上傳圖片
for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    
    # 判斷是否為圖片檔案
    if os.path.isfile(image_path) and image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        
        # 在 Notion 資料庫中新增一個條目
        notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "Name": {"title": [{"text": {"content": image_name}}]},
                "Image": {
                    "files": [
                        {
                            "name": image_name,
                            "type": "external",
                            "external": {"url": f"file://{image_path}"}
                        }
                    ]
                }
            }
        )
        print(f"{image_name} 已成功上傳至 Notion 資料庫")
