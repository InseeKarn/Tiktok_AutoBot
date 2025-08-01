# Tiktok_AutoBot

This project is a Python script that automates uploading videos to TikTok.

It reads data from an Excel file (`upload_list.xlsx`) containing:

- Video file paths
- Captions
- Product IDs
- Music names

- **TikTok currently restricts video uploads via automation**The script uses `pyautogui` to control mouse clicks and keyboard input to automate the 
upload process through the TikTok app interface.

---

## Important Notes

- To assist with product linking, this project includes a **Yellow Basket API desktop tool** for easier management of product IDs and integration.

- This automation script is **built and tested specifically for my monitor resolution and screen layout**. You will need to adjust mouse click coordinates (`x, y`) in the script to fit your own screen setup. or maybe i'll build something easier in future.

---

## How to Use

1. Install dependencies:

```bash
pip install pandas pyautogui openpyxl
