#!/bin/bash

kubectl create secret docker-registry gitlab-registry-secret \
  --docker-server=registry.gitlab.com \
  --docker-username=changeme \
  --docker-password=changeme \
  --docker-email=changeme \
  -n rncp