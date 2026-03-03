#!/bin/bash

pipenv update

sudo cp server/celery-worker.service /etc/systemd/system/celery-worker.service

sudo systemctl daemon-reload

sudo systemctl enable celery-worker

sudo systemctl start celery-worker

sudo systemctl status celery-worker
