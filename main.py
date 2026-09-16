from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class TodoItem(BaseModel):
    content:str
todos = ["学习 python","完成作业"]
@app.get("/todos")
def get_todos():
    return {"todos":todos}
@app.post("/todos")
def add_todo(item:TodoItem):
    todos.append(item.content)
    return {"message":"添加成功","current_todos":todos}