FROM python:3.11.2

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install vim openssh-client

RUN useradd -rms /bin/bash/ geeks && chmod 777 ./

WORKDIR /geeks

RUN mkdir /geeks/static && mkdir /geeks/media && chown -R geeks:geeks /geeks && chmod 755 /geeks

COPY --chown=mr:mr . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "core.wsgi:application"]
