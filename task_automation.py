import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

def move_jpg_files():
    source_folder = input("Enter source folder path: ")
    destination_folder = input("Enter destination folder path: ")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            src = os.path.join(source_folder, file)
            dest = os.path.join(destination_folder, file)
            shutil.move(src, dest)
            moved += 1
            print(f"Moved: {file}")

    print(f"✅ {moved} JPG files moved successfully!\n")


def extract_emails():
    input_file = input("Enter input file name (e.g. input.txt): ")
    output_file = input("Enter output file name (e.g. emails.txt): ")

    try:
        with open(input_file, "r") as f:
            content = f.read()

        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

        with open(output_file, "w") as f:
            for email in emails:
                f.write(email + "\n")

        print(f"✅ {len(emails)} emails extracted and saved!\n")

    except FileNotFoundError:
        print("❌ File not found!\n")


def scrape_title():
    url = input("Enter website URL: ")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title found"

        with open("title.txt", "w") as f:
            f.write(title)

        print(f"✅ Page title saved: {title}\n")

    except Exception as e:
        print("❌ Error:", e, "\n")


def main():
    while True:
        print("===== 🛠️ Python Automation Tool =====")
        print("1. Move JPG files")
        print("2. Extract emails from file")
        print("3. Scrape webpage title")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_title()
        elif choice == "4":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

main()