import time
from selenium.webdriver.common.by import By

def test_login_nok(driver): # Entrada Inválida
    driver.get("https://bugbank.netlify.app/")
    driver.find_element(By.NAME, "email").send_keys("admin@email.com")
    driver.find_element(By.NAME, "password").send_keys("adminn")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text == "Usuário ou senha inválido.\nTente novamente ou verifique suas informações!"

def test_login_com_saldo_ok(driver): # Caminho Feliz
    driver.get("https://bugbank.netlify.app/")
    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("pedro@email.com")
    driver.find_element(By.NAME, "name").send_keys("Pedro Gouveia")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("pedro123")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("pedro123")
    driver.find_element(By.XPATH , '//*[@id="toggleAddBalance"]').click()
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("pedro@email.com")
    driver.find_element(By.NAME, "password").send_keys("pedro123")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 1.000,00")

def test_login_sem_saldo_ok(driver): # Caminho Alternativo
    driver.get("https://bugbank.netlify.app/")
    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("joao@email.com")
    driver.find_element(By.NAME, "name").send_keys("João Silva")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("joao123")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("joao123")
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("joao@email.com")
    driver.find_element(By.NAME, "password").send_keys("joao123")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click() 
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 0,00")
