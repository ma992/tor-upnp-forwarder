# tor-upnp-forwarder
This python script will connect to a local Tor process, then use UPnP to forward ports on a router.
It requires miniupnpc and stem:
pip install miniupnpc stem

To use it, add a crontab entry:
* *	* * *	root	/path/to/script/tor_upnp_forwarder.py [controlport]

The [controlport] should be replaced with the controlport of the Tor process, usually 9051.
