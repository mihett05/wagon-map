FROM python:3.11-slim

WORKDIR /app

RUN pip install requests

COPY __main__.py disl_one_day.csv ./

CMD ["python", "__main__.py"]
