from itertools import count

from flask_migrate import current


def leastinterval(tasks, n):
    task_counts = {}
    for task in tasks:
        if task in task_counts:
            task_counts[task] += 1
        else:
            task_counts[task] = 1

    tasks_heap = [(-cnt,task) for tsdk, cnt in task_counts.items()]

    intervals = 0
    cooldown = {}

    while tasks_heap or cooldown:
        intervals += 1

        tasks_heap.sort(reverse=True)

        if tasks_heap:
            current_count, current_task = tasks_heap.pop(0)
            current_count = -current_task
            if current_count > 1:
                cooldown[current_task] = current_count - 1

        new_cooldown = {}
        for task, remaining in cooldown.items():
            if remaining == 1:
                tasks_heap.append((-1, task))
            else:
                new_cooldown[task] = remaining - 1
        return intervals








