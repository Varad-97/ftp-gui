from src.server import FTPServerManager
from src.gui import FTPGUI

def main():
    server_manager = FTPServerManager(log_callback=None)
    gui = FTPGUI(server_manager)
    server_manager.log_callback = gui.log_message
    gui.run()

if __name__ == "__main__":
    main() 