# 📚 **TaskFlowPy** - Gerenciador de Tarefas Simples

**TaskFlowPy** é um gerenciador de tarefas eficiente para Python, permitindo o armazenamento de tarefas em **JSON** e **SQLite**, além de suporte para uso via terminal (CLI).

---

## ✨ **Funcionalidades Principais**
- ✅ **Adicionar, listar, remover e concluir tarefas**.
- 🗂 **Armazenamento flexível**: JSON ou SQLite.
- 🖥 **Interface de Linha de Comando (CLI)** para gerenciamento rápido.
- 🔄 **Suporte para múltiplos formatos de armazenamento**.
- ⚡ **Fácil de instalar e usar**.

---

## ⚡ **Instalação**

Instale o **TaskFlowPy** diretamente do PyPI:

```bash
pip install TaskFlowPy
```

> 💡 Requisitos: Python 3.6 ou superior.

---

## 🚀 **Como Usar**

### ✅ **Adicionar uma Tarefa**
```python
from TaskFlowPy.task_manager import TaskManager

manager = TaskManager()
manager.add_task("Finalizar relatório", "Relatório financeiro de Q2")
```

### 📄 **Listar Tarefas**
```python
tasks = manager.list_tasks()
for task in tasks:
    print(task)
```

### ❌ **Remover uma Tarefa**
```python
manager.remove_task(1)  # Remove a tarefa com ID 1
```

### ✅ **Marcar Tarefa como Concluída**
```python
manager.complete_task(2)  # Marca a tarefa com ID 2 como concluída
```

---

## 🏃 **Executando via CLI**

TaskFlowPy também pode ser usado diretamente no terminal:

```bash
taskflowpy add "Comprar mantimentos" "Lista de compras do mercado"
taskflowpy list
taskflowpy complete 1
taskflowpy remove 2
```

---

## 🏗 **Estrutura do Projeto**
```
TaskFlowPy/
│
├── TaskFlowPy/               # 📦 Código do pacote
│   ├── __init__.py
│   ├── cli.py                    # 🖥 Interface de linha de comando
│   ├── task_manager.py          # 🔥 Implementação principal
│   ├── storage.py               # 📂 Gerenciamento de armazenamento
│
├── tests/                       # 🧪 Testes unitários
│   ├── test_task_manager.py
│
├── pyproject.toml                # ⚙️ Configuração do pacote
├── README.md                    # 📚 Documentação do projeto
├── LICENSE                      # 📜 Licença MIT
└── MANIFEST.in                   # 📋 Inclusão de arquivos extras
```

---

## 📝 **Licença**

Distribuído sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 **Autor**

Desenvolvido por **[Roberto Lima](https://github.com/robertolima-dev)** 🚀✨

---

## 💬 **Contato**

- 📧 **Email**: robertolima.izphera@gmail.com
- 💼 **LinkedIn**: [Roberto Lima](https://www.linkedin.com/in/roberto-lima-01/)
- 💼 **Website**: [Roberto Lima](https://robertolima-developer.vercel.app/)
- 💼 **Gravatar**: [Roberto Lima](https://gravatar.com/deliciouslyautomaticf57dc92af0)

---

## ⭐ **Gostou do projeto?**

Deixe uma ⭐ no repositório e compartilhe com a comunidade! 🚀✨  

```bash
git clone https://github.com/robertolima-dev/TaskFlowPy.git
cd TaskFlowPy
pip install -e .
```