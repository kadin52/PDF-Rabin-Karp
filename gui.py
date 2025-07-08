import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_handler import load_pdf
from search_algorithm import rabin_karp

class PDFSearchApp:
    def __init__(self):
        self.text = ""
        self.title = ""
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("PDF Phrase Search Using Rabin Karp")
        self.root.geometry("800x600")

        b_frame = tk.Frame(self.root)
        b_frame.pack(side="top")

        self.title_label = tk.Label(b_frame, text="No file uploaded")
        self.title_label.pack(side="left", padx=5)

        upload_button = tk.Button(b_frame, text="Upload PDF", command=self.upload_file)
        upload_button.pack(side="left", padx=5)

        p_frame = tk.Frame(self.root)
        p_frame.pack(side="top", pady=40)

        instruction = tk.Label(p_frame, text="Enter phrase to search:", font=("Arial", 12))
        instruction.pack(side="left", padx=5)

        self.phrase_entry = tk.Entry(p_frame, width=50, font=("Arial", 12),
                                     highlightbackground="black", 
                                     highlightcolor="black", 
                                     highlightthickness=1)
        self.phrase_entry.pack(side="left", padx=5)

        search_button = tk.Button(self.root, text="Search", command=self.search)
        search_button.pack(pady=5)

        self.search_results = tk.Label(self.root, text="", fg='blue',
                                       font=("Arial", 10), wraplength=700, justify='left')
        self.search_results.pack(pady=80)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                self.text, self.title = load_pdf(file_path)
                self.title_label.config(text=f"Uploaded: {self.title}")
                print(f"file_path: {file_path}")
                print(f"title: {self.title}")
                print(self.text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load PDF: {str(e)}")

    def search(self):
        pattern = self.phrase_entry.get()
        if not self.text:
            messagebox.showwarning("Warning", "Please upload a PDF file first.")
            return

        if not pattern:
            messagebox.showwarning("Warning", "Please enter a phrase to search.")
            return

        matches = rabin_karp(self.text, pattern)
        if matches:
            result = f"Found {len(matches)} matches at positions: {matches}"
            self.search_results.config(text=result)
        else:
            self.search_results.config(text="No matches found.")

    def run(self):
        self.root.mainloop()