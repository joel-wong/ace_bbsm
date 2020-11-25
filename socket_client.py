import socket
import BBSM_CONSTANTS


class Client:
    bbb_socket = None

    def connect_to_bbb(self):
        self.bbb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bbb_socket.connect((BBSM_CONSTANTS.HOST, BBSM_CONSTANTS.PORT))

    def send_json_to_bbb(self, json_to_send):
        self.bbb_socket.sendall(bytes(json_to_send, 'utf-8'))

    def receive_json_from_bbb(self):
        data = self.bbb_socket.recv(BBSM_CONSTANTS.MAX_FILE_SIZE)
        return data

    def disconnect_from_bbb(self):
        self.bbb_socket.sendall(bytes("", 'utf-8'))  # Send empty string to indicate connection can be terminated
        self.bbb_socket.close()


# Sample use of class Client
'''
jstring = "hi"
c = Client()
c.connect_to_bbb()
c.send_json_to_bbb(jstring)
jstring_received = c.receive_json_from_bbb()
c.disconnect_from_bbb()
'''
