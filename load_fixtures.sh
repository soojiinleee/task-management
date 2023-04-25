#!/bin/bash

# List of fixture files to load
fixtures=(
  "user/fixtures/teams.json"
  "user/fixtures/users.json"
  "task/fixtures/tasks.json"
  "task/fixtures/subtasks.json"
)

# Loop through each fixture file and load it into the database
for fixture in "${fixtures[@]}"
do
  echo "Loading $fixture..."
  python manage.py loaddata "$fixture"
done

echo "All fixtures loaded successfully!"
