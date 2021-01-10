HOST = 'beaglebone.local'  # Beagle Bone Black hostname when connected to your LAN via ethernet
PORT = 65432  # Port to listen on, this can be any arbitrary private port between 49152 and 65535
ALLOW_SERVER_TIMEOUT = False  # implements server timeout
SERVER_TIMEOUT = 20  # If no client connects within this timeframe (seconds), server closes.
                     # Ignored if ALLOW_SERVER_TIMEOUT = False
