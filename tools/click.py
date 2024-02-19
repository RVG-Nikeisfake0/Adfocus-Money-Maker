from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time
import math

def automate(url, threads: int = None, repeat: int = 1):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    for i in range(repeat):    
        driver.get(url)
        time.sleep(10)
        try:
            driver.find_element(By.CSS_SELECTOR, "#showSkip a.skip").click()
            wait = 2
            if threads:
                threads_wait = wait + (threads * (0.15 + (threads // 1000)))
                time.sleep(threads_wait)
            else:
                time.sleep(wait + 1.5)
        except:
            pass

def click(url, threads: int = None, repeat: int = 1):
    if threads:
        # threads wait exists to handle lag due to large amounts of chromedriver processes being spawned by threads.
        for i in range(threads):
            t = threading.Thread(target=automate, args=(url, threads, repeat))
            t.daemon = True
            t.start()
        wait = 2
        threads_wait = wait + (threads * (0.15 + (threads // 1000)))
        extra = 4.5
        time.sleep(threads_wait + extra)
        t.join()
        return t
    else:
        return automate(url, repeat=repeat)