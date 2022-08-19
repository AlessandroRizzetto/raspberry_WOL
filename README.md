<p align="center">
  <h2 align="center"> Raspberry Wake-On-LAN</h2>
  
  <p align="center">
  Alessandro Rizzetto
  </p>
 </p>
 <br>
 
 ---
 
## Table of contents

# Project Description
The goal of this project is to turn on different devices connected to a Raspberry Pi.  
This is possible thanks to a dedicated android application, connected to a python server running on the Raspberry.  



# How to Setup
## Setup a Dynamics DNS
- Head to [duckDNS](duckdns.org) and create your sub domain after logging in or creating an account.
- Click on the install tab, chose your OS (Pi in this case) and select your domain from the drop down.
- Follow the proposed tutorial paying attention to create the duckdns directory in your home.

## Server Configuration
Clone the repository and update server.py with the IP address of your Raspberry and the desired port at line 19.

```bash
git clone https://github.com/elrich2610/raspberry_WOL.git
cd raspberry_WOL
nano server.py
sudo python3 server.py
```
To run the server as a service:






- 
- 
