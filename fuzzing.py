import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",dest="url",help="target url")
parser.add_argument("-w","--wordlist",help="wordlist")
args = parser.parse_args()
dosya = open(args.wordlist,"r")
icerik = dosya.read()
dosya.close()
for i in icerik.splitlines():
	url=args.url+str(i)
	sonuc=requests.get(url=url)
	if "200" in str(sonuc.status_code):
		print(i+" +")
	else:
		print(i+" -")