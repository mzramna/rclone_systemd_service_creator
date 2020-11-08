FROM alpine:latest

ENV RCLONE_CONFIG_FILE="/config/rclone.conf"
ENV RCLONE_MOUNT_FOLDER="/media/rclone"
VOLUME /media/rclone
VOLUME /config

ADD main.py /config/

RUN apk add python3 rclone

CMD python3 /config/main.py