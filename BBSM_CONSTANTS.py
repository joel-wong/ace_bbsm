# BeagleBone Black IP address when connected to your LAN via ethernet
# this can be any private IPv4 address but must be the same in both the
# ace-test-framework code (run on the computer) and in the
# ace-bbb-test-runner code (run on the BeagleBone)
HOST = '10.16.132.250'
# Port to listen on, this can be any arbitrary private port between
# 49152 and 65535
PORT = 65432
# implements server timeout
ALLOW_SERVER_TIMEOUT = False
# If no client connects within this timeframe (seconds), server closes.
# Ignored if ALLOW_SERVER_TIMEOUT = False
SERVER_TIMEOUT = 20
