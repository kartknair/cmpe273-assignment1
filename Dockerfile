FROM python:2.7.13
MAINTAINER Karthik Nair "karthikreads@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","printFromRemote.py"]
CMD ["https://github.com/sithu/assignment1-config-example"]