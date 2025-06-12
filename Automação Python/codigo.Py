import pyautogui
import time
import pandas as pd
import keyboard

pyautogui.PAUSE = 4.0
pyautogui.FAILSAFE = True  # Permite parar com o mouse no canto superior esquerdo

# Abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(4)

# Seleciona o perfil do Google
pyautogui.click(x=503, y=419)

# Seleciona o campo de busca
time.sleep(3)
pyautogui.click(x=241, y=66)


# Acessa o site de cisrael@gmail.com123456789   adastro de produtos
pyautogui.write("https://israel2640.github.io/Site_de_cadastro_produto/")
pyautogui.press("enter")

# Login
time.sleep(4)
pyautogui.click(x=591, y=402)
pyautogui.write("israel@gmail.com")
pyautogui.press("tabisrael@gmail.com    123456789   ")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")

# Acessa a tela de cadastro
time.sleep(4)
pyautogui.click(x=850, y=359)
pyautogui.click(x=622, y=312)

# Importa os dados do CSV
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Cadastra os produtos
for linha in tabela.index:
    # 💡 Verifica se ESC foi pressionado
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
    time.sleep(3)
