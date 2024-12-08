# Importa a biblioteca Selenium para automação de navegador
from selenium import webdriver
# Para configurar opções do navegador Chrome
from selenium.webdriver.chrome.options import Options
# Para localizar os elementos na página
from selenium.webdriver.common.by import By
# Para esperar a visibilidade dos elementos
from selenium.webdriver.support.ui import WebDriverWait
# Para condições esperadas, como a visibilidade dos elementos
from selenium.webdriver.support import expected_conditions as EC
import time  # Importa a biblioteca time para usar o tempo de espera

# Função para aguardar a visibilidade de um elemento específico


def aguardar_elemento(navegador, localizador, tempo=10):
    """
    Aguarda até que o elemento especificado seja visível na página.
    :param navegador: O objeto do navegador controlado pelo Selenium
    :param localizador: O localizador usado para encontrar o elemento (pode ser By.CLASS_NAME, By.LINK_TEXT, etc.)
    :param tempo: O tempo máximo de espera, em segundos (padrão é 10 segundos)
    """
    return WebDriverWait(navegador, tempo).until(
        # Espera o elemento ficar visível
        EC.visibility_of_element_located(localizador)
    )


# Configurar as opções do navegador Chrome
chrome_options = Options()  # Cria uma instância de opções para o Chrome
# Desativa o uso da GPU para melhorar a performance (útil em máquinas sem GPU)
chrome_options.add_argument("--disable-gpu")

# Inicializa o navegador Chrome com as opções configuradas
navegador = webdriver.Chrome(options=chrome_options)

# Acessa o site da Magazine Luiza
navegador.get("https://ri.magazineluiza.com.br/")

# Maximiza a janela do navegador para garantir que todos os elementos fiquem visíveis
navegador.maximize_window()

# Espera até que o botão "Informações Financeiras" esteja visível na página
aguardar_elemento(navegador, (By.CLASS_NAME, "page"))

# Encontra todos os elementos com a classe "page" na página e procura pelo botão com o texto "Informações Financeiras"
botoes = navegador.find_elements(By.CLASS_NAME, "page")
for botao in botoes:  # Loop para percorrer todos os elementos encontrados
    if "Informações Financeiras" in botao.text:  # Verifica se o botão contém o texto desejado
        botao.click()  # Clica no botão "Informações Financeiras"
        break  # Interrompe o loop após clicar no botão

# Espera até que o link "Planilha de Resultado" esteja visível e clica nele
aguardar_elemento(navegador, (By.LINK_TEXT, "Planilha de Resultado"))
planilha_link = navegador.find_element(By.LINK_TEXT, "Planilha de Resultado")
planilha_link.click()  # Clica no link para acessar a planilha de resultados

# Espera até que o link "Planilha de Resultados Trimestrais" esteja visível e clica nele para iniciar o download
aguardar_elemento(
    navegador, (By.LINK_TEXT, "Planilha de Resultados Trimestrais"))
download_planilha = navegador.find_element(
    By.LINK_TEXT, "Planilha de Resultados Trimestrais")
download_planilha.click()  # Clica no link para baixar a planilha trimestral

# Pausa por 3 segundos para garantir que o download seja iniciado antes de fechar o navegador
time.sleep(3)
