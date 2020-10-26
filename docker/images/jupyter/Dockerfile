FROM python:3.9

EXPOSE 8888

RUN pip install \
  numpy \
  pandas \
  notebook \
  pymsql \
  mysqlclient \
  mysql-connector-python \


RUN mkdir /lab

WORKDIR  /lab

ENTRYPOINT [ "jupyter" ]
CMD [ "notebook","--allow-root","--ip=0.0.0.0"]
