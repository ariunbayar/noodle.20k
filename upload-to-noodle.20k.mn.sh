#!/bin/bash
tar --exclude='.git' --exclude='.gitignore' --exclude='db.sqlite3' --exclude='.gitmodules' --exclude='main/local_settings.py' -czf - . | ssh user@noodle.20k.mn tar -xzf - -C /home/user/projects/noodle
ssh root@noodle.20k.mn systemctl restart uwsgi
