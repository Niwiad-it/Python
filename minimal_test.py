import tkinter as tk
from tkinter import ttk
import traceback

def run_test():
    try:
        # Create the root window
        root = tk.Tk()
        
        # Set window title and size
        root.title("Minimal Test")
        root.geometry("300x200")
        
        # Try to force the window to be visible
        root.lift()  # Lift the window
        root.attributes('-topmost', True)  # Make it stay on top
        
        # Add a label
        label = ttk.Label(root, text="Test Window")
        label.pack(pady=20)
        
        # Add a quit button
        quit_btn = ttk.Button(root, text="Quit", command=root.destroy)
        quit_btn.pack(pady=10)
        
        print("Window created and should be visible")
        print("If you can't see it:")
        print("1. Check your taskbar")
        print("2. Look for a window titled 'Minimal Test'")
        print("3. Try Alt+Tab to switch to it")
        
        # Start the main loop
        root.mainloop()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nTraceback:")
        traceback.print_exc()

if __name__ == "__main__":
    print("Starting minimal test...")
    run_test()
    input("\nPress Enter to exit...")
