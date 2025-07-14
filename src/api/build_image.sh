#!/bin/bash

image_api='salary-prediction-api'
docker build -t $image_api -f Dockerfile ./