
from datetime import datetime
from datetime import timedelta
import json
import os
import random

TOPIC_WORD_LIMIT = 300

tasks_file = 'files/in_progress.json'
backlog_file = 'files/backlog.json'

if not os.path.exists(tasks_file):
    if os.path.exists(backlog_file):
        tasks = json.load(open(backlog_file, "rt", encoding="UTF-8"))
        index_start = max(tasks, key=lambda task: task['index'])['index'] + 1
    else:
        tasks = []
        index_start = 1
    for root, dirs, files in os.walk('files/new'):
        for i, file in enumerate(files):
            input_file = f"{root}/{file}"
            data = json.load(open(input_file, "rt", encoding="UTF-8"))
            for item in data:
                task = { 
                    "index": i + index_start,
                    "domain": item['category'],
                    "name": item['problem'],
                    "problem_prompt": f"Опиши проблему '{item['problem']}' из области '{item['category']}', как если бы она случилась с тобой сегодня и ты рассказываешь её другу, не описывай решение, используй не более {TOPIC_WORD_LIMIT} слов",
                    "problem_image": f"Нарисуй смешной рисунок, вдохновлённый проблемой '{item['problem']}' из области '{item['category']}'",
                    "solution_prompt": f"Опиши одно из решений проблемы '{item['problem']}' из области '{item['category']}' как если бы ты рассказывал её другу, используй не более {TOPIC_WORD_LIMIT} слов",
                    "solution_image": f"Нарисуй смешной рисунок, вдохновлённый решением проблемы '{item['problem']}' из области '{item['category']}'",
                    "group": f"{item['category']}",
                }
                tasks.append(task)
            processed_file = f"files/processed/{file}"
            os.rename(input_file, processed_file)

    year = datetime.today().year
    random.seed(year)
    random.shuffle(tasks)

    curr_date = datetime.today() + timedelta(days=2)
    for task in tasks:
        task["date"] = curr_date.strftime("%Y-%m-%d")
        curr_date += timedelta(days=2)

    json.dump(tasks, open(tasks_file, 'wt', encoding='UTF-8'), indent=4, ensure_ascii=False)
    if os.path.exists(backlog_file):
        os.remove(backlog_file)
    print(f"{len(tasks)} tasks created")
else: 
    print("Tasks already exists, revert before push")