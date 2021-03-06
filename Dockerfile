FROM python:3.9

WORKDIR /app

COPY requirements.txt .
# コンテナ内で必要なパッケージをインストール
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

COPY ./ ./
EXPOSE 8000
# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]