import traceback

try:
    from UI import CryptoApp
    import tkinter as tk
    
    def main():
        root = tk.Tk()
        app = CryptoApp(root)
        root.mainloop()

    if __name__ == "__main__":
        main()
except Exception as e:
    print("Error occurred:")
    print(str(e))
    print("\nFull traceback:")
    traceback.print_exc()
    input("Press Enter to exit...")
