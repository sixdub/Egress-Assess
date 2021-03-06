#!/bin/bash

clear
echo "[*] Installing pyftpdlib..."
git clone https://github.com/giampaolo/pyftpdlib.git
cd pyftpdlib
python setup.py install
cd ..
rm -rf pyftpdlib
cd ..
clear
echo "[*] Generating SSL Certificate"
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
echo
echo "[*] Install complete!"
