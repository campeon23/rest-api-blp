# CONTRIBUTING

## How to build Dockerfile locally

'''
docker build -t $(docker_app_name) .
'''

## How to run the Dockerfile locally

'''
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" $(docker_app_name) sh -c "flask run"
'''
