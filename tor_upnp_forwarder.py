#!/usr/bin/env python

from stem import Signal
from stem.control import Controller
import miniupnpc
import socket
import sys

u = miniupnpc.UPnP();
u.discoverdelay = 200;

forward_dir = True;

with Controller.from_port(port = int(sys.argv[1])) as controller:
	controller.authenticate();
	try:
		lor = int(controller.get_info("net/listeners/or").strip('\"').split(':')[1]);
	except IndexError:
		print("Error when parsing response of GETINFO net/listeners/or. Relaying is likely disabled.");
		exit(1);
	try:
		ldir = int(controller.get_info("net/listeners/dir").strip('\"').split(':')[1]);
	except IndexError:
		forward_dir = False;
	u.discover();
	u.selectigd();
	print("Forwarding ORPort "+str(lor));
	bor = u.addportmapping(lor, "TCP", u.lanaddr, lor, "Tor ORPort "+str(lor), '')
	if bor:
		print("OK");
	else:
		print("Error");
	if forward_dir:
		print("Forwarding DirPort "+str(ldir));
		bdir = u.addportmapping(ldir, "TCP", u.lanaddr, ldir, "Tor DirPort "+str(ldir), '')
		if bor:
			print("OK");
		else:
			print("Error");
