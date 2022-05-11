FROM python:3.10.4

WORKDIR /workspace

COPY requirements.txt .

# RUN \
#  apk add --no-cache python3 postgresql-libs && \
#  apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
#  python3 -m pip install -r requirements.txt --no-cache-dir && \
#  apk --purge del .build-deps

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    python-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pip-tools \
    && python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .
