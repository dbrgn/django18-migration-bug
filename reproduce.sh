#!/bin/bash
dropdb dj18
createdb dj18
./manage.py migrate
