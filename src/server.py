import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer
from .handler import MyHandler

class FTPServerManager:
    def __init__(self, log_callback):
        self.server = None
        self.log_callback = log_callback

    def start_server(self, username, password, ftp_directory):
        if not os.path.exists(ftp_directory):
            self.log_callback(f"Error: Directory {ftp_directory} does not exist.")
            return

        authorizer = DummyAuthorizer()
        authorizer.add_user(username, password, ftp_directory, perm="elrw")

        handler = MyHandler
        handler.authorizer = authorizer
        handler.banner = "Welcome to master's FTP server"
        handler.log_callback = self.log_callback

        address = ('0.0.0.0', 2121)

        try:
            self.server = FTPServer(address, handler)
            self.server.max_cons = 256
            self.server.max_cons_per_ip = 5
            self.log_callback(f"FTP server is running on port {address[1]}")
            self.server.serve_forever()
        except PermissionError:
            self.log_callback("Error: Permission denied. Try running the script with sudo or as an administrator.")
        except OSError as e:
            self.log_callback(f"Error: {e}")

    def stop_server(self):
        if self.server:
            self.server.close_all()
            self.log_callback("FTP server stopped.") 
