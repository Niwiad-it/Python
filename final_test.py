import tkinter as tk
from tkinter import ttk
import sys
import traceback

def show_window():
    try:
        # Create and configure root window
        root = tk.Tk()
        root.title("Final Test")
        root.geometry("400x300+100+100")  # Size and position
        
        # Force window to be visible
        root.attributes('-topmost', True)
        root.update()
        
        # Create a frame with padding
        frame = ttk.Frame(root, padding=20)
        frame.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid weights
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        # Add widgets
        label = ttk.Label(frame, text="Can you see this window?")
        label.grid(row=0, column=0, pady=10)
        
        # Add exit button
        exit_button = ttk.Button(frame, text="Exit", command=root.destroy)
        exit_button.grid(row=1, column=0, pady=10)
        
        # Print instructions
        print("\nWindow should now be visible:")
        print("1. Look for 'Final Test' window")
        print("2. Check taskbar")
        print("3. Try Alt+Tab")
        print("4. Look at coordinates 100,100 on your screen")
        print("\nIf you can see the window, click 'Exit' to close it")
        
        # Disable topmost after a short delay
        root.after(2000, lambda: root.attributes('-topmost', False))
        
        # Start main loop
        root.mainloop()
        return True
        
    except Exception as e:
        print(f"\nError creating window: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Starting final test...")
    if show_window():
        print("\nWindow was created and closed successfully")
    else:
        print("\nFailed to create window")
    
    print("\nPress Enter to exit...")
    input()
