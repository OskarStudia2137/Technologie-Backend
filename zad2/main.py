from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoCreate):
    id: int

todos = []
id_counter = 1

@app.get("/todos", response_model=list[Todo])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo_data: TodoCreate):
    global id_counter
    new_todo = todo_data.model_dump()
    new_todo["id"] = id_counter
    todos.append(new_todo)
    id_counter += 1
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            updated_data = updated_todo.model_dump()
            updated_data["id"] = todo_id
            todos[index] = updated_data
            return updated_data
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(index)
            return
    raise HTTPException(status_code=404, detail="Todo not found")