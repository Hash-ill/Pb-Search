# Pb-Leak
Simple OSINT command line tool for pastebin

# Description

This tool use API of https://psbdmp.ws/ . This is a simple database of leak on pastebin.
We just provide the pastebin url, you have to open url in you browser.
You can search email, domain or general term.
Please, be kind, avoid to use it for an offensive purpose.

# Usage

This tool work under python3.

First, install packages:

```sudo pip3 install -r requirements.txt```

Then,to know the different options:

```
python3 Pb-Leak.py -h
.______   .______           __       _______     ___       __  ___ 
|   _  \  |   _  \         |  |     |   ____|   /   \     |  |/  / 
|  |_)  | |  |_)  |  ______|  |     |  |__     /  ^  \    |  '  /  
|   ___/  |   _  <  |______|  |     |   __|   /  /_\  \   |    <   
|  |      |  |_)  |        |  `----.|  |____ /  _____  \  |  .  \  
| _|      |______/         |_______||_______/__/     \__\ |__|\__\ 
                                                                   
credit: Hash-ill
Please avoid to use it for an offensive purpose.
usage: paster.py [-h] [-e EMAIL] [-d DOMAIN] [-g GENERAL] [-o]

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        To search for an email on psbdmp
  -d DOMAIN, --domain DOMAIN
                        To search for domain on psbdmp
  -g GENERAL, --general GENERAL
                        To search keyword on psbdmp
  -o, --output          create file with pastebin url output
```
