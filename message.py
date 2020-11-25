import BBSM_CONSTANTS
import math


def send_msg(sock, msg):
    # Prefix each message with a 4-byte length, encode message in ASCII
    encoded_msg = msg.encode('ASCII')
    msg_len_prefix = len(encoded_msg).to_bytes(BBSM_CONSTANTS.MESSAGE_PREFIX_LENGTH, 'big')
    # Send prefixed message
    sock.sendall(msg_len_prefix + encoded_msg)


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = sock.recv(BBSM_CONSTANTS.MESSAGE_PREFIX_LENGTH)
    if not raw_msglen:
        return None
    msg_len = int.from_bytes(raw_msglen, 'big')
    # Receive the number of bytes indicated by the message length
    msg = ""
    for i in range(math.ceil(msg_len/BBSM_CONSTANTS.RECEIVE_BUFFER_SIZE)):
        fragment = sock.recv(BBSM_CONSTANTS.RECEIVE_BUFFER_SIZE).decode("ASCII")
        msg = msg + fragment
    # Return full message in String form
    return msg
