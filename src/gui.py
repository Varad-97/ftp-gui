import tkinter as tk
from tkinter import scrolledtext, filedialog
import threading
from .ipfetch import get_ethernet_ip

class FTPGUI:
    def __init__(self, server_manager):
        self.server_manager = server_manager
        self.root = tk.Tk()
        self.setup_gui()

    def setup_gui(self):
        self.root.title("FTP Server")
        self.root.geometry("600x400")
        self.root.configure(bg="#1c1c1c")

        ip_address = get_ethernet_ip() or "Not Available"
        ip_label = tk.Label(
            self.root, 
            text=f"Your Ethernet IP: {ip_address}", 
            bg="#1c1c1c", 
            fg="white",
            font=("Arial", 10, "bold")
        )
        ip_label.pack(pady=5)

        # Create frame
        frame = tk.Frame(self.root, bg="#1c1c1c")
        frame.pack(pady=10)

        # Username
        tk.Label(frame, text="Username:", bg="#1c1c1c", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password
        tk.Label(frame, text="Password:", bg="#1c1c1c", fg="white").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Directory
        self.directory_var = tk.StringVar()
        tk.Label(frame, text="FTP Directory:", bg="#1c1c1c", fg="white").grid(row=2, column=0, padx=5, pady=5)
        directory_entry = tk.Entry(frame, textvariable=self.directory_var, width=40)
        directory_entry.grid(row=2, column=1, padx=5, pady=5)

        select_button = tk.Button(frame, text="Select Directory", command=self.select_directory)
        select_button.grid(row=2, column=2, padx=5, pady=5)

        # Control buttons
        start_button = tk.Button(self.root, text="Start Server", command=self.start_server_thread)
        start_button.pack(pady=5)

        stop_button = tk.Button(self.root, text="Stop Server", command=self.server_manager.stop_server)
        stop_button.pack(pady=5)

        # Log area
        self.log_area = scrolledtext.ScrolledText(
            self.root, width=50, height=15, bg="#2c2c2c", fg="white", insertbackground='white'
        )
        self.log_area.pack(pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_var.set(directory)
            self.log_message(f"Selected directory: {directory}")

    def start_server_thread(self):
        thread = threading.Thread(
            target=self.server_manager.start_server,
            args=(
                self.username_entry.get(),
                self.password_entry.get(),
                self.directory_var.get()
            )
        )
        thread.daemon = True
        thread.start()

    def log_message(self, message):
        self.log_area.insert(tk.END, message + '\n')
        self.log_area.yview(tk.END)

    def run(self):
        self.root.mainloop() 