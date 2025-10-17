import time
from selenium.webdriver.common.by import By

def test_transferencia_sem_descricao_ok(driver): # Caminho Feliz
    driver.get("https://bugbank.netlify.app/")
    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click() # Cadastrar usuário sem saldo
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("pedro@email.com")
    driver.find_element(By.NAME, "name").send_keys("Pedro Gouveia")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("senhadopedro1@")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("senhadopedro1@")
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("pedro@email.com")
    driver.find_element(By.NAME, "password").send_keys("senhadopedro1@")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 0,00")
    conta = driver.find_element(By.XPATH, '//*[@id="textAccountNumber"]/span').text # Armazena o número da conta com dígito
    conta_e_digito = conta.split("-")
    driver.find_element(By.ID, "btnExit").click()

    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click() # Cadastro de outro usuário com saldo
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("joao@email.com")
    driver.find_element(By.NAME, "name").send_keys("João Silva")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("senhadojoao2")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("senhadojoao2")
    driver.find_element(By.XPATH , '//*[@id="toggleAddBalance"]').click()
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("joao@email.com")
    driver.find_element(By.NAME, "password").send_keys("senhadojoao2")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 1.000,00")

    driver.find_element(By.ID, "btn-TRANSFERÊNCIA").click() # Fazendo a transferência
    driver.find_element(By.NAME, "accountNumber").send_keys(conta_e_digito[0])
    driver.find_element(By.NAME, "digit").send_keys(conta_e_digito[1])
    driver.find_element(By.NAME, "transferValue").send_keys("100")
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("Transferencia realizada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()

def test_transferencia_com_descricao_ok(driver): # Caminho Alternativo
    driver.get("https://bugbank.netlify.app/")
    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click() # Cadastrar usuário sem saldo
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("pedro@email.com")
    driver.find_element(By.NAME, "name").send_keys("Pedro Gouveia")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("senhadopedro1@")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("senhadopedro1@")
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("pedro@email.com")
    driver.find_element(By.NAME, "password").send_keys("senhadopedro1@")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 0,00")
    conta = driver.find_element(By.XPATH, '//*[@id="textAccountNumber"]/span').text # Armazena o número da conta com dígito
    conta_e_digito = conta.split("-")
    driver.find_element(By.ID, "btnExit").click()

    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click() # Cadastro de outro usuário com saldo
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("joao@email.com")
    driver.find_element(By.NAME, "name").send_keys("João Silva")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("senhadojoao2")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("senhadojoao2")
    driver.find_element(By.XPATH , '//*[@id="toggleAddBalance"]').click()
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("joao@email.com")
    driver.find_element(By.NAME, "password").send_keys("senhadojoao2")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 1.000,00")

    driver.find_element(By.ID, "btn-TRANSFERÊNCIA").click() # Fazendo a transferência
    driver.find_element(By.NAME, "accountNumber").send_keys(conta_e_digito[0])
    driver.find_element(By.NAME, "digit").send_keys(conta_e_digito[1])
    driver.find_element(By.NAME, "transferValue").send_keys("100")
    driver.find_element(By.NAME, "description").send_keys("Transferência de 100 reais.")
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("Transferencia realizada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()

def test_transferencia_nok(driver): # Entrada Inválida
    driver.get("https://bugbank.netlify.app/")
    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click() # Cadastrar usuário sem saldo
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("pedro@email.com")
    driver.find_element(By.NAME, "name").send_keys("Pedro Gouveia")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("senhadopedro1@")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("senhadopedro1@")
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("pedro@email.com")
    driver.find_element(By.NAME, "password").send_keys("senhadopedro1@")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 0,00")
    conta = driver.find_element(By.XPATH, '//*[@id="textAccountNumber"]/span').text # Armazena o número da conta com dígito
    conta_e_digito = conta.split("-")
    driver.find_element(By.ID, "btnExit").click()

    driver.find_element(By.CSS_SELECTOR, ".ihdmxA").click() # Cadastro de outro usuário com saldo
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input').send_keys("joao@email.com")
    driver.find_element(By.NAME, "name").send_keys("João Silva")
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys("senhadojoao2")
    driver.find_element(By.NAME, "passwordConfirmation").send_keys("senhadojoao2")
    driver.find_element(By.XPATH , '//*[@id="toggleAddBalance"]').click()
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("criada com sucesso")
    driver.find_element(By.ID, "btnCloseModal").click()
    driver.find_element(By.NAME, "email").send_keys("joao@email.com")
    driver.find_element(By.NAME, "password").send_keys("senhadojoao2")
    driver.find_element(By.CSS_SELECTOR, ".otUnI").click()
    assert driver.find_element(By.ID, "textBalance").text.endswith("R$ 1.000,00")

    driver.find_element(By.ID, "btn-TRANSFERÊNCIA").click() # Fazendo a transferência
    driver.find_element(By.NAME, "accountNumber").send_keys(conta_e_digito[0])
    driver.find_element(By.NAME, "digit").send_keys(conta_e_digito[1])
    driver.find_element(By.NAME, "transferValue").send_keys("-100")
    driver.find_element(By.CSS_SELECTOR, ".CMabB").click()
    time.sleep(0.2)
    assert driver.find_element(By.ID, "modalText").text.endswith("Valor da transferência não pode ser 0 ou negativo")
    driver.find_element(By.ID, "btnCloseModal").click()
