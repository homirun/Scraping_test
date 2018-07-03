#coding:utf-8
import urllib.request
from bs4 import BeautifulSoup
def main():
    html = urllib.request.urlopen("http://gochiusa.com")
    soup = BeautifulSoup(html, "lxml")
    res = soup.find(id = "nwu_001_t").find_all("a")
    write_file(res)
    log = read_files()
    print(log)
    for i in res:
        print(i.text)
    del_file()

def del_file():
    with open("log_gochi", "w") as f:
        f.write("")

def write_file(content):
    with open("log_gochi", "a+") as f:
        for text_line in content:
            f.writelines(text_line.text+"\n")

def read_files():
    with open("log_gochi", "r+") as f:
        log = f.readlines()
        print(len(log))
        for i in range(len(log)):
            print("aaa")
            log.insert(i, log[i].replace("\n", ""))
    return log

if __name__ == "__main__":
    main()