from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog, messagebox
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


def phrase_search_in_document():
    print("Welcome to phrase detecction app!")

    root=tk.Tk()
    root.title("PDF Phrase Search Using Rabin Karp")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    with open("Student Project # 2.pdf", 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
            #print(page.extract_text())

    print(text)

    document = text
    phrase =input("enter the phrase to search for: ")
    matches = rabin_karp(text, phrase)
    print(matches)
    for i in range(13):
        print(f"{i}: {text[i]}")




if __name__ == "__main__":
    phrase_search_in_document()