#!/bin/bash

# tests
curl -X GET localhost:8000/hello
echo

# Bonne requete
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "company": 0,
  "gender": 0,
  "position_level": 0,
  "performance_score": 0,
  "work_hours_per_week": 0,
  "experience_years": 0,
  "has_certifications": true,
  "promoted": true
}'
echo

# Mauvaise requete
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "company": 'Apple',
  "gender": M,
  "position_level": 0,
  "work_hours_per_week": 0,
  "experience_years": 0,
  "has_certifications": true,
}'