FROM alpine
RUN apk add --no-cache wget py3-pip prometheus alertmanager

WORKDIR /root
RUN wget https://github.com/prymitive/karma/releases/download/v0.120/karma-linux-amd64.tar.gz && \
    tar -xvf karma-linux-amd64.tar.gz && \
    mv karma-linux-amd64 /usr/bin/karma
RUN pip install --break-system-packages mkdocs
COPY entrypoint.sh main.py prometheus.yml prometheus.alerts.yml alertmanager.yml mkdocs.yml ./
COPY docs ./docs
ENTRYPOINT [ "./entrypoint.sh" ]
