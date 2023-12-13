from selenium.webdriver.common.by import By


def click_with_reposts(driver):
    driver.execute_script("window.scrollTo(0, 800)")

    element = driver.find_element(By.XPATH, '//div[@id="portlet_who_mentioned"]')
    element_2 = element.find_element(By.CSS_SELECTOR, 'label')
    element_2.click()
