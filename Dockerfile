FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r app/requirements.txt

EXPOSE 5000

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]