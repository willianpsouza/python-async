FROM python:3.11.1-alpine

WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip \ 
&& apk add --no-cache --virtual .build-deps gcc libc-dev make cargo \
&& pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install --no-cache-dir -r requirements.txt \
&& apk del .build-deps gcc libc-dev make

EXPOSE 8000

ENTRYPOINT [ "/app/gunicorn_starter.sh" ]


#"exec line: docker run -p 8000:8000 cpus=1 -it id_container"
#"bulid line: docker build -t speed_test/python3.07 ."
