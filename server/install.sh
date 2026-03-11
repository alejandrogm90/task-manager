#!/bin/bash

pipenv update

cp app/my-task-worker.service /etc/systemd/system/my-task-worker.service

systemctl daemon-reload

systemctl enable my-task-worker

systemctl start my-task-worker

systemctl status my-task-worker
