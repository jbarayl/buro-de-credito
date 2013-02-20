buro-de-credito
===============

Para migraciondes de modelos ver:
	http://south.aeracode.org/


	To start using south...

	Make sure your django tables match your current database tables exactly - if you planned to add or remove columns, comment those out.
	
	manage.py schemamigration creditos --initial
	manage.py migrate creditos --fake
	
	Make changes to your django model
	
	manage.py schemamigration creditos --auto
	manage.py migrate creditos

	Solo para migrar nuevos cambios

	manage.py schemamigration creditos --auto
	manage.py migrate creditos


En caso de que no se pueda subir datos de ciudades a base de datos poner: 
  manage.py cities_light --force-import-all
