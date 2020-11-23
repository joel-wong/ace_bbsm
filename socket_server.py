import socket
import bbsm_constants as bbsm


class Server:
    bbb_socket = None
    connection = None
    address = None

    def connect_to_client(self):
        self.bbb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bbb_socket.bind((bbsm.HOST, bbsm.PORT))
        self.bbb_socket.listen()
        self.connection, self.address = self.bbb_socket.accept()
        print('Connected by', self.address)

    def communicate_with_client(self):
        while True:
            data = self.connection.recv(bbsm.MAX_FILE_SIZE)
            if not data:  # Empty string indicates client is ready to close connection
                break
            # TODO: parse json into a dictionary
            # TODO: call BBB IO functions to output/read data
            # TODO: parse collected data into json
            # TODO: send json back to client
            self.connection.sendall(data)  # Temporarily just sends pack what was received

    def disconnect_from_client(self):
        self.connection.close()
        self.bbb_socket.close()


# Sample use of class Server
'''
s = Server()
s.connect_to_client()
s.communicate_with_client()
s.disconnect_from_client()
'''
