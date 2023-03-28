help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  start   Start the containers"
	@echo "  logs    Show the logs"
	@echo "  sh      Open a shell in the app container"

start:
	@docker-compose up -d;

logs:
	@docker-compose logs app -f;

sh:
	@docker-compose exec app sh;

restart:
	@docker-compose restart;

build:
	@docker-compose build;

stop:
	@docker-compose stop;

down:
	@docker-compose down;