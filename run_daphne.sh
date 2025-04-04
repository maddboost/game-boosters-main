#!/bin/bash
source /home/game-boosters-main/venv/bin/activate
exec daphne -u /tmp/daphne.sock gameBoosterss.asgi:application

