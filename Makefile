# Makefile for workout-analytics.

NO_COLOR	= \033[0m
COLOR	 	= \033[32;01m

deploy: backup
	@echo "$(COLOR)* Updating code.$(NO_COLOR)"
	@git pull
	@echo "$(COLOR)* Re-creating containers.$(NO_COLOR)"
	@docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --force-recreate web nginx postgres memcached

backup:
	@echo "$(COLOR)* Backing up database.$(NO_COLOR)"
	@docker run --volumes-from workoutanalytics_data_1 -v $(PWD):/backup postgres tar cvf /backup/backup.tar /var/lib/postgresql/data

restore:
	@echo "$(COLOR)* Restoring database.$(NO_COLOR)"
	@docker run --volumes-from workoutanalytics_data_1 -v $(PWD):/backup postgres tar xvf /backup/backup.tar

clean:
	@echo "$(COLOR)* Cleaning unwanted files.$(NO_COLOR)"
	@-find . -type f \( -name \*~ -o -name \*.pyc -o -name \#\*\# \) -delete -print 2>/dev/null
