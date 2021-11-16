FROM python:3.9

ADD requirements/ /opt/app/requirements

WORKDIR /opt/app

RUN pip install -r requirements/base.txt
ADD . /opt/app

RUN useradd -ms /bin/bash web && chown -R web /var/log && chown -R web /var/tmp && chown -R web /opt/app
USER web

CMD python3 start.py
