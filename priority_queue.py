from datetime import datetime
import math


class Task:
    def __init__(self, task_id, priority, deadline, arrival_time):
        self.task_id = task_id
        self.priority = priority
        self.deadline = deadline
        self.arrival_time = arrival_time

    def __str__(self):
        return f'Task(id: {self.task_id}, priority: {self.priority}, deadline: {self.deadline}, arrivalTime: {self.arrival_time})'

    def copy_with(self, task_id=None, priority=None, deadline=None, arrival_time=None):
        return Task(
            task_id=task_id if task_id is not None else self.task_id,
            priority=priority if priority is not None else self.priority,
            deadline=deadline if deadline is not None else self.deadline,
            arrival_time=arrival_time if arrival_time is not None else self.arrival_time,
        )


def main():
    sample = [1, 4, 10, 14, 7, 9, 3, 2, 8, 16]
    data = []
    mapper = {}
    for i in range(10):
        data.append(Task(
            task_id=i,
            priority=i + 1,
            deadline=datetime(2024, 12, i + 1),
            arrival_time=datetime(2025, 12, i + 1),
        ))

        # Used to map which task is at which position
        # To keep it simple, currently the index and the taskId are the same.
        mapper[i] = i

    build_max_heap(data, mapper)
    increase_priority(data, mapper, 1, 100)
    increase_priority(data, mapper, 2, 400)
    insert_new_task(
        data,
        mapper,
        Task(
            task_id=12,
            priority=12,
            deadline=datetime.now(),
            arrival_time=datetime.now(),
        ),
    )

    print(mapper)

    print([e.priority for e in data])


def insert_new_task(data, mapper, task):
    priority = task.priority
    task.priority = float('-inf')
    data.append(task)
    mapper[task.task_id] = len(data) - 1
    increase_priority(data, mapper, task.task_id, priority)


def increase_priority(data, mapper, task_id, priority):
    if task_id not in mapper:
        raise Exception(f'No mapping ID found for {task_id}')
    if priority < data[mapper[task_id]].priority:
        raise Exception('Provided priority is lower than the existing one')
    if priority == data[mapper[task_id]].priority:
        return
    index = mapper[task_id]
    data[index].priority = priority
    while index > 0 and data[parent_index(index)].priority < priority:
        temp = data[parent_index(index)].copy_with()
        mapper[temp.task_id] = index
        mapper[data[index].task_id] = parent_index(index)
        data[parent_index(index)] = data[index].copy_with()
        data[index] = temp
        index = parent_index(index)


def parent_index(index):
    return (index - 1) // 2


def build_max_heap(d, mapper):
    for i in range(len(d) // 2, -1, -1):
        max_heapify(d, mapper, i)


def max_heapify(data, mapper, i):
    left_index = 2 * i + 1
    right_i = 2 * i + 2
    largest = i
    if left_index < len(data) and data[left_index].priority > data[largest].priority:
        largest = left_index
    if right_i < len(data) and data[right_i].priority > data[largest].priority:
        largest = right_i
    if largest != i:
        temp = data[largest]
        mapper[temp.task_id] = i
        mapper[data[i].task_id] = largest
        data[largest] = data[i]
        data[i] = temp
        max_heapify(data, mapper, largest)


if __name__ == "__main__":
    main()
