import simple_blogger.CommonBlogger
from datetime import timedelta

class Project():
    def __get_category_folder(self, task):
        return task['group']
                    
    def __get_topic_folder(self, task):
        return task['name']

    def __system_prompt(self, task):
        return "Ты - технический директор, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"

    def __task_converter(idea):
        TOPIC_WORD_LIMIT = 300
        return { 
                    "domain": idea['category'],
                    "name": idea['problem'],
                    "problem_prompt": f"Опиши проблему '{idea['problem']}' из области '{idea['category']}', как если бы она случилась с тобой сегодня и ты рассказываешь её другу, не описывай решение, используй не более {TOPIC_WORD_LIMIT} слов",
                    "problem_image": f"Нарисуй смешной рисунок, вдохновлённый проблемой '{idea['problem']}' из области '{idea['category']}'",
                    "solution_prompt": f"Опиши одно из решений проблемы '{idea['problem']}' из области '{idea['category']}' как если бы ты рассказывал её другу, используй не более {TOPIC_WORD_LIMIT} слов",
                    "solution_image": f"Нарисуй смешной рисунок, вдохновлённый решением проблемы '{idea['problem']}' из области '{idea['category']}'",
                    "group": f"{idea['category']}",
                }

    def __init__(self):
        self.blogger = simple_blogger.CommonBlogger(
            review_chat_id=-1002374309134,
            production_chat_id='@cto_in_fire',
            blogger_bot_token_name='ATHE_BOT_TOKEN',
            catagory_folder_getter=self.__get_category_folder,
            topic_folder_getter=self.__get_topic_folder,
            project_name='cto_in_fire',
            system_prompt=self.__system_prompt,
            task_converter=self.__task_converter,
            days_between_posts=timedelta(days=2),
        )

    def push(self):
        self.blogger.push()

    def revert(self):
        self.blogger.revert()

    def gen_image(self, task, type):
        self.blogger.gen_image(task, type)

    def gen_text(self, task, type):
        self.blogger.gen_text(task, type)

    def review(self, type):
        self.blogger.review(type)

    def send(self, type):
        self.blogger.send(type)