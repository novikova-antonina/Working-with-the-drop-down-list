from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def main():
    driver = webdriver.Chrome()
    try:
        driver.get("https://suninjuly.github.io/selects1.html")

        num1 = int(driver.find_element(By.ID, "num1").text)
        num2 = int(driver.find_element(By.ID, "num2").text)
        result = num1 + num2

        select = Select(driver.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(result))

        driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        input("Нажмите Enter для закрытия браузера...")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
