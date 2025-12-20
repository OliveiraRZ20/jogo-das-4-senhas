# 🎮 Jogo das 4 Senhas

Um jogo interativo em terminal para 2 jogadores onde você deve descobrir as 4 palavras secretas do seu adversário! Combine estratégia, dedução e um pouco de sorte para vencer.

---

## 🎯 Descrição do Projeto

**Jogo das 4 Senhas** é um jogo clássico reimplementado em Python. Cada jogador define 4 palavras relacionadas entre si, e então se revezam tentando adivinhar as palavras do adversário. A cada tentativa errada, uma letra adicional é revelada, ajudando na próxima rodada.

---

## ✨ Recursos Utilizados

- 🐍 **Python 3.10+** - Linguagem de programação
- 🎨 **Colorama** - Cores em terminal cross-platform (Windows, macOS, Linux)
- 📦 **Match/Case** - Pattern matching moderno do Python
- 🔤 **Type Hints** - Anotações de tipo para melhor legibilidade
- 💻 **Terminal Interativo** - Interface amigável em linha de comando

---

## 📁 Estrutura do Projeto

```
jogo-das-4-senhas/
│
├── game/                          # Pacote principal da aplicação
│   ├── __init__.py               # Inicializador do pacote
│   ├── __main__.py               # Ponto de entrada da aplicação
│   │
│   ├── objects/                   # Lógica principal do jogo
│   │   ├── __init__.py           # Exports do módulo
│   │   ├── jogador.py            # Classe Jogador (pontos, palavras, turno)
│   │   ├── jogo.py               # Classe Jogo (dinâmica, verificação)
│   │   └── menu.py               # Classe Menu (interface)
│   │
│   └── utils/                     # Utilitários e helpers
│       ├── __init__.py           # Inicializador
│       ├── logger.py             # Funções de log com cores
│       ├── terminal.py           # Funções de controle de terminal
│       └── user_input.py         # Validação e leitura de entradas
│
├── requirements.txt               # Dependências do projeto
├── README.md                      # Este arquivo
├── LICENSE                        # Licença do projeto
└── notebook.ipynb                # Notebook Jupyter (documentação/testes)
```

### 🔧 Descrição dos Módulos

| Módulo | Responsabilidade |
|--------|------------------|
| `jogador.py` | Gerencia dados do jogador (nome, palavras, pontos, letras descobertas) |
| `jogo.py` | Controla a dinâmica do jogo (turnos, verificação de vencedor, lógica) |
| `menu.py` | Exibe menus, regras e opções do jogo |
| `logger.py` | Sistema de logging com cores (alertas, informações, confirmações) |
| `terminal.py` | Funções de controle de terminal (limpar, pausar, finalizar) |
| `user_input.py` | Validação robusta de entradas do usuário |

---

## 📋 Pré-requisitos

- **Python 3.10 ou superior**
- **pip** (gerenciador de pacotes Python)
- **Git** (opcional, para clonar o repositório)

### Verificar versão do Python
```bash
python --version
# ou
python3 --version
```

---

## 🚀 Como Executar

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/jogo-das-4-senhas.git
cd jogo-das-4-senhas
```

### 2️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Executar o Jogo
```bash
python -m game
```

**Ou de forma alternativa:**
```bash
python game/__main__.py
```

---

## 🎮 Como Utilizar

### Fluxo do Jogo

1. **Tela Inicial** - Exibe as regras do jogo
2. **Menu Principal** - Escolha uma opção:
   - `1` - Iniciar novo jogo
   - `2` - Ver as regras
   - `3` - Sair do jogo

3. **Criação de Jogadores** - Cada jogador:
   - Digite seu nome
   - Digite 4 palavras (5-15 letras cada)
   - Cada palavra deve ter relação com a anterior

4. **Turnos do Jogo** - Os jogadores se alternam:
   - Visualize as letras já reveladas
   - Digite sua tentativa para adivinhar a palavra
   - Se acertar: avança para próxima palavra
   - Se errar: ganha uma dica (letra adicional)

5. **Vitória** - Primeiro a descobrir as 4 palavras do adversário vence!

### Exemplo de Uso

```
┌─────────────────────────────────────────────────────────────────┐
│                          REGRAS                                 │
├─────────────────────────────────────────────────────────────────┤
│ - 2 jogadores definem 4 palavras cada (5-15 letras)             │
│ - Cada palavra deve ter relação com a anterior                  │
│ - Se errar: uma letra é revelada como dica                      │
│ - Primeiro a descobrir todas as 4 palavras vence!               │
└─────────────────────────────────────────────────────────────────┘

[INFO] João, agora você irá definir suas 4 palavras secretas...
[INFO] Digite a primeira palavra que deseja adicionar:
> PYTHON

[INFO] João, digite uma palavra que tenha a ver com a anterior (PYTHON):
> PROGRAMACAO

... (continuação do jogo)

[INFO] É a vez de Maria jogar!
[INFO] Palavra atual: PY
> PYTHON
[SUCESSO] Parabéns Maria! Você descobriu a palavra 'PYTHON'!
```

### ⌨️ Controles

- **Enter** - Confirmar entrada ou continuar
- **Ctrl + C** - Sair do jogo (fechamento seguro)

### ✅ Validações Implementadas

- ✓ Nomes com apenas letras
- ✓ Palavras entre 5-15 letras
- ✓ Palavras sem repetição
- ✓ Entradas vazias rejeitadas
- ✓ Apenas letras permitidas

---

## 🎨 Compatibilidade

| SO | Status | Detalhes |
|----|--------|----------|
| **Windows** | ✅ Total | Cores funcionam em CMD e PowerShell |
| **macOS** | ✅ Total | Compatível com Terminal nativo |
| **Linux** | ✅ Total | Funciona em todos os terminais |

---

## 📝 Exemplo de Estrutura de Dados

```python
jogador = Jogador()
jogador.nome = "Maria"
jogador.palavras = ["PYTHON", "PROGRAMACAO", "DESENVOLVIMENTO", "SOFTWARE"]
jogador.pontos = 2  # Descobriu 2 palavras
jogador.qtd_letras_descobertas = 3  # Tem 3 letras reveladas da palavra atual
```

---

## 🐛 Tratamento de Erros

O projeto implementa tratamento robusto de erros:
- Validação de entrada em loop até entrada válida
- Tratamento seguro de `KeyboardInterrupt` (Ctrl+C)
- Limpeza de tela automática entre turnos

---

## 📚 Tecnologias e Padrões

- **OOP (Programação Orientada a Objetos)** - Classes bem estruturadas
- **Type Hints** - Anotações de tipo em todas as funções
- **Pattern Matching** - Match/case do Python 3.10+
- **Validação de Entrada** - Funcões dedicadas em `user_input.py`
- **Separação de Responsabilidades** - Módulos com propósitos específicos

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👨‍💻 Autor

Desenvolvido como projeto educacional em Python.

---

**Aproveite o jogo! 🎮✨**
