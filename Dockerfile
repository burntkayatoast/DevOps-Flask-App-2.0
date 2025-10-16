FROM python:3.14
COPY hello.py .
RUN pip install flask
EXPOSE 5000
CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]
