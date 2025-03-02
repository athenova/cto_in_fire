import json
from project import Project

def gen(count):
    tasks = json.load(open('files/in_progress.json', 'rt', encoding='UTF-8'))
    project = Project()
    for i, task in enumerate(tasks):
        if i < count:
            #project.gen_image(task, 'problem')
            project.gen_image(task, 'solution')

if __name__ == '__main__':
    gen(1)
