FROM python:3.12-slim


WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

ENV PYTHONPATH=/app:$PYTHONPATH

EXPOSE 8000

CMD ["python", "main.py"] 