FROM python:3.8
RUN mkdir /home/app
COPY . /home/app/capback
RUN pip install django
EXPOSE 8000
CMD ["python","manage.py","runserver"]
