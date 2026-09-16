from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

app = FastAPI()

DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, nullable=False)


class TodoItem(BaseModel):
    content: str = Field(..., min_length=1)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).order_by(Todo.id).all()
    return {"todos": [todo.content for todo in todos]}


@app.post("/todos")
def add_todo(item: TodoItem, db: Session = Depends(get_db)):
    todo = Todo(content=item.content)
    db.add(todo)
    db.commit()
    db.refresh(todo)

    current_todos = db.query(Todo).order_by(Todo.id).all()
    return {"message": "添加成功", "current_todos": [t.content for t in current_todos]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
