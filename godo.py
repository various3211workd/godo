# -*- coding: utf-8 -*-
import sys
from googlesearch import search

def google_search(query, limit=10):
    for url in search(query, pause=4.0, num=limit, user_agent="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"):
        print(url)

def main():
    args = sys.argv

    if len(args) != 2:
        print("[USAGE] python godo.py <site_name>")
        exit()

    search_site = args[1]
    #google_search("inurl:wp-config.php")

if __name__ == '__main__':
    main()