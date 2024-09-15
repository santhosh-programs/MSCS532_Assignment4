from datetime import datetime
import math


class Task:
    def __init__(self, task_id, priority, deadline, arrival_time):
        self.task_id = task_id
        self.priority = priority
        self.deadline = deadline
        self.arrival_time = arrival_time

    def __repr__(self):
        return f"Task(id: {self.task_id}, priority: {self.priority}, deadline: {self.deadline}, arrival_time: {self.arrival_time})"

    def copy_with(self, task_id=None, priority=None, deadline=None, arrival_time=None):
        return Task(
            task_id=task_id if task_id is not None else self.task_id,
            priority=priority if priority is not None else self.priority,
            deadline=deadline if deadline is not None else self.deadline,
            arrival_time=arrival_time if arrival_time is not None else self.arrival_time,
        )

# Check if the heap is empty


def is_empty(data):
    return len(data) == 0

# Reads the next high priority item but does not remove it


def read_next_high_priority_item(data):
    if is_empty(data):
        raise Exception("Heap is empty")
    return data[0]

# Removes the high priority item and reshuffles the heap to maintain the max heap property


def extract_high_priority_item(data, mapper):
    max_task = read_next_high_priority_item(data)
    data[0] = data[-1]
    mapper[data[-1].task_id] = 0
    data.pop()
    max_heapify(data, mapper, 0)
    return max_task

# Inserting a new task and rebuilding the heap


def insert_new_task(data, mapper, task):
    priority = task.priority
    task.priority = -math.inf
    data.append(task)
    mapper[task.task_id] = len(data) - 1
    increase_priority(data, mapper, task.task_id, priority)

# Increase the priority of a specified taskId
# New priority should be higher than the existing one


def increase_priority(data, mapper, task_id, priority):
    if task_id not in mapper:
        raise Exception(f"No mapping ID found for {task_id}")

    idx = mapper[task_id]

    if priority < data[idx].priority:
        raise Exception("Provided priority is lower than the existing one")

    if priority == data[idx].priority:
        return

    data[idx].priority = priority

    while idx > 0 and data[parent_index(idx)].priority < priority:
        parent_idx = parent_index(idx)
        temp = data[parent_idx].copy_with()
        mapper[temp.task_id] = idx
        mapper[data[idx].task_id] = parent_idx
        data[parent_idx] = data[idx].copy_with()
        data[idx] = temp
        idx = parent_idx

# To retrieve the index of the parent of that node in a 0-indexed list


def parent_index(index):
    return (index - 1) // 2

# Build the max heap structure from a list of tasks


def build_max_heap(data, mapper):
    for i in range(len(data) // 2, -1, -1):
        max_heapify(data, mapper, i)

# Function to rebuild the heap to follow the max heap property


def max_heapify(data, mapper, i):
    left_idx = 2 * i + 1
    right_idx = 2 * i + 2
    largest = i

    if left_idx < len(data) and data[left_idx].priority > data[largest].priority:
        largest = left_idx

    if right_idx < len(data) and data[right_idx].priority > data[largest].priority:
        largest = right_idx

    if largest != i:
        temp = data[largest]
        mapper[temp.task_id] = i
        mapper[data[i].task_id] = largest
        data[largest] = data[i]
        data[i] = temp
        max_heapify(data, mapper, largest)

# Main function to demonstrate the task heap functionality


def main():
    data = []
    mapper = {}

    # Adding tasks to the data list and mapper
    for i in range(10):
        task = Task(
            task_id=i,
            priority=i + 1,
            deadline=datetime(2024, 12, i + 1),
            arrival_time=datetime(2025, 12, i + 1)
        )
        data.append(task)
        mapper[i] = i

    build_max_heap(data, mapper)
    increase_priority(data, mapper, 1, 100)
    increase_priority(data, mapper, 2, 400)

    insert_new_task(data, mapper, Task(12, 12, datetime.now(), datetime.now()))

    print(mapper)
    print([task.priority for task in data])

    extract_high_priority_item(data, mapper)
    increase_priority(data, mapper, 9, 99)
    print([task.priority for task in data])

    extract_high_priority_item(data, mapper)
    print([task.priority for task in data])

    extract_high_priority_item(data, mapper)
    print([task.priority for task in data])


if __name__ == "__main__":
    main()
