import BBSM_CONSTANTS


def send_msg(sock, msg):
    msg_len = len(msg)
    socket_output_file_handle = sock.makefile('w')
    socket_output_file_handle.write(str(msg_len) + "\n" + msg)
    socket_output_file_handle.close()


def recv_msg(sock):
    socket_input_file_handle = sock.makefile('r')
    first_input = socket_input_file_handle.readline()
    if first_input != "":
        try:
            msg_len = int(first_input)
            msg = socket_input_file_handle.read(msg_len)
        except ValueError:
            # expected the length of the msg to be the first_input, but did
            # not receive an integer value
            # return an empty string, indicating that the connection should
            # be terminated
            msg = ""
    else:
        # socket has been closed
        # connection should be terminated
        msg = ""
    socket_input_file_handle.close()
    # Return full message in String form
    return msg
