from simple_blogger import CommonBlogger
from datetime import timedelta

class Project(CommonBlogger):
    def _get_category_folder(self, task):
        return task['group']
                    
    def _get_topic_folder(self, task):
        return task['name']

    def _system_prompt(self, task):
        return "Ты - технический директор, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"

    def _task_converter(self, idea):
        return { 
                    "domain": idea['category'],
                    "name": idea['problem'],
                    "problem_prompt": f"Опиши проблему '{idea['problem']}' из области '{idea['category']}', как если бы она случилась с тобой сегодня и ты рассказываешь её другу, не описывай решение, используй не более {self.topic_word_limit} слов",
                    "problem_image": f"Нарисуй смешной рисунок, вдохновлённый проблемой '{idea['problem']}' из области '{idea['category']}'",
                    "solution_prompt": f"Опиши одно из решений проблемы '{idea['problem']}' из области '{idea['category']}' как если бы ты рассказывал её другу, используй не более {self.topic_word_limit} слов",
                    "solution_image": f"Нарисуй смешной рисунок, вдохновлённый решением проблемы '{idea['problem']}' из области '{idea['category']}'",
                    "group": f"{idea['category']}",
                }

    def __init__(self, **kwargs):
        super().__init__(
            review_chat_id=-1002374309134,
            days_between_posts=timedelta(days=2),
            text_ai_token_name='OPENAI_API_KEY',
            ai_text_model='chatgpt-4o-latest',
            text_base_url='https://api.openai.com/v1',
            **kwargs
        )