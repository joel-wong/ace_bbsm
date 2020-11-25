import socket
import BBSM_CONSTANTS
import message


class Server:
    bbb_socket = None
    connection = None
    address = None

    def connect_to_client(self):
        self.connection, self.address = self.bbb_socket.accept()
        print('Connected by', self.address)

    def communicate_with_client(self):
        while True:
            data = message.recv_msg(self.connection)
            if not data:  # Empty string indicates client is ready to close connection
                break
            # TODO: parse json into a dictionary
            # TODO: call BBB IO functions to output/read data
            # TODO: parse collected data into json
            # TODO: send json back to client
            message.send_msg(self.connection, data)  # Temporarily just sends back what was received

    def disconnect_from_client(self):
        self.connection.close()

    def start_server(self):
        self.bbb_socket = socket.create_server((BBSM_CONSTANTS.HOST, BBSM_CONSTANTS.PORT))
        self.bbb_socket.listen()
        if BBSM_CONSTANTS.ALLOW_SERVER_TIMEOUT:
            self.bbb_socket.settimeout(BBSM_CONSTANTS.SERVER_TIMEOUT)
        while True:
            try:
                self.connect_to_client()
            except socket.timeout:
                break
            self.communicate_with_client()
            self.disconnect_from_client()

    def close_server(self):
        self.bbb_socket.close()


# Sample use of class Server
'''
s = Server()
s.start_server()
s.close_server()
'''
