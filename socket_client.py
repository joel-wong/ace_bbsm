import socket
import BBSM_CONSTANTS
import message


class Client:
    bbb_socket = None

    def connect_to_bbb(self):
        self.bbb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bbb_socket.connect((BBSM_CONSTANTS.HOST, BBSM_CONSTANTS.PORT))

    def send_json_to_bbb(self, json_to_send):
        message.send_msg(self.bbb_socket, json_to_send)

    def receive_json_from_bbb(self):
        data = message.recv_msg(self.bbb_socket)
        return data

    def disconnect_from_bbb(self):
        self.bbb_socket.shutdown(socket.SHUT_RDWR)
        self.bbb_socket.close()


# Sample use of class Client
'''
jstring = "Hello"
c = Client()
c.connect_to_bbb()
c.send_json_to_bbb(jstring)
received_jstring = c.receive_json_from_bbb()
c.disconnect_from_bbb()
'''
