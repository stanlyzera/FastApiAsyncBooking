#!/bin/bash

celery --app=app.tasks.celery_config:celery worker -l INFO --broker=redis://redis:6379/0
