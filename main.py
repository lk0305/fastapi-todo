from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, Integer, String, inspect, select, text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite+aiosqlite:///./todos.db"

engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False, default=False, server_default="0")


class TodoItem(BaseModel):
    content: str = Field(..., min_length=1)


async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

        def get_column_names(sync_connection):
            return {
                column["name"]
                for column in inspect(sync_connection).get_columns("todos")
            }

        column_names = await connection.run_sync(get_column_names)
        if "completed" not in column_names:
            await connection.execute(
                text(
                    "ALTER TABLE todos "
                    "ADD COLUMN completed BOOLEAN NOT NULL DEFAULT 0"
                )
            )


@app.on_event("startup")
async def startup():
    await init_db()


async def get_db():
    async with SessionLocal() as db:
        yield db


@app.get("/todos")
async def get_todos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).order_by(Todo.id))
    todos = result.scalars().all()
    return {
        "todos": [
            {
                "id": todo.id,
                "content": todo.content,
                "completed": todo.completed,
            }
            for todo in todos
        ]
    }


@app.post("/todos")
async def add_todo(item: TodoItem, db: AsyncSession = Depends(get_db)):
    todo = Todo(content=item.content)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)

    result = await db.execute(select(Todo).order_by(Todo.id))
    current_todos = result.scalars().all()
    return {
        "message": "添加成功",
        "current_todos": [todo.content for todo in current_todos],
    }


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    todo = result.scalar_one_or_none()
    if todo is None:
        raise HTTPException(status_code=404, detail="待办事项不存在")

    await db.delete(todo)
    await db.commit()
    return {"message": "删除成功"}


@app.put("/todos/{todo_id}")
async def complete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    todo = result.scalar_one_or_none()
    if todo is None:
        raise HTTPException(status_code=404, detail="待办事项不存在")

    todo.completed = True
    await db.commit()
    await db.refresh(todo)
    return {
        "message": "待办事项已完成",
        "todo": {
            "id": todo.id,
            "content": todo.content,
            "completed": todo.completed,
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
