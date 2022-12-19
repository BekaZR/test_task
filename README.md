# test_task

# Start project:
  1) Start docker machine on your PC
  2) Change main project directory in terminal
  3) Create .env file near core directory by .env.example 
  4) Run command **"sudo docker-compose up --build"** in your terminal
  5) Go to localhost in your browser (without port 8000, nginx was connected)
  6) Project was successful started

# API
  1) For create superuser 
     - Run command **"sudo docker ps"** or **"sudo docker container ls"**(when project in docker started)
     - Seach container with name **mad_devs_web** and copy his CONTAINER ID
     - Run command **"sudo docker exec -it *CONTAINER ID* python manage.py createsuperuser"**

  2) Go to **http://localhost/api/properties/** set to body this
     - {
        "key": "Your key",
        "value": "Your value"
      }
     - Select POST method
     
  3) Go to **http://localhost/api/entity/** set to body this
     - {
        "value": number,
        "properties": [id properties]
      }
     - Select POST method
     
  3) Go to **http://localhost/api/entity_wrong_data/** set to body this
     - {
        "data[value]": number
      }
     - Select POST method

  4) Go to **http://localhost/api/entity/** in set to body this
     - Select GET method
