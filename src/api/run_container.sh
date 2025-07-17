#!/bin/bash

image_api='salary-prediction-api:latest'

docker run -d -p 8000:8000 --name salary-prediction-api --volume ./models:/app/models $image_api