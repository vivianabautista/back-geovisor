# back-geovisor


docker-compose build
docker-compose up

# Exec Migratiosn Docker Console
docker exec -it <nombre_del_contenedor> sh
python manage.py migrate
exit

# Create New Super User
python manage.py createsuperuser