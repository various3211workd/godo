# -*- coding: utf-8 -*-
import sys
from googlesearch import search

def google_search(query):
    
    # read database query
    #db_data = open('db/sql_injection_list.txt', 'r')

    # debug
    search_data = query# + ' /lire.php?rub='
    print(search_data)
    
    #iterable = search(search_data, pause=4.0, num=1, user_agent="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)")
    iterable = (i for i in [])
    
    if next(iterable, None) is None:
        print('Not initiated')
        
"""
    for data in db_data:
        search_data = query + ' ' + data
        if not search(search_data, pause=4.0, num=1, user_agent="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"):
            print("無いよ")
        else:
            print(search_data)
"""

def main():
    args = sys.argv

    if len(args) == 2:
        search_site = "site:" + args[1]
        google_search(search_site)
        #google_search("inurl:wp-config.php")
    else:
        print("[USAGE] python godo.py <site_name>")

if __name__ == '__main__':
    main()