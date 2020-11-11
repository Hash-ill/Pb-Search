import requests
import argparse
import re
import os

def Pastebin_search(search,object):#this function provide search on psbdmp
    #search = string, subject of the search
    #object = string, the object to search
    #Data = dict, contain all the API response
        try:
            url="https://psbdmp.ws/api/search/{}/{}".format(search,object)#formatage de la requete api
            response = requests.get(url)
            data=response.json()#contact api with formated request
            if data['count']==0: #in case of response without data
                print("nothing found for :"+object+"")
                exit()
            else:#if informations are found on psbdmp
                for i in range(len(data['data'])):
                    print("https://pastebin.com/"+data['data'][i]['id']+"")
                print('Un leak potentiel existe pour:'+object+'')
                for i in range(len(data['data'])):
                    print("https://pastebin.com/"+data['data'][i]['id']+"")#display url where the information is found
                print('Ces informations ne sont pas forcement accessible ')
                return Data
        except Exception as e:
            print("nous avons une erreur lors de la recherche")

def output(Id,Data,Info):
    if not os.path.exists(Id):#verify the existence of folder
        os.makedirs(Id)
    for i in range(len(Data['data'])):#write in a file every url which are found by psbdmp
        with open(str(""+Id+"/"+Info+".txt"),"a") as f:
            f.write("https://pastebin.com/"+Data['data'][i]['id']+"\n")
    f.close()


if __name__ == '__main__':
    print(".______      ___           _______.___________. _______ .______")
    print("|   _  \    /   \         /       |           ||   ____||   _  \ ")
    print("|  |_)  |  /  ^  \       |   (----`---|  |----`|  |__   |  |_)  |")
    print("|   ___/  /  /_\  \       \   \       |  |     |   __|  |      /")
    print("|  |     /  _____  \  .----)   |      |  |     |  |____ |  |\  \----.")
    print("| _|    /__/     \__\ |_______/       |__|     |_______|| _| `._____|")
    print("credit: Hash-ill")
    print("Please avoid to use it for an offensive purpose.")
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="To search for an email on psbdmp")
    parser.add_argument("-d", "--domain", help="To search for domain on psbdmp")
    parser.add_argument("-g", "--general", help="To search keyword on psbdmp")
    parser.add_argument("-o","--output", help="create file with pastebin url output", action="store_true")
    args = parser.parse_args()
    if args.email:
        if re.match(r"[^@]+@[^@]+\.[^@]+", args.email):#verification of email format
            if args.output:
                Data=Pastebin_search("email",args.email)
                output(str("Mail"),Data,args.email)
            else:
                Pastebin_search("email",args.email)
        else:
            print("please enter an email")
    if args.domain:
        if re.match(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]", args.domain):#verification of domain format
            if args.output:
                Data=Pastebin_search("domain",args.domain)
                output("Domain",Data,args.domain)
            else:
                Pastebin_search("domain",args.domain)
        else:
            print("please enter a domain name")
    if args.general:
        if args.output:
            Data=Pastebin_Search("general",args.general)
            output(str("general"),Data,args.general)
        else:
            Pastebin_Search("general",args.general)
