# trunk-ignore(checkov/CKV_DOCKER_3)
# trunk-ignore(checkov/CKV_DOCKER_3)
# trunk-ignore(checkov/CKV_DOCKER_3)
# trunk-ignore-all(trivy/DS002)
FROM python:3.8-slim

# RUN useradd -m trivy

# Install make and python3 with pip
RUN apt-get update && apt-get install -y --no-install-recommends make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Update pip

WORKDIR /app

COPY . .

RUN make install
# RUN make run

# RUN chown -R trivy:trivy /app

# USER trivy
# ENV PATH=$PATH:/home/trivy/.local/bin

# RUN pip install python-dotenv==0.21.1

# COPY utils/config.py /app/config.py

# Your CMD instruction
# CMD ["python", "config.py"]