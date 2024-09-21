from os import system
from sys import argv
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def get_page_source(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        page = browser.new_page()
        
        page.goto(url)
        
       
        page_source = page.content()
        
        browser.close()
        
        return page_source
down_repos=[0]
p=1
while p<100:

    url = f'https://github.com/search?q={argv[1]}&type=repositories&p={p}'  
    page_source = get_page_source(url)
    # print(page_source)
    soup=BeautifulSoup(page_source,"html.parser")
    repos=soup.find_all("a")
    for repo in repos:
        repo_finder=repo.get("class"
                            )
        if "dIlPa" in  repo_finder:
            #  print("https://github.com/"+repo.get("href")+"\n")
            down_repos.append("https://github.com/"+repo.get("href"))
    down_repos.append("next page")
    print(down_repos)
    for i in  range(1,len(down_repos)):
        print(i,".",down_repos[i])
        # print(repo_finder)
        # print(f'Link: {href}, Text: {text}')
    num=input("adad repo ra vared konid:")
    for i in  range(1,len(down_repos)):
        if i==int(num):
            system(f"git clone  {down_repos[i]}")
            
        if num==down_repos[-1]:
            break
        else:
            continue
    p=p+1
    if num==down_repos[-1]:
        continue
    else:
        break