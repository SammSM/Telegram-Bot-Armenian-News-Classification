from selenium import webdriver
from selenium.webdriver.common.by import By

import json
import time

driver = webdriver.Chrome()
driver.maximize_window()

news = ['Քաղաքական', 'Հասարակական', 'Կրթական', 'Առոջապահական']
news_links = ['#menu-item-56 > a', '#menu-item-52 > a', '#menu-item-104622 > a', '#menu-item-104614 > a']
news_article = {
    'Քաղաքական': [], 
    'Հասարակական': [], 
    'Կրթական': [], 
    'Առոջապահական': []
}

try:
    driver.get(url = 'https://168.am/')
    time.sleep(2)
    
    for n in range(0, len(news)):
        driver.find_element(By.CSS_SELECTOR, news_links[n]).click()
        time.sleep(2)
        for p in range(3, 14, 2):
            for a in range(3, 25):
                article = driver.find_element(By.CSS_SELECTOR, f'body > div.container > div.container.pt-3 > div.row > div.col.col-md-8 > div > div:nth-child({a}) > a > div.related-title > div > p').text
                news_article[news[n]].append(article)
            driver.find_element(By.CSS_SELECTOR, f'#wp_page_numbers > ul > li:nth-child({p}) > a')

except Exception as ex:
    print(ex.__class__.__name__)

finally:
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(news_article, file, ensure_ascii=False, indent=4)

    driver.close()
    driver.quit()