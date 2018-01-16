FROM python:latest
ARG settings
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install nodejs -y
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app
RUN npm install
RUN python manage.py collectstatic --settings=$settings --noinput
#RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor
#COPY docker-build/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf