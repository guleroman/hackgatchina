FROM python:3-onbuild
RUN pip3 install --upgrade pip

RUN git clone https://github.com/guleroman/hackgatchina.git /API
WORKDIR /API

EXPOSE 5000

ENTRYPOINT ["python3", "microblog/run.py"]