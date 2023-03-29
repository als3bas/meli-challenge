help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  start       Start the containers"
	@echo "  logs        Show the logs"
	@echo "  sh          Open a shell in the container"
	@echo "  restart     Restart the containers"
	@echo "  build       Build the containers"
	@echo "  stop        Stop the containers"
	@echo "  down        Stop and remove the containers"
	@echo "  seeder      Run the seeder"

run:
	@python ./src/main.py $(month);

start:
	@docker-compose up -d;

logs:
	@docker-compose logs -f;

sh:
	@docker-compose exec db sh;

restart:
	@docker-compose restart;

build:
	@docker-compose build;

stop:
	@docker-compose stop;

down:
	@docker-compose down;

seeder:
	@python ./src/seeder.py;