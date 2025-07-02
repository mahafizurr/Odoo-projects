import socket
import json

HOST = '0.0.0.0'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024).decode()
            if data:
                # Process barcode and send to Odoo
                print(f"Scanned: {data}")
                # Add Odoo API integration here