from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

def rabin_karp(text,pattern,q=101):
    d = 256
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q #precomputed value for hash rolling
    p_hash = 0
    t_hash = 0
    matches = [] #stores starting indices of matches


    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q #udate pattern hash
        t_hash = (d * t_hash + ord(text[i])) % q #update text hash

    for i in range(n-m+1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                matches.append(i)
        if i<n-m:
            t_hash = (d*(t_hash - ord(text[i]) * h ) +ord(text[i+m])) % q

            if t_hash<0:
                t_hash += q
    return matches

def search(pattern, results_box):

    matches = rabin_karp(text,pattern)


    if matches:
        result = f"Found {len(matches)} matches at positions: {matches}"
        results_box.config(text = result)
    else:
        results_box.config(text = "No matches found.")


def upload_file(title_label):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    global text
    text=""
    if file_path:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            title = Path(file_path).name

            for page in reader.pages:
                text += page.extract_text()



        title_label.config(text=f"Uploaded: {title}")

    print(f"file_path: {file_path}")
    print(f"title: {title}")
    print(text)
    return text


def phrase_search_in_document():
    print("Welcome to phrase detection app!")
    global text
    root=tk.Tk()
    root.title("PDF Phrase Search Using Rabin Karp")

    root.geometry("800x600")


    b_frame = tk.Frame(root)
    b_frame.pack(side="top")
    p_frame =tk.Frame(root)
    p_frame.pack(side="top",pady=40)

    upload_button = tk.Button(b_frame,text="Upload PDF", command=lambda:upload_file(title_label))
    upload_button.pack(side = "left",padx=5)

    title_label = tk.Label(b_frame, text = "No file uploaded")
    title_label.pack(side="left",padx=5)

    instruction = tk.Label(p_frame, text="Enter phrase to search:", font=("Arial", 12))
    instruction.pack(side='left',padx=5)

    phrase_entry = tk.Entry(p_frame,width=50,font=("Arial", 12),
                    highlightbackground="black", highlightcolor="black", highlightthickness=1)
    phrase_entry.pack(side="left",padx=5)

    search_button = tk.Button(root,text = "Search",
                    command=lambda:search(phrase_entry.get(), search_results))
    search_button.pack(pady=5)

    search_results = tk.Label(root,text="",fg='blue',font = ("arial",10),wraplength=700,justify='left')
    search_results.pack(pady=80)

    root.mainloop()

if __name__ == "__main__":
    phrase_search_in_document()

