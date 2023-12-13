from selenium.webdriver.common.by import By


def kogo(driver):
    element = driver.find_element(By.XPATH, '//a[@data-do="show_who_mentioned_ads"]')
    element.click()
