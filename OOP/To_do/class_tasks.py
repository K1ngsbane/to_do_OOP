from source import *
from helpers import *
from datetime import datetime


class Tasks:

    def __init__(self, user_id, title, description, priority, due_date, done):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.done = done

    def __str__(self):
        return f'{self.user_id}  {self.title} {self.description} {self.priority} {self.due_date} {self.done}'

    def change_done(self):
        self.done = True

    def change_priority(self):
        self.priority = input('Введіть оновлений пріорітет: ')

    def check_completed(self):
        if self.done:
            print(self.title)

    def check_uncompleted(self):
        if self.done is False:
            print(self.title)

    def check_overdue(self):
        if self.due_date < datetime.now():
            print('Задача ' + self.title + ' прострочена')


task_1 = Tasks(1, 'Wash hands', 'Wash hands and face with soap', 5, datetime(2021, 11, 1, 12, 37), False)

print('Доступні функції:')
for index in functional.functions:
    print(index + ': ' + functional.functions[index])

chosen = input('Виберіть функцію та введіть відповідну букву: ')
while True:
    if chosen.lower() == 'm':
        # clear_screen.cls()
        # convert_datetime_to_str.convert_datetime_to_str(tasks)
        # save_as_json.save_as_json('data', 'tasks.json', tasks)
        # print('Данні збережено. До зустрічі!')
        break
    elif chosen.lower() in functional.answer_option:
        if chosen.lower() == 'a':
            clear_screen.cls()
            # add_task.add_new_task(tasks)
            # print(tasks)
            skip.skip()
        elif chosen.lower() == 'b':
            clear_screen.cls()
            # find_task.find_task(tasks)
            skip.skip()
        elif chosen.lower() == 'c':
            clear_screen.cls()
            task_1.change_done()
            print(task_1)
            skip.skip()
        elif chosen.lower() == 'd':
            clear_screen.cls()
            task_1.change_priority()
            print(task_1)
            skip.skip()
        elif chosen.lower() == 'e':
            clear_screen.cls()
            # remove_task.del_task(tasks)
            skip.skip()
        elif chosen.lower() == 'f':
            clear_screen.cls()
            # check_tasks_adding_order.check_order(tasks)
            skip.skip()
        elif chosen.lower() == 'g':
            clear_screen.cls()
            # check_tasks_priority_order.check_priority(tasks)
            skip.skip()
        elif chosen.lower() == 'h':
            clear_screen.cls()
            task_1.check_uncompleted()
            print(task_1)
            skip.skip()
        elif chosen.lower() == 'i':
            clear_screen.cls()
            task_1.check_completed()
            print(task_1)
            skip.skip()
        elif chosen.lower() == 'j':
            clear_screen.cls()
            task_1.check_overdue()
            print(task_1)
            skip.skip()
        elif chosen.lower() == 'k':
            clear_screen.cls()
            # check_statistics.check_stat(tasks)
            skip.skip()
        elif chosen.lower() == 'l':
            # clear_screen.cls()
            # convert_datetime_to_str.convert_datetime_to_str(tasks)
            # save_as_csv.save_as_csv('data', 'tasks.csv', tasks)
            # print('Тестові данні збережено.')
            # skip.skip()
            pass
        for index in functional.functions:
            print(index + ': ' + functional.functions[index])
        chosen = input('Виберіть функцію та введіть відповідну букву: ')
    else:
        chosen = input('Виберіть корректний індекс задачі: ')
