FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8888

CMD ["jupyter", "notebook", "image_gen.ipynb", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]