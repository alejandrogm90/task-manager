docker_run = docker-compose  # Linux
#docker_run = docker         # Windows
python_run = python3 # pipenv run python3
build_name = task-manager-server-image
tasks_id = ""

all: build

rerun: down build

up:
	$(docker_run) up $(build_name)

down:
	$(docker_run) down
	$(docker_run) rm

run:
	$(docker_run) run -p 6380:6379 $(build_name)

build:
	$(docker_run) up --build

list:
	$(docker_run) ps

exec:
	$(docker_run) exec $(build_name) bash

info:
	@if [ "$(tasks_id)" = "" ]; then \
		echo "Add tasks_id=YOUR-TASK-ID"; \
	else \
		echo "Running with tasks_id: $(tasks_id)"; \
		$(python_run) client/info_tareas.py $(tasks_id); \
	fi

show:
	$(docker_run) exec $(build_name) ls /app

app1:
	$(python_run) client/pruebas_celerity_0.py

