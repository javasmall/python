
import requests
url='https://weiliicimg9.pstatp.com/weili/ms/57436992794921884.webp'
url2='https://icweiliimg9.pstatp.com/weili/ms/256690017602371867.webp'
r=requests.get(url)
print(r.status_code)
with open('/img/bizhi.jpg', 'wb') as f:
    f.write(r.content)
