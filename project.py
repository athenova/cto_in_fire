from simple_blogger import Journalist
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from datetime import datetime

class Project(Journalist):
    def _system_prompt(self, _):
        return "Ты - технический директор, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"

    def _task_converter(self, idea):
        return { 
                    "category": idea['category'],
                    "topic": idea['problem'],
                    "topic_image": f"Нарисуй картинку, вдохновлённую темой '{idea['problem']}' из области '{idea['category']}'",
                    "topic_prompt": f"Выбери рандомно актуальную проблему по теме '{idea['problem']}' из области '{idea['category']}', опиши проблему, как если бы рассказывал другу, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее {self.topic_word_limit} слов",
                }

    def __init__(self, **kwargs):
        super().__init__(
            review_chat_id=-1002374309134,
            first_post_date=datetime(2025, 3, 3),
            text_generator=OpenAITextGenerator(),
            **kwargs
        )