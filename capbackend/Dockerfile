FROM python:3.9.6
RUN mkdir /home/app
COPY . /home/app/capback
WORKDIR /home/app/capback
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver"]