import click

from .task_manager import TaskManager


@click.group()
def main():
    """TaskFlowPy — gerenciador de tarefas via terminal."""


@main.command()
@click.argument("title")
@click.argument("description", default="")
def add(title, description):
    """Adiciona uma nova tarefa."""
    task = TaskManager().add_task(title, description)
    click.echo(f"Tarefa #{task['id']} criada: {task['title']}")


@main.command(name="list")
def list_tasks():
    """Lista todas as tarefas."""
    tasks = TaskManager().list_tasks()
    if not tasks:
        click.echo("Nenhuma tarefa cadastrada.")
        return
    for task in tasks:
        status = "✅" if task["completed"] else "⏳"
        click.echo(f"{status} #{task['id']} {task['title']} — {task['description']}")


@main.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """Marca uma tarefa como concluída."""
    task = TaskManager().complete_task(task_id)
    if task is None:
        click.echo(f"Tarefa #{task_id} não encontrada.")
        raise SystemExit(1)
    click.echo(f"Tarefa #{task_id} marcada como concluída.")


@main.command()
@click.argument("task_id", type=int)
def remove(task_id):
    """Remove uma tarefa pelo ID."""
    TaskManager().remove_task(task_id)
    click.echo(f"Tarefa #{task_id} removida.")


if __name__ == "__main__":
    main()
