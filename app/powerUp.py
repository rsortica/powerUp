# automação de cadastro de itens num formulário web

import pandas
import pyautogui

import time

pyautogui.PAUSE = 0.5
# acessar navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 

# acessar pagina "https:\\dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# fazer login
pyautogui.click(x=499, y=393)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('teste@gmail.com')

# passar para próximo campo
pyautogui.press('tab')
pyautogui.write('auto5879')
pyautogui.click(x=770, y=551)

time.sleep(3)

# ler base de dados
tabela = pandas.read_csv('produtos.csv')
#print(tabela)

# cadastrar produtos
for linha in tabela.index:

    pyautogui.click(x=499, y=279)

    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(codigo)

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo'])) 

    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.press('tab')
    pyautogui.press('enter')
    # pyautogui.scroll(5000)3000.0      


# repetir a execução para cada linha da tabela
    250.0   62.5        

    