# Creating-A-Multi-Container-Application-Using-Docker-Compose
This project implements a multi-container architecture using Docker Compose to deploy a Python Flask application alongside a database in separate, networked containers. This setup isolates application and database services for modular development, easy scalability, and improved fault tolerance.

# Usage

1. Update the environment variables in the .env file

2. To start the environment
    Command: docker-compose up

3. To stop the environment
    Command: docker-compose down

4. To rebuild after application code update
    Command: docker-compose up --build