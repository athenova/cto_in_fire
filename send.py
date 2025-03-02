import schedule
import time
from project import Project

if __name__ == '__main__':
    project = Project()
    #schedule.every().day.at("12:00",'Europe/Moscow').do(project.send, type='problem')
    schedule.every().day.at("17:00",'Europe/Moscow').do(project.send, type='solution')
    two_minutes = 2 * 60
    for i in range(two_minutes):
        schedule.run_pending()
        time.sleep(1)
