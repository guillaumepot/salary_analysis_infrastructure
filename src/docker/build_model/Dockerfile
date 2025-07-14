FROM python:3.10-slim


WORKDIR /app

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

ENV PYTHONPATH=/app:$PYTHONPATH

EXPOSE 9992

CMD ['python3', 'build_model.py']