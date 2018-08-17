import time
import csv
from bs4 import BeautifulSoup
import sys, io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# @author Nahida Sultana Chowdhury <nschowdh@iu.edu>
#additionally add CSV file method here...

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
chromedriver_loc = "/home/mitu/Desktop/gcrawlertest/my_crawler/env/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver_loc)
wait = WebDriverWait( driver, 10 )

# Append your app store urls here
urls = ["https://www.amazon.com/Panasonic-ErgoFit-Headphones-Controller-RP-TCM125-K/dp/B00E4LGVUO/ref=pd_rhf_dp_p_img_2?_encoding=UTF8&psc=1&refRID=0Q53Z1ZPSND28MKVKBE5"
]
appCounter = 0
for url in urls:
    #print(url)
    time.sleep(1)
    try:
        driver.get(url)
        driver.maximize_window()
        
        page = driver.page_source
        
        soup_expatistan = BeautifulSoup(page, "html.parser")
        xpath_title   = './/a[@data-hook="review-title"]//text()'
        expatistan_table = soup_expatistan.find("span", class_="a-size-large")
        productName = expatistan_table.string.strip()
        print("product name: ", productName)
        myFile = open('/home/mitu/Desktop/gcrawlertest/my_crawler/env/bin/amazon_rev.csv',"w")
        with myFile:
            writer = csv.writer(myFile)
            try:
                see_all_reviews_button = driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')

                see_all_reviews_button.click()
                time.sleep(10)

                #Reviews extract for the first page
                reviews_div = driver.find_element_by_xpath('//*[@id="a-page"]/div[3]/div[1]/div[2]/div/div[1]/div[3]').get_attribute("innerHTML")
                soup_expatistan = BeautifulSoup(reviews_div, "html.parser") 
                expand_pages = soup_expatistan.find_all("div", class_="a-section celwidget")
                for expand_page in expand_pages:
                    ind_rev = expand_page.find("span", class_="a-size-base review-text")
                    ind_rev_date = expand_page.find("span", class_="a-size-base a-color-secondary review-date")
                    csvRow = [ind_rev_date.text.encode("utf8"), ind_rev.text.encode("utf8")]
                    writer.writerow(csvRow)
                    #print(ind_rev)
                time.sleep(5)
                
                #Reviews extract for the rest of the n pages
                for i in range(0,5): #n = 5
                    if (i<3):
                        next_button = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[8]/a')
                    else:
                        next_button = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[9]/a')
                    try:
                        next_button.click()
                        reviews_div = driver.find_element_by_xpath('//*[@id="a-page"]/div[3]/div[1]/div[2]/div/div[1]/div[3]').get_attribute("innerHTML")
                        soup_expatistan = BeautifulSoup(reviews_div, "html.parser") 
                        expand_pages = soup_expatistan.find_all("div", class_="a-section celwidget")
                        for expand_page in expand_pages:
                            ind_rev = expand_page.find("span", class_="a-size-base review-text")
                            ind_rev_date = expand_page.find("span", class_="a-size-base a-color-secondary review-date")
                            csvRow = [ind_rev_date.text.encode("utf8"), ind_rev.text.encode("utf8")]
                            writer.writerow(csvRow)
                            #print(ind_rev)
                        time.sleep(10)
                        #ind_rev_date = expand_page.find("div", class_="UD7Dzf")
                        time.sleep(5)
                    except Exception:
                        time.sleep(1)

                print(i)
            except Exception:
                time.sleep(1)
        myFile.close()
    except Exception:
        time.sleep(1)
driver.quit()


