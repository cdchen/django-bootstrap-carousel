
app_name = django_bootstrap_carousel

top_srcdir = $(shell pwd)

south_migration_options = --auto

all:

south_migrations:
	buildout versions:Django=1.6.10 && \
	$(top_srcdir)/bin/django schemamigration $(app_name) $(south_migration_options)

django_migrations:
	buildout versions:Django=1.7.3 && \
	$(top_srcdir)/bin/django makemigrations $(app_name)

migrations: django_migrations south_migrations


