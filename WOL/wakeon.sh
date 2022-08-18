#!/bin/bash
# Wake on LAN
if [ -n "$1" ]
then
                val=$1
fi
echo ""
echo "Wake on LAN is running..."
echo "Selected MAC-ADDRESS: ${val}"
echo ""
sudo etherwake -i eth0 ${val}
echo "The computer is now starting up!"
