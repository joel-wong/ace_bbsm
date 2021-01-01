def send_msg(sock, msg):
    msg_len = len(msg)
    encoded_msg_len = msg_len.to_bytes(BBSM_CONSTANTS.MESSAGE_PREFIX_LENGTH, 'big')
    # Send message length
    sent = sock.send(encoded_msg_len)
    if sent != BBSM_CONSTANTS.MESSAGE_PREFIX_LENGTH:
        raise RuntimeError("sending error, not all packets sent")
    socket_output_file_handle = sock.makefile('w')
    socket_output_file_handle.write(msg)
    socket_output_file_handle.close()


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = sock.recv(BBSM_CONSTANTS.MESSAGE_PREFIX_LENGTH)
    if not raw_msglen:
        return None
    msg_len = int.from_bytes(raw_msglen, 'big')
    # Receive the number of bytes indicated by the message length
    socket_input_file_handle = sock.makefile('r')
    msg = socket_input_file_handle.read(msg_len)
    socket_input_file_handle.close()
    # Return full message in String form
    return msg
