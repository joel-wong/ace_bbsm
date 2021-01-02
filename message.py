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
        # socket has been closed
        msg_len = int(first_input)
        msg = socket_input_file_handle.read(msg_len)
    else:
        msg = ""
    socket_input_file_handle.close()
    # Return full message in String form
    return msg
