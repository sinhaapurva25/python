print("hello world")
import random
import urllib.request
def download_web_image(url):
    name = random.random()
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url, full_name)
download_web_image("https://pluspng.com/img-png/png-lord-ganesh-explore-om-ganesh-lord-ganesha-and-more-1348.png")

x = range(1,5,2)
for n in x:
  print(n)

a=dict()
print(a)

def foo():
    try:
        return 1
    finally:
        return 2
    k=foo()
    print(k)

x=['a','b','c','d']
try:
    pos=x.index("geeksforgeeks")
    print(pos*3)
except Exception:
    print("Value Error")