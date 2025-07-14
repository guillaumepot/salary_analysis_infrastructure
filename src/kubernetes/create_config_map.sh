#!/bin/bash
kubectl create configmap models --from-literal=models_path=/app/models -n salary-prediction