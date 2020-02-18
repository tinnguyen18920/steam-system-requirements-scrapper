#python 3.8
""""""
import requests
from bs4 import BeautifulSoup

import config


def scrape_all_app_id(page,f):  
    """Scrape all appid of Steam game to a text file with filters""" 

    #max page: 1387
    url = "https://store.steampowered.com/search/results?\
    sort_by=Released_DESC&category1=998&os=win&page=%s" % page
    r = requests.get(url,headers=config.HEADERS)
    if r.ok:
        response = r.text
        soup = BeautifulSoup(response,"html.parser")
        apps = soup.findAll("a",{"class":"search_result_row ds_collapse_flag"})
        for app in apps:
            f.write(app['data-ds-appid']+"\n")
            print(app['data-ds-appid'])
            
def main():
    f = open("apps_id2.txt","w")
    for i in range(1,1388):
        scrape_all_app_id(str(i),f)
if __name__ == "__main__":
    main()