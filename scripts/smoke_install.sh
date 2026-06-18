#!/usr/bin/env bash
# Builda o wheel e instala numa venv limpa (sem deps de dev) para pegar
# dependências/entry points que só faltam fora do ambiente de desenvolvimento.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

rm -rf dist build ./*.egg-info
python -m build

TMP_ROOT="$(mktemp -d)"
VENV_DIR="$TMP_ROOT/venv"
python -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install -q "$(ls dist/*.whl)"

"$VENV_DIR/bin/python" -c "
from TaskFlowPy.task_manager import TaskManager
print('IMPORT OK')
"

cd "$TMP_ROOT"
"$VENV_DIR/bin/taskflowpy" add "smoke" "smoke test"
"$VENV_DIR/bin/taskflowpy" list | grep -q "smoke" && echo "CLI OK"
"$VENV_DIR/bin/taskflowpy" complete 1
"$VENV_DIR/bin/taskflowpy" remove 1

rm -rf "$TMP_ROOT"
echo "Smoke test passou."
