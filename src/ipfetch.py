import socket

def get_ethernet_ip():
    """
    Get the IP address of the Ethernet interface.

    Returns:
        str: The IP address of the Ethernet interface, or None if an error occurs.
    """
    try:
        # Create a socket and connect to a public DNS server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except socket.error as e:
        print(f"Socket error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    finally:
        s.close()
    
    return ip

if __name__ == "__main__":
    # This block will only run if the module is executed as a script
    ip_address = get_ethernet_ip()
    if ip_address:
        print(f"Ethernet IP address: {ip_address}")
    else:
        print("Could not retrieve the Ethernet IP address.")
