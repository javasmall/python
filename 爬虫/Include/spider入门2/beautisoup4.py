from bs4 import BeautifulSoup
import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
#soup.find(text=正则表达)
print(soup.find_all(text=re.compile('Hello')))
