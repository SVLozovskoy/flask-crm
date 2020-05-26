FROM ubuntu:latest
MAINTAINER Sergey Lozovskoy 'Sergey_lozovskoy@outlook.com'


RUN  apt-get install -y python3-dev build-essential python3-pip


RUN pip install -r requirments.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]
