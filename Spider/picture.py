import requests

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1523380189712&di=f346aa919bfea923a6f0abe9a0c0ee42&imgtype=0&src=http%3A%2F%2Fimg2.iqilu.com%2Fed%2F11%2F08%2F25%2F29%2F228_110825141438_1.jpg"

path = "/home/fanzhikang/图片/爬狗.jpg"



def getPicture(url,path):
    
    r = requests.get(url)
    with open(path,"wb") as f:
        f.write(r.content)
        f.close()
        print("文件保存")
    
if __name__ == "__main__":
    getPicture(url,path)
