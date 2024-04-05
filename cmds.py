import sys
import os


try:
    args = sys.argv
    if len(args) > 2:
        raise OverflowError("Only 1 argument Expected... args = ['setup', 'run']")
    if args[1] == 'setup':
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")
    elif args[1] == 'run':       
        os.system("python manage.py runserver")
    else:
        print('Error')
except Exception as e:
    print(e)
