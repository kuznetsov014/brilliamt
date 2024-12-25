import os

cmd = os
cmd.system("Scripts\\activate.bat")
cmd.system("python webapp\\manage.py runserver")
