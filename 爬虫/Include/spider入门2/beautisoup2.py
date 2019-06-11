#find_all(name , attrs , recursive , text , **kwargs)
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
#元组
#print(soup.find_all(name='ul')[1])
#print(type(soup.find_all(name='ul')[0]))
#可以进行多次嵌套
for ul in soup.find_all(name='ul'):
   print(ul.find_all(name='li')[0])
    # for li in ul.find_all(name='li'):
    #     print(li)
