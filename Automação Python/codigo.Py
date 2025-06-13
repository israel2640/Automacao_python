import pyautogui
import time
import os
import pandas as pd
import keyboard

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Abrir o Chrome
pyautogui.hotkey("ctrl", "alt", "c")

# Seleciona o campo de busca
time.sleep(1)
pyautogui.click(x=241, y=66)

# Acessa o site de cadastro de produtos
pyautogui.write("https://israel2640.github.io/Site_de_cadastro_produto/")
pyautogui.press("enter")

# Login
time.sleep(1)
pyautogui.click(x=580, y=405)
pyautogui.write("israel@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")

# Acessa a tela de cadastro
time.sleep(1)
pyautogui.click(x=850, y=359)
pyautogui.click(x=622, y=312)

# Caminho absoluto do CSV baseado na localização do script
caminho_arquivo = os.path.join(os.path.dirname(__file__), "produtos.csv")

try:
    tabela = pd.read_csv(caminho_arquivo)
    print("✅ CSV carregado com sucesso:")
    print(tabela)
except Exception as e:
    print("❌ Erro ao ler CSV:", e)
    
# Cadastra os produtos
for linha in tabela.index:
    if keyboard.is_pressed("esc"):
        print("Execução interrompida pelo usuário (ESC).")
        break

    pyautogui.click(x=622, y=312)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    time.sleep(1)
