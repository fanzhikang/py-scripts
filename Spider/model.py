import requests

def getHtmlText(url):
    try:
        kv = {'wd':'python'}
        r = requests.get(url,params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
        return len(r.text)
    except:
        return "产生异常"
    
if __name__ == "__main__":
    url = "http://www.baidu.com/s"
    print(getHtmlText(url))
