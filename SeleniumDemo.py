import bs4
from selenium import webdriver 
import time

#Loads Chromedriver
browser = webdriver.Chrome("C:/Users/addis/OneDrive/Desktop/chromedriver_win32/chromedriver.exe")


#Gets Total administered CSV
def getAdmin():
   
    #Gets the webpage
    browser.get('https://covid.cdc.gov/covid-data-tracker/#vaccinations')

    #sleeps so that the other code has time to execute
    time.sleep(10)

    #Clicks Proper Radio Buttons on webpage for total admin csv

    AViewRadioButton = browser.find_element_by_css_selector('#view-radio-Doses_Administered')
    AViewRadioButton.click()

    AShowRadioButton =  browser.find_element_by_css_selector('#show-radio-Doses_Administered')
    AShowRadioButton.click()

    AMetricRadioButton = browser.find_element_by_css_selector('#count-radio-count-total')
    AMetricRadioButton.click()

    APopRadioButton = browser.find_element_by_css_selector('#population-radio-total')
    APopRadioButton.click()

    #clicks the table toggle to access download button
    elem = browser.find_element_by_css_selector('#vaccinations-table-header-icon')
    elem.click()

    #Clicks Download button to get CSV
    buttonElemAdmin = browser.find_element_by_css_selector('#btnVaccinationsExport')
    buttonElemAdmin.click()
    



# Downloads Total Delivered CSV
def getDeliv():

    #get URL Page

    browser.get('https://covid.cdc.gov/covid-data-tracker/#vaccinations')
    time.sleep(10)
    #Sleep so the program can finish executing




    #Click proper radio buttons to select total delivered CSV
    DViewRadioButton = browser.find_element_by_css_selector('#view-radio-Doses_Administered')
    DViewRadioButton.click()

    DShowRadioButton =  browser.find_element_by_css_selector('#show-radio-Doses_Distributed')
    DShowRadioButton.click()

    DMetricRadioButton = browser.find_element_by_css_selector('#count-radio-count-total')
    DMetricRadioButton.click()

    #Get the selector for table toggle and click
    
    elemDeliv = browser.find_element_by_css_selector('#vaccinations-table-header-icon')
    elemDeliv.click()

    #get the selector for download button anc click

    elemDelivButton = browser.find_element_by_css_selector('#btnVaccinationsExport')
    elemDelivButton.click()

getAdmin()
getDeliv()








