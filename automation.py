from selenium import webdriver
import csv
import time
import requests

with open('Quiz.csv') as t:
    q=csv.DictReader(t)
    company=[]
    street=[]
    city=[]
    st=[]
    zipcode=[]
    for line in q:
        c=(line['Company'])
        company.insert(-1,c)
        s=(line['Street'])
        street.insert(-1,s)
        ci=(line['City'])
        city.insert(-1,ci)
        sti=(line['St'])
        st.insert(-1,sti)
        z=(line['ZIPCode'])
        zipcode.insert(-1,z)

driver=webdriver.Chrome('C:/Users/bhara/OneDrive/Desktop/python/chromedriver.exe')

driver.get('https://tools.usps.com/zip-code-lookup.htm?byaddress')




#Xpath
xCompany='//*[@id="tCompany"]'
xstreet='//*[@id="tAddress"]'
xcity='//*[@id="tCity"]'
xst='//*[@id="tState"]'
xzip='//*[@id="tZip-byaddress"]'
Find='//*[@id="zip-by-address"]'

k=0
while k<len(company):

    driver.find_element_by_xpath(xCompany).send_keys(company[k])
    driver.find_element_by_xpath(xstreet).send_keys(street[k])
    driver.find_element_by_xpath(xcity).send_keys(city[k])
    driver.find_element_by_xpath(xst).send_keys(st[k])
    driver.find_element_by_xpath(xzip).send_keys(zipcode[k])
    driver.find_element_by_xpath(Find).click()


    k=k+1
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="zip-lookup-app"]/div/div[1]/div/ul/li[1]/a/span').click()
    time.sleep(3)
driver.quit()