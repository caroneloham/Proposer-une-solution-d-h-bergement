import socket
import threading

# Configuration des ports à écouter
PORTS = [8080, 8888, 9999]  # Exemple de ports à simuler

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Activité détectée : {data}")
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        client_socket.close()

def setup_port_listener(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Écoute sur le port {port}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connexion détectée de {addr} sur le port {port}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    finally:
        server_socket.close()
        print(f"Port {port} fermé")

def main():
    for port in PORTS:
        thread = threading.Thread(target=setup_port_listener, args=(port,))
        thread.start()

if __name__ == "__main__":
    main()
