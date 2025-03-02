# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.


class TASK():
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_done = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = TASK(description, deadline)
        self.tasks.append(new_task)
        print(f"Создана новая задача - {description}")

    def mark_done(self, task_index):
        if 0 <= (task_index - 1) <= len(self.tasks):
            self.tasks[task_index - 1].is_done = True
            print(f'Задача "{self.tasks[task_index - 1].description}" отмечена выполненной!')
        else:
            print(f"Ошибка: {task_index - 1} неверный индекс задачи. В списке всего - {len(self.tasks)} задач!")

    def list_tasks(self):
        print("\nВыполненые задачи:")
        done_task = False
        for i, task in enumerate(self.tasks, start=1):
            if task.is_done:
                print(f"{i}. {task.description} - до {task.deadline}")
                done_task = True
        if not done_task:
            print("Нет выполненных задач.")

        print("\nТекущие задачи (не выполненные):")
        current_task = False
        for i, task in enumerate(self.tasks, start=1):
            if not task.is_done:
                print(f"{i}. {task.description} (до {task.deadline})")
                current_task = True
        if not current_task:
            print("Все задачи выполнены!")


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Купить молоко", "04.03.2025")
    manager.add_task("Сделать презентацию", "05.03.2025")
    manager.add_task("Записаться к врачу", "03.03.2025")
    manager.add_task("Подготовить отчет по проекту", "06.03.2025")
    manager.add_task("Позвонить клиенту для уточнения деталей", "07.03.2025")
    manager.add_task("Оплатить счета за коммунальные услуги", "08.03.2025")
    manager.add_task("Забронировать билеты на отпуск", "09.03.2025")
    manager.add_task("Провести встречу с командой", "10.03.2025")

    manager.list_tasks()
    print("\n"+"#"*50)

    manager.mark_done(1)
    manager.mark_done(5)
    manager.mark_done(8)
    manager.mark_done(10)
    manager.mark_done(8)
    manager.mark_done(-1)


    print("#"*50+"\n")
    manager.list_tasks()
