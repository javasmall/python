from selenium import webdriver
import time
import random
browser = webdriver.PhantomJS()

browser.get('https://www.baidu.com')
time.sleep(2)

for i in range(200):
  try:
    time.sleep(5)
    browser.get('https://www.wenjuan.com/s/2Uf6Fbe/')
    sex=browser.find_elements_by_css_selector("a[rel='question_5bfe34cd92beb5077b5fdaec']")
    index=random.randint(1,5)
    if index<3:
        sex[1].click()
    else:
        sex[0].click()
    time.sleep(0.5)
    grade=browser.find_elements_by_css_selector("a[rel='question_5bfe34cd92beb5077b5fdaed']")
    #index=random.randint(0,3)
    grade[2].click()
    time.sleep(0.5)
    istanguo=browser.find_elements_by_css_selector("a[rel='question_5bfe34ce92beb5077b5fdaee']")
    index=random.randint(1,10)
    if index>6:
        istanguo[0].click()
    else:
        istanguo[1].click()
    tiaojian=browser.find_elements_by_css_selector("a[rel='question_5bfe34ce92beb5077b5fdaf1']")
    index=random.randint(1,13)
    if index<=6:
        tiaojian[0].click()
    index = random.randint(1, 13)
    if index<=6:
        tiaojian[1].click()
    index = random.randint(1, 13)
    if index <= 3:
        tiaojian[2].click()
    if index<=8:
        tiaojian[3].click()
    index = random.randint(1, 13)
    if index<=3:
        tiaojian[4].click()
    index = random.randint(1, 13)
    if index <= 7:
        tiaojian[5].click()
    if index<=6:
        tiaojian[6].click()
    index = random.randint(1, 13)
    if index<=9:
        tiaojian[7].click()
    index = random.randint(1, 13)
    if index <= 9:
        tiaojian[8].click()
    if index<=2:
        tiaojian[9].click()
    index = random.randint(1, 13)
    if index<=2:
        tiaojian[10].click()
    index = random.randint(1, 16)
    if index <= 2:
        tiaojian[11].click()
    index = random.randint(1, 13)
    if index <= 8:
        tiaojian[12].click()
    age= browser.find_elements_by_css_selector("a[rel='question_5bfe34ce92beb5077b5fdaf4']")
    index=random.randint(0,100)
    if index<50:
        age[0].click()
    elif index>65:
        age[2].click()
    else:
        age[1].click()
    time.sleep(0.5)
    yingxiang=browser.find_elements_by_css_selector("a[rel='question_5bfe34ce92beb5077b5fdafb']")
    index=random.randint(1,10)
    jud=False
    if(index<=4):
        yingxiang[0].click()
        jud=True
    index = random.randint(1, 10)
    if (index <= 2):
        yingxiang[1].click()
        jud = True
    index = random.randint(1, 10)
    if (index <= 6):
        jud = True
        yingxiang[2].click()
    index = random.randint(1, 10)
    if (index <= 8):
        yingxiang[3].click()
        jud = True
    index = random.randint(1, 10)
    if (index <= 5):
        yingxiang[4].click()
        jud = True
    if jud==False:#防止运气不好一个没选上
        yingxiang[2].click()
    time.sleep(0.3)
    jichu=browser.find_elements_by_css_selector("a[rel='question_5bfe34ce92beb5077b5fdafd']")
    index=random.randint(0,100)
    if index<64:
        jichu[1].click()
    elif index>98:
        jichu[2].click()
    else:
        jichu[0].click()

    time.sleep(0.5)
    jiehun=browser.find_elements_by_css_selector("a[rel='question_5bfe395992beb5238625321e']")
    index=random.randint(0,100)
    if index<65:
        jiehun[2].click()
    elif index>98:
        jiehun[0].click()
    elif index>=65 and index<=83:
        jiehun[3].click()
    else:
        jiehun[1].click()
    browser.find_element_by_id("next_button").click()
  except Exception as e:
      print(e)

#input.clear()
#button = browser.find_element_by_class_name('btn-search')
#button.click()