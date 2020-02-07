#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os,re

#plays 2048

#left, down, right, down repeat
def movement():
    ActionChains(browser).send_keys(Keys.DOWN).perform()
    ActionChains(browser).send_keys(Keys.LEFT).perform()
    ActionChains(browser).send_keys(Keys.DOWN).perform()
    ActionChains(browser).send_keys(Keys.RIGHT).perform()
def moveUp():
    ActionChains(browser).send_keys(Keys.UP).perform()
def getScore():
    num=browser.find_element_by_class_name("score-container")
    score=num.text
    return scorefilter.search(score).group()

browser=webdriver.Firefox()

#wait=WebDriverWait(browser,15)
scorefilter=re.compile(r'\d+')
count=0
#for i in range(5):
browser.get('https://play2048.co/')
while 1:
    try:
        browser.find_element_by_class_name('mailing-list-email-field').click()
        print('Score: '+s2)
        break
    except:
        s1=getScore() #if moved and score didn't change
        movement()
        s2=getScore()
        #3 failures to move in a row means stuck
        if s1==s2:
            count+=1
        else:
            count=0
        if count==3:
            moveUp()
#take screenshot of score if it better than highscore maybe
browser.close()
os.system("taskkill /im geckodriver.exe /f")

