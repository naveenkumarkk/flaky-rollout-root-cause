FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    nginx \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install -r /app/api/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

RUN rm -f /etc/nginx/sites-enabled/default
RUN cp /app/nginx/default.conf /etc/nginx/conf.d/default.conf

CMD ["/bin/bash", "/app/scripts/boot.sh"]