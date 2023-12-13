from selenium.webdriver.common.by import By


def kto(driver):
    element = driver.find_element(By.XPATH, '//a[@data-do="show_who_mentioned"]')
    element.click()
