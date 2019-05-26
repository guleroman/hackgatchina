FROM python:3-onbuild
RUN pip3 install --upgrade pip

RUN git clone https://github.com/guleroman/hackgatchina.git /API
WORKDIR /API/microblog

EXPOSE 5000

ENTRYPOINT ["python3", "app/views.py"]