import os
import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk
import traceback
import sys

def create_window():
    try:
        # Create main window
        root = tk.Tk()
        root.title("Debug Test")
        root.geometry("400x300")
        
        print("1. Window created")
        
        # Try to set theme
        try:
            sv_ttk.set_theme("dark")
            print("2. Theme set successfully")
        except Exception as e:
            print(f"Theme error: {str(e)}")
        
        # Create main frame
        frame = ttk.Frame(root, padding="20")
        frame.grid(row=0, column=0, sticky="nsew")
        print("3. Frame created")
        
        # Configure grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        print("4. Grid configured")
        
        # Add a test button
        btn = ttk.Button(frame, text="Test Button")
        btn.grid(row=0, column=0, pady=10)
        print("5. Button added")
        
        # Add a label
        label = ttk.Label(frame, text="If you can see this window, click the button")
        label.grid(row=1, column=0, pady=10)
        print("6. Label added")
        
        print("\nWindow should be visible now. Check your taskbar!")
        print("The window should have a modern dark theme with a button and label.")
        
        root.mainloop()
        
    except Exception as e:
        print(f"\nError creating window: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    print("Starting debug test...")
    create_window()
    input("\nPress Enter to exit...")
