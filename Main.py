import tkinter as tk
from tkinter import messagebox
from scraper import scrape_data
from backend import db_utils


class GTICheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GTI Duplicate Check")
        self.root.geometry("300x150")
        
        # Create UI components
        self.start_button = tk.Button(root, text="Start", command=self.start_check)
        self.start_button.pack(pady=20)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_check)
        self.stop_button.pack(pady=10)
        
    def start_check(self):
        # Scrape data and check for duplicates
        try:
            gti, task_id = scrape_data()
            if not gti:
                messagebox.showinfo("Error", "Website is not open or GTI not found!")
                return
            
            duplicate, row_id, old_task_id = db_utils.check_duplicate(gti, task_id)
            
            if duplicate:
                db_utils.log_duplicate(gti, old_task_id, task_id)
                messagebox.showinfo(
                    "Duplicate Found", 
                    f"Duplicate Found!\nRow ID: {row_id}\nOld Task ID: {old_task_id}"
                )
            else:
                messagebox.showinfo("Not a Duplicate", "Not a duplicate. Please review!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def stop_check(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GTICheckerApp(root)
    root.mainloop()
