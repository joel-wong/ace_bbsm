import socket

from ace_bbsm import BBSM_CONSTANTS
from ace_bbsm import message


class Server:
    bbb_socket = None
    connection = None
    address = None

    def __init__(self):
        self.bbb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_client(self):
        self.connection, self.address = self.bbb_socket.accept()
        print('Connected by', self.address)

    def receive_from_client(self):
        return message.recv_msg(self.connection)

    def send_to_client(self, data):
        message.send_msg(self.connection, data)

    def disconnect_from_client(self):
        self.connection.close()

    def start_server(self):
        self.bbb_socket.bind((BBSM_CONSTANTS.HOST, BBSM_CONSTANTS.PORT))
        self.bbb_socket.listen()
        if BBSM_CONSTANTS.ALLOW_SERVER_TIMEOUT:
            s.bbb_socket.settimeout(BBSM_CONSTANTS.SERVER_TIMEOUT)

    def close_server(self):
        self.bbb_socket.close()


# Sample use of class Server
if __name__ == "__main__":
    s = Server()
    s.start_server()
    while True:
        try:
            s.connect_to_client()
        except socket.timeout:
            break
        while True:
            data = s.receive_from_client()
            if not data:  # Empty string indicates client is ready to close connection
                break
            # TODO: parse json into a dictionary
            # TODO: call BBB IO functions to output/read data
            # TODO: parse collected data into json
            # TODO: send json back to client
            s.send_to_client(data)  # Temporarily just sends back what was received
        s.disconnect_from_client()
    s.close_server()
