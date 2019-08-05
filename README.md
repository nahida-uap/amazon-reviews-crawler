# amazon-reviews-crawler

This is a Python based Amazon Appstore Crawler which require:

    - Python
    - Selenium (Install - pip install selenium)
    - beautifulsoup4
    - Chromedriver (need to place in the same working directory)

As Input user need to pass single or multi URL: urls = [""https://www.amazon.com/Panasonic-ErgoFit-Headphones-Controller-RP-TCM125-K/dp/B00E4LGVUO/ref=pd_rhf_dp_p_img_2?_encoding=UTF8&psc=1&refRID=0Q53Z1ZPSND28MKVKBE5"] In returns the program will retrun the following fields and will store into seperate CSV files:

    - App title
    - Review text body
    - Creation Date
    
To run the code type the following command:

    python amazonCrawler.py
