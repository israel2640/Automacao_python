# 🤖 Automação de Cadastro de Produtos com Python

Este projeto realiza o **cadastro automático de produtos em um site**, utilizando Python, leitura de um arquivo CSV e automação com PyAutoGUI.

---

## 🚀 Funcionalidades

- Abre o navegador Chrome automaticamente
- Acessa o site de cadastro de produtos
- Realiza login com usuário e senha
- Lê os dados do arquivo `produtos.csv`
- Preenche o formulário no site com os dados lidos
- Roda automaticamente até o fim ou até o usuário apertar ESC (se tiver permissão adequada)

---

## 🧰 Tecnologias e Bibliotecas Utilizadas

- [Python 3.10+](https://www.python.org/)
- `pandas` → Leitura de CSV
- `pyautogui` → Automação de teclado e mouse
- `keyboard` → Interrupção via tecla ESC *(requer permissões especiais)*
- `time` e `os` (bibliotecas padrão do Python)

---

## 🖥️ Pré-requisitos

Antes de rodar o projeto, certifique-se de:

1. Ter o **Python instalado e funcionando** (`python --version`)
2. Instalar as bibliotecas necessárias (veja abaixo)
3. Estar com o **arquivo `produtos.csv` na mesma pasta que `codigo.py`**
4. Rodar o script em um ambiente **com interface gráfica** (desktop com acesso ao mouse e teclado)
5. Se quiser usar `keyboard.is_pressed()`, **rodar como administrador**

---

## 🧪 Instalação das dependências

No terminal (cmd, PowerShell ou terminal do VS Code), execute:

```bash
pip install pandas pyautogui keyboard
```

Se quiser atualizar o pip:

```bash
python -m pip install --upgrade pip
```

---

## 📂 Estrutura do Projeto

```
Automacao_python/
│
├── Automação Python/
│   ├── codigo.Py           ← Script principal
│   ├── produtos.csv        ← Arquivo com os dados dos produtos
│   ├── gabarito.py         ← Script auxiliar
│   └── pegar_posicao.py    ← Para descobrir posições do mouse
│
├── README.md               ← Este arquivo
├── LICENSE
└── .gitattributes
```

---

## 🧾 Formato esperado do `produtos.csv`

O arquivo `.csv` deve conter as colunas abaixo:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
123,Acer,Notebook,Informática,3500,2500,"Promoção até dia 30"
...
```

---

## ▶️ Como executar

1. **Abra o terminal como administrador**
2. Navegue até a pasta onde está o `codigo.Py`
3. Execute:

```bash
python codigo.Py
```

---

## 🛑 Como interromper

- Pressione `ESC` enquanto o script estiver rodando **(somente se estiver executando como administrador)**
- Ou clique no botão "Parar" se estiver usando a versão com `tkinter`

---

## ⚠️ Possíveis erros e soluções

| Erro | Causa | Solução |
|------|-------|---------|
| `ModuleNotFoundError: No module named 'keyboard'` | Biblioteca não instalada | Execute `pip install keyboard` |
| `Erro ao ler CSV: No such file or directory` | CSV não está no mesmo diretório | Verifique o caminho do arquivo ou use `os.path` no código |
| `keyboard.is_pressed()` não funciona | Permissões insuficientes | Rode o terminal ou VS Code como **Administrador** |
| O Chrome não abre | Nome do navegador não corresponde | Confirme se `"chrome"` funciona no campo de busca do Windows |

---

## 💡 Dicas

- Use o script `pegar_posicao.py` para descobrir as coordenadas do mouse com `pyautogui.position()`
- Sempre teste com uma pequena quantidade de dados antes de usar o CSV completo
- Deixe um tempo suficiente entre os comandos com `pyautogui.PAUSE = 4.0` para evitar erros

---

## 👨‍💻 Autor

Desenvolvido por **Israel**, com apoio da assistente **Jarvis** ❤️  
Curso: Técnico em Desenvolvimento de Sistemas - ETE Cícero Dias

---