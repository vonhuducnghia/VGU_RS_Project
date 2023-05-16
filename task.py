class TaskInfo:
    def __init__(self, id):
        self.id = id
        print(f'Init task {self.id}')

    def get_info(self):
        print(f'Task {self.id} is in charge!!!!')