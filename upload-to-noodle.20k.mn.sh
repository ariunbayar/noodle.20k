#!/bin/bash
tar --exclude='.git' --exclude='.gitignore' --exclude='.gitmodules' -czf - . | ssh user@noodle.20k.mn tar -xzf - -C /home/user/projects/noodle
ssh user@noodle.20k.mn systemctl restart uwsgi
