from js import console
from datetime import datetime

tasks = []


def adicionar_task():
    div_main_tasks = Element("div-main-tasks")
    div_main_tasks.element.innerText = ""
    for i in tasks:
        div_main_tasks.element.innerText += f"{i['content']}\n"


def criar_task(*ags, **kags):
    input_task = Element("input_task")
    task = input_task.element.value

    dict_task = {
        "task-id": len(task),
        "content": task,
        "data": datetime.now(),
        "status": "criada"
    }

    tasks.append(dict_task)
    input_task.element.value = ""
    adicionar_task()
