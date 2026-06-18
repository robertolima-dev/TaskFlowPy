# 📜 Changelog


## [0.2.0] - 2026-06-18
### Adicionado
- `TaskFlowPy/cli.py`: implementa de fato o CLI documentado no README
  (`taskflowpy add/list/complete/remove`), que nunca tinha sido commitado.

### Corrigido
- `pyproject.toml` não declarava `dependencies` nem `[project.scripts]`;
  o wheel publicado não instalava `click` e o comando `taskflowpy` nunca
  existia, mesmo `setup.py` e o README prometendo o CLI.

### Alterado
- Removido `setup.py` duplicado; `pyproject.toml` passa a ser a única
  fonte de metadados do pacote.
- Build via `python -m build` + `twine check`, com CI (`ci.yml`) e release
  automatizado por tag (`release.yml`) publicando no PyPI.

## [0.1.0] - 2025-03-19
### Adicionado
- 🚀 Primeira versão do TaskFlowPy.