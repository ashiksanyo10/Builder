import tkinter as tk
from tkinter import messagebox
import requests
from scraper import scrape_website

API_URL = "http://127.0.0.1:5000/check"

def check_gti():
    gti, task_id = scrape_website()
    if not gti or not task_id:
        messagebox.showerror("Error", "Unable to scrape GTI or Task ID.")
        return

    response = requests.post(API_URL, json={"gti": gti, "task_id": task_id})
    result = response.json()

    if result["status"] == "duplicate":
        messagebox.showinfo("Duplicate Found", f"GTI: {gti}\nRow ID: {result['rowid']}\nOld Task ID: {result['old_task_id']}")
    else:
        messagebox.showinfo("Not a Duplicate", "Please review the content.")

root = tk.Tk()
root.title("GTI Duplicate Checker")

check_button = tk.Button(root, text="Check GTI", command=check_gti)
check_button.pack()

root.mainloop()
