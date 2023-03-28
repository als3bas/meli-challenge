help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  start   Start the containers"
	@echo "  logs    Show the logs"
	@echo "  sh      Open a shell in the app container"
+	@echo "  restart Restart the containers"
	@echo "  build   Build the containers"
	@echo "  stop    Stop the containers"
	@echo "  down    Stop and remove the containers"
	@echo "  dev     Build, start and show the logs"


start:
	@docker-compose up -d;

logs:
	@docker-compose logs app -f;

app-sh:
	@docker-compose exec app sh;

db-sh:
	@docker-compose exec db sh;

restart:
	@docker-compose restart;

build:
	@docker-compose build;

stop:
	@docker-compose stop;

down:
	@docker-compose down;

dev:
	@make build && make start && make logs;

seeder:
	@docker-compose exec app python seeder.py;