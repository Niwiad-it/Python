import traceback
import sys

def check_imports():
    packages = {
        'tkinter': 'Built-in GUI package',
        'sv_ttk': 'Sun Valley theme for ttk',
        'cryptography': 'Cryptography package'
    }
    
    missing = []
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✓ {package} - {description}")
        except ImportError as e:
            missing.append(f"✗ {package} - {description} - Error: {str(e)}")
    
    if missing:
        print("\nMissing packages:")
        for msg in missing:
            print(msg)
        return False
    return True

try:
    print("Checking required packages...")
    if not check_imports():
        print("\nPlease install missing packages.")
        sys.exit(1)
        
    print("\nStarting application...")
    from UI import CryptoApp
    import tkinter as tk
    
    def main():
        root = tk.Tk()
        app = CryptoApp(root)
        print("\nApplication window created. If you don't see it:")
        print("1. Check if it's behind other windows")
        print("2. Look for it in your taskbar")
        root.mainloop()

    if __name__ == "__main__":
        main()
except Exception as e:
    print("\nError occurred:")
    print(str(e))
    print("\nFull traceback:")
    traceback.print_exc()
    
input("\nPress Enter to exit...")
