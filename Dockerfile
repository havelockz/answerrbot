FROM python:3
WORKDIR /app
COPY . .
WORKDIR /app
RUN pip install -r requirements.txt
CMD python mail.py