# 基础镜像python=3.9
FROM python:3.9

# 创建工作目录
WORKDIR /code

# 安装环境依赖
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 拷贝代码
COPY ./app /code/app

# 启动应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
