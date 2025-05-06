import tkinter as tk
from tkinter import ttk
import sv_ttk

def main():
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("300x200")
    
    # Apply theme
    sv_ttk.set_theme("dark")
    
    # Add a button
    button = ttk.Button(root, text="Test Button")
    button.pack(pady=20)
    
    print("Window created - check your taskbar!")
    root.mainloop()

if __name__ == "__main__":
    main()
