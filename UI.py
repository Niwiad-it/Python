import os
import tkinter as tk
import sv_ttk
from tkinter import ttk, messagebox, filedialog
from my_functions import encrypt_message, decrypt_message
from key_generator import generate_new_keypair, save_keys_to_file, load_keys_from_file
from file_utils import save_message_to_file, load_message_from_file

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Manager")
        self.root.geometry("1024x768")
        
        # Apply Windows 11 theme
        sv_ttk.set_theme("dark")  # Modern dark theme
        
        # Configure grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Main container
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        
        # Create theme toggle button
        self.theme_button = ttk.Button(
            self.main_frame,
            text="Toggle Theme",
            command=self.toggle_theme,
            style="Accent.TButton"
        )
        self.theme_button.grid(row=0, column=0, sticky="NE", padx=5, pady=5)
        
        # Tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create tabs
        self.keys_tab = ttk.Frame(self.notebook)
        self.encrypt_tab = ttk.Frame(self.notebook)
        self.decrypt_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.keys_tab, text="Key Management")
        self.notebook.add(self.encrypt_tab, text="Encrypt")
        self.notebook.add(self.decrypt_tab, text="Decrypt")
        
        # Setup each tab
        self.setup_keys_tab()
        self.setup_encrypt_tab()
        self.setup_decrypt_tab()
        
        # Current keys
        self.current_public_key = None
        self.current_private_key = None
        
        # Load saved keys if they exist
        self.load_saved_keys()

    def toggle_theme(self):
        """Toggle between light and dark theme"""
        current_theme = sv_ttk.get_theme()
        if current_theme == "dark":
            sv_ttk.set_theme("light")
        else:
            sv_ttk.set_theme("dark")

    def setup_keys_tab(self):
        # Key Generation Frame
        key_frame = ttk.LabelFrame(self.keys_tab, text="Key Generation", padding="10")
        key_frame.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        key_frame.columnconfigure(1, weight=1)
        
        # Bit length selection
        ttk.Label(key_frame, text="Key Size:").grid(row=0, column=0, padx=5, pady=5)
        self.key_size_var = tk.StringVar(value="2048")
        key_size_combo = ttk.Combobox(key_frame, textvariable=self.key_size_var)
        key_size_combo['values'] = ('1024', '2048', '4096')
        key_size_combo.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Buttons frame
        buttons_frame = ttk.Frame(key_frame)
        buttons_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Generate button with modern style
        generate_btn = ttk.Button(
            buttons_frame,
            text="Generate New Keypair",
            command=self.generate_keys,
            style="Accent.TButton"
        )
        generate_btn.pack(side=tk.LEFT, padx=5)
        
        # Save/Load buttons
        save_btn = ttk.Button(
            buttons_frame,
            text="Save Keys",
            command=self.save_keys
        )
        save_btn.pack(side=tk.LEFT, padx=5)
        
        load_btn = ttk.Button(
            buttons_frame,
            text="Load Keys",
            command=self.load_keys
        )
        load_btn.pack(side=tk.LEFT, padx=5)
        
        # Key Display Frame
        display_frame = ttk.LabelFrame(self.keys_tab, text="Current Keys", padding="10")
        display_frame.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        display_frame.columnconfigure(0, weight=1)
        
        # Public key display
        ttk.Label(display_frame, text="Public Key:").grid(row=0, column=0, sticky=tk.W)
        self.public_key_text = tk.Text(display_frame, height=4, width=50)
        self.public_key_text.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Private key display
        ttk.Label(display_frame, text="Private Key:").grid(row=2, column=0, sticky=tk.W)
        self.private_key_text = tk.Text(display_frame, height=4, width=50)
        self.private_key_text.grid(row=3, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))

    def setup_encrypt_tab(self):
        # Message input frame
        input_frame = ttk.LabelFrame(self.encrypt_tab, text="Message", padding="10")
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        input_frame.columnconfigure(0, weight=1)
        
        # Message input
        ttk.Label(input_frame, text="Message to encrypt:").grid(row=0, column=0, sticky=tk.W)
        self.encrypt_input = tk.Text(input_frame, height=5, width=50)
        self.encrypt_input.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Buttons frame
        buttons_frame = ttk.Frame(input_frame)
        buttons_frame.grid(row=2, column=0, pady=10)
        
        # Encrypt button
        encrypt_btn = ttk.Button(
            buttons_frame,
            text="Encrypt",
            command=self.encrypt_message,
            style="Accent.TButton"
        )
        encrypt_btn.pack(side=tk.LEFT, padx=5)
        
        # Load/Save buttons
        load_btn = ttk.Button(
            buttons_frame,
            text="Load Message",
            command=lambda: self.load_message(self.encrypt_input)
        )
        load_btn.pack(side=tk.LEFT, padx=5)
        
        # Result frame
        result_frame = ttk.LabelFrame(self.encrypt_tab, text="Result", padding="10")
        result_frame.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        result_frame.columnconfigure(0, weight=1)
        
        # Result
        ttk.Label(result_frame, text="Encrypted result:").grid(row=0, column=0, sticky=tk.W)
        self.encrypt_output = tk.Text(result_frame, height=5, width=50)
        self.encrypt_output.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Save result button
        save_btn = ttk.Button(
            result_frame,
            text="Save Result",
            command=lambda: self.save_message(self.encrypt_output.get(1.0, tk.END))
        )
        save_btn.grid(row=2, column=0, pady=10)

    def setup_decrypt_tab(self):
        # Message input frame
        input_frame = ttk.LabelFrame(self.decrypt_tab, text="Encrypted Message", padding="10")
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        input_frame.columnconfigure(0, weight=1)
        
        # Message input
        ttk.Label(input_frame, text="Message to decrypt:").grid(row=0, column=0, sticky=tk.W)
        self.decrypt_input = tk.Text(input_frame, height=5, width=50)
        self.decrypt_input.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Buttons frame
        buttons_frame = ttk.Frame(input_frame)
        buttons_frame.grid(row=2, column=0, pady=10)
        
        # Decrypt button
        decrypt_btn = ttk.Button(
            buttons_frame,
            text="Decrypt",
            command=self.decrypt_message,
            style="Accent.TButton"
        )
        decrypt_btn.pack(side=tk.LEFT, padx=5)
        
        # Load button
        load_btn = ttk.Button(
            buttons_frame,
            text="Load Message",
            command=lambda: self.load_message(self.decrypt_input)
        )
        load_btn.pack(side=tk.LEFT, padx=5)
        
        # Result frame
        result_frame = ttk.LabelFrame(self.decrypt_tab, text="Result", padding="10")
        result_frame.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        result_frame.columnconfigure(0, weight=1)
        
        # Result
        ttk.Label(result_frame, text="Decrypted result:").grid(row=0, column=0, sticky=tk.W)
        self.decrypt_output = tk.Text(result_frame, height=5, width=50)
        self.decrypt_output.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Save result button
        save_btn = ttk.Button(
            result_frame,
            text="Save Result",
            command=lambda: self.save_message(self.decrypt_output.get(1.0, tk.END))
        )
        save_btn.grid(row=2, column=0, pady=10)

    def generate_keys(self):
        """Generate new key pair"""
        try:
            bit_length = int(self.key_size_var.get())
            public_key, private_key = generate_new_keypair(bit_length)
            
            self.current_public_key = public_key
            self.current_private_key = private_key
            
            # Display keys
            self.public_key_text.delete(1.0, tk.END)
            self.public_key_text.insert(1.0, public_key)
            
            self.private_key_text.delete(1.0, tk.END)
            self.private_key_text.insert(1.0, private_key)
            
            # Save keys to default location
            save_keys_to_file(public_key, private_key)
            
            messagebox.showinfo("Success", "New keypair generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate keys: {str(e)}")

    def save_keys(self):
        """Save current keys to files"""
        if not self.current_public_key or not self.current_private_key:
            messagebox.showerror("Error", "No keys to save!")
            return
        
        try:
            directory = filedialog.askdirectory(title="Select Directory to Save Keys")
            if directory:
                public_file = os.path.join(directory, "public_key.pem")
                private_file = os.path.join(directory, "private_key.pem")
                
                save_keys_to_file(self.current_public_key, self.current_private_key,
                                public_file, private_file)
                
                messagebox.showinfo("Success", "Keys saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save keys: {str(e)}")

    def load_keys(self):
        """Load keys from files"""
        try:
            directory = filedialog.askdirectory(title="Select Directory with Keys")
            if directory:
                public_file = os.path.join(directory, "public_key.pem")
                private_file = os.path.join(directory, "private_key.pem")
                
                public_key, private_key = load_keys_from_file(public_file, private_file)
                
                self.current_public_key = public_key
                self.current_private_key = private_key
                
                # Display keys
                self.public_key_text.delete(1.0, tk.END)
                self.public_key_text.insert(1.0, public_key)
                
                self.private_key_text.delete(1.0, tk.END)
                self.private_key_text.insert(1.0, private_key)
                
                messagebox.showinfo("Success", "Keys loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load keys: {str(e)}")

    def load_saved_keys(self):
        """Try to load previously saved keys"""
        try:
            if os.path.exists("public_key.pem") and os.path.exists("private_key.pem"):
                public_key, private_key = load_keys_from_file()
                self.current_public_key = public_key
                self.current_private_key = private_key
                
                # Display keys
                self.public_key_text.delete(1.0, tk.END)
                self.public_key_text.insert(1.0, public_key)
                
                self.private_key_text.delete(1.0, tk.END)
                self.private_key_text.insert(1.0, private_key)
        except Exception:
            pass  # Silently fail if keys can't be loaded

    def encrypt_message(self):
        """Encrypt message using current public key"""
        if not self.current_public_key:
            messagebox.showerror("Error", "No public key available!")
            return
        
        message = self.encrypt_input.get(1.0, tk.END).strip()
        if not message:
            messagebox.showerror("Error", "No message to encrypt!")
            return
        
        try:
            encrypted = encrypt_message(self.current_public_key, message)
            self.encrypt_output.delete(1.0, tk.END)
            self.encrypt_output.insert(1.0, encrypted)
            messagebox.showinfo("Success", "Message encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt message: {str(e)}")

    def decrypt_message(self):
        """Decrypt message using current private key"""
        if not self.current_private_key:
            messagebox.showerror("Error", "No private key available!")
            return
        
        encrypted = self.decrypt_input.get(1.0, tk.END).strip()
        if not encrypted:
            messagebox.showerror("Error", "No message to decrypt!")
            return
        
        try:
            decrypted = decrypt_message(self.current_private_key, encrypted)
            self.decrypt_output.delete(1.0, tk.END)
            self.decrypt_output.insert(1.0, decrypted)
            messagebox.showinfo("Success", "Message decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt message: {str(e)}")

    def load_message(self, text_widget):
        """Load message from file into specified text widget"""
        file_path = filedialog.askopenfilename(
            title="Select Message File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                message = load_message_from_file(file_path)
                if message:
                    text_widget.delete(1.0, tk.END)
                    text_widget.insert(1.0, message)
                    return True
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load message: {str(e)}")
        return False

    def save_message(self, message):
        """Save message to file"""
        if not message.strip():
            messagebox.showerror("Error", "No message to save!")
            return False
            
        file_path = filedialog.asksaveasfilename(
            title="Save Message",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                save_message_to_file(message, file_path)
                messagebox.showinfo("Success", "Message saved successfully!")
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save message: {str(e)}")
        return False

def main():
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()