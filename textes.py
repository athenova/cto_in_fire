import json
from project import Project

def gen(count):
    tasks = json.load(open('files/in_progress.json', 'rt', encoding='UTF-8'))
    project = Project()
    for i, task in enumerate(tasks):
        if i < count:
            project.gen_text(task)

if __name__ == '__main__':
    gen(1)