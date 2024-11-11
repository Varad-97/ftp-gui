from pyftpdlib.handlers import FTPHandler

class MyHandler(FTPHandler):
    def on_connect(self):
        self.log_callback(f"New connection from {self.remote_ip}")

    def on_disconnect(self):
        self.log_callback(f"Disconnection from {self.remote_ip}")

    def on_login(self, username):
        self.log_callback(f"User {username} logged in from {self.remote_ip}")

    def on_file_sent(self, file):
        self.log_callback(f"File sent: {file} to {self.remote_ip}")
    
    def on_file_received(self, file):
        self.log_callback(f"File received: {file} from {self.remote_ip}")
    
    def on_incomplete_file_sent(self, file):
        self.log_callback(f"Incomplete file sent: {file} to {self.remote_ip}")
    
    def on_incomplete_file_received(self, file):
        self.log_callback(f"Incomplete file received: {file} from {self.remote_ip}")

    def on_enter(self, path):
        self.log_callback(f"Directory entered: {path} by {self.remote_ip}")

    def on_mkdir(self, path):
        self.log_callback(f"Directory created: {path} by {self.remote_ip}")

    def on_rmdir(self, path):
        self.log_callback(f"Directory removed: {path} by {self.remote_ip}")

    def on_rename(self, old, new):
        self.log_callback(f"Rename: {old} to {new} by {self.remote_ip}") 