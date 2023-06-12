FROM python:3

WORKDIR /app

COPY . .

RUN python -m pip install flask

RUN python -m pip install scikit-learn

RUN python -m pip install mysql-connector-python


CMD ["python" , "app.py"]


