import pandas as pd
import pyautogui
import pyperclip
import time
import os

DELAY_OPEN_APP = 6
DELAY_BETWEEN_ACTIONS = 2

# Read the Excel file
df = pd.read_excel(r"D:\projects\Tiktok_AutoBot\upload_list.xlsx")

# Read the last index from a file to resume from where it left off(if it done start from 0)
index_file = "last_index.txt"
if os.path.exists(index_file):
    with open(index_file, "r") as f:
        last_index = int(f.read().strip())
else:
    last_index = 0

# Ceck index 
if last_index >= len(df):
    last_index = 0

# while True:
#     print(pyautogui.position())

for index, row in df.iterrows():
    video_path = row["video_path"]
    caption = row["caption"]
    product_ids_raw = str(row["product_ids"])
    music = row["music_name"]
    product_ids = [pid.strip() for pid in product_ids_raw.split("|") if pid.strip()]

    # ✅ Start TikTok
    print(f"🎬 Opening Tiktok: {video_path}")
    os.system("start shell:AppsFolder\\BytedancePte.Ltd.TikTok_6yccndn6064se!App")  # ← แก้ path นี้ให้ตรงกับเครื่องของคุณ
    time.sleep(DELAY_OPEN_APP)

    # ✅ Click on upload video button
    pyautogui.click(x=100, y=380)  
    time.sleep(DELAY_BETWEEN_ACTIONS)

    # ✅ Click on upload video button
    pyautogui.click(x=1081, y=464)  
    time.sleep(DELAY_BETWEEN_ACTIONS)
    # ✅ Select video file
    pyperclip.copy(video_path)
    pyautogui.hotkey("ctrl", "v") 
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)

    # ✅ type caption
    pyautogui.click(x=471, y=387)
    pyautogui.hotkey("ctrl", "a")  # Delete existing caption
    pyautogui.press("backspace")  # Delete existing caption
    print(repr(caption))  # Debug: print caption to console
    pyperclip.copy(caption,) #Copy hashtags
    pyautogui.hotkey("ctrl", "v") # paste caption
    time.sleep(DELAY_BETWEEN_ACTIONS)

    # ✅ Add products
    for i, pid in enumerate(product_ids, 1):
        print(f"Added product {i}/{len(product_ids)}: {pid}")
        pyautogui.click(x=357, y=1000)  # click Add products
        pyautogui.click(x=1160, y=634)  # Click next 
        time.sleep(DELAY_BETWEEN_ACTIONS)
        pyautogui.click(x=572, y=259)  # Click search bar
        pyautogui.write(pid)
        pyautogui.press("enter")
        time.sleep(DELAY_BETWEEN_ACTIONS)
        pyautogui.click(x=448, y=403)  # click add
        time.sleep(DELAY_BETWEEN_ACTIONS)
        pyautogui.click(x=1453, y=977)  
        time.sleep(DELAY_BETWEEN_ACTIONS) 
        pyautogui.click(x=1149, y=654)  
        time.sleep(DELAY_BETWEEN_ACTIONS)
        

    # ✅ Add music
    pyautogui.click(x=1744, y=966)  # Click Edit video
    time.sleep(3)
    pyautogui.click(x=703, y=235)
    pyperclip.copy(music) # Copy music name
    pyautogui.hotkey("ctrl", "v")  # Paste music name
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.click(x=852, y=283)  # Click use
    time.sleep(1)
    pyautogui.click(x=852, y=283)  # Click use
    pyautogui.click(x=604, y=642)  # Edit volume
    pyautogui.click(x=647, y=544)  # Edit volume
    pyautogui.click(x=1353, y=940)  # Save edit
    time.sleep(1)

    # ✅ Post or Save draft
    pyautogui.scroll(-1000)
    # pyautogui.click(x=387, y=980)  # Post
    pyautogui.click(x=624, y=976)  # Save draft
    print(f"✅ Upload successfully: {video_path}")
    with open(index_file, "w") as f:
        f.write(str(last_index + 1))

    time.sleep(10)
