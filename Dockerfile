FROM alpine:latest

ENV RCLONE_CONFIG_FILE="/config/rclone.conf"

VOLUME /media/rclone
VOLUME /config

ADD main.py /config/

RUN apk add python3 rclone

CMD python3 /config/main.py