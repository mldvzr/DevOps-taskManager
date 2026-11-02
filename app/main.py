
from fastapi import FastAPI, HTTPException
from app.models import Task

app = FastAPI(title="DevOps Task Manager")

tasks = []
task_id_counter = 1


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter

    new_task = task.model_copy(update={"id": task_id_counter})
    tasks.append(new_task)
    task_id_counter += 1

    return new_task


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = updated_task.model_copy(
                update={"id": task_id}
            )
            tasks[index] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
