#!/usr/bin/env python
# Based on wrapper.py

import sys
import json
import socket

def query_icedove():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('localhost', 3411))
		reply = s.recv(8192)
		s.close()
		obj = json.loads(reply)
		cnt = 0;
		for accoutns in obj:
			cnt = cnt + accoutns['unread']
		if cnt == 0:
			return ['No new mail', '#ffffff']
		else:
			return ['Have new mail', '#ffff00']
	except Exception as e:
		return ['Mailer offline', '#ff0000']

def print_line(msg):
	sys.stdout.write(msg + '\n')
	sys.stdout.flush()

def read_line():
	try:
		line = sys.stdin.readline().strip();
		if not line:
			sys.exit(3);
		return line
	except KeyboardInterrupt:
		sys.exit()

if __name__ == '__main__':
	# {"version" : 1}
	print_line(read_line())
	# [
	print_line(read_line())

	while True:
		line, prefix = read_line(), ''
		if line.startswith(','):
			line, prefix = line[1:], ','

		j = json.loads(line)
		mail = query_icedove()
		j.insert(0, {'full_text' : mail[0], 'color' : mail[1], 'name' : 'icedove'})
		
		print_line(prefix + json.dumps(j));
