# FastAPI 待办事项 API

这是一个基于 **FastAPI** 构建的简单待办事项 API 演示项目，用于展示如何使用 Python 快速创建和运行一个轻量级的 RESTful API。

## 项目简介

本项目是一个基于 FastAPI 的简单待办事项 API，当前提供待办事项的查询和创建功能，适合用于学习 FastAPI、接口开发以及 API 文档调试。

## 环境要求

运行本项目需要满足以下环境要求：

- Python 3.X
- FastAPI
- Uvicorn

建议使用 Python 3.8 或更高版本。

## 安装

### 1. 安装项目依赖

在终端中执行以下命令：

```bash
pip install fastapi uvicorn
```

### 2. 获取项目代码

将项目代码下载或克隆到本地后，进入项目根目录：

```bash
cd todo-cli-python
```

## 运行项目

在项目根目录下执行以下命令：

```bash
uvicorn main:app --reload
```

服务启动后，默认运行地址为：

```text
http://127.0.0.1:8000
```

其中：

- `main` 表示 `main.py` 文件
- `app` 表示在 `main.py` 中创建的 FastAPI 应用实例
- `--reload` 表示开启自动重载，修改代码后服务会自动重新启动

## 测试接口

项目启动后，可以通过浏览器打开 FastAPI 自动生成的交互式 API 文档：

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

在 Swagger UI 页面中，可以查看接口说明、填写请求参数并直接调用 API。

## 当前接口

| 请求方法 | 接口路径 | 功能说明 |
|---|---|---|
| `GET` | `/todos` | 获取待办事项列表 |
| `POST` | `/todos` | 创建新的待办事项 |

### 获取待办事项

```http
GET /todos
```

用于获取当前已有的待办事项列表。

### 创建待办事项

```http
POST /todos
```

用于创建一条新的待办事项，具体请求参数请参考接口文档：

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 项目结构

```text
.
├── main.py          # FastAPI 应用入口
└── README.md        # 项目说明文档
```

## 许可证

本项目仅用于学习和演示 FastAPI 的基本使用。