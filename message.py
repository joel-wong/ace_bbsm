import BBSM_CONSTANTS


def send_msg(sock, msg):
    encoded_msg = msg.encode('ASCII')
    msg_len = len(encoded_msg)
    encoded_msg_len = msg_len.to_bytes(BBSM_CONSTANTS.MESSAGE_PREFIX_LENGTH, 'big')
    # Send message length
    sent = sock.send(encoded_msg_len)
    if sent == 0:
        raise RuntimeError("socket connection broken")
    # Send message
    totalsent = 0
    while totalsent < msg_len:
        sent = sock.send(encoded_msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = sock.recv(BBSM_CONSTANTS.MESSAGE_PREFIX_LENGTH)
    if not raw_msglen:
        return None
    msg_len = int.from_bytes(raw_msglen, 'big')
    # Receive the number of bytes indicated by the message length
    msg = ""
    num_packets = msg_len // BBSM_CONSTANTS.RECEIVE_BUFFER_SIZE
    if msg_len % BBSM_CONSTANTS.RECEIVE_BUFFER_SIZE > 0:
        num_packets += 1
    for i in range(num_packets):
        fragment = sock.recv(BBSM_CONSTANTS.RECEIVE_BUFFER_SIZE).decode("ASCII")
        msg = msg + fragment
    # Return full message in String form
    return msg
