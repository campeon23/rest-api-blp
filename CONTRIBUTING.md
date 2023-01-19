# CONTRIBUTING

## How to build Dockerfile locally

'''
docker build -t $(docker_app_name) .
'''

## How to run the Dockerfile locally

'''
docker run -dp 5006:5000 -w /app -v "$(pwd):/app" $(docker_app_name) sh -c "flask run --host 0.0.0.0"
'''
