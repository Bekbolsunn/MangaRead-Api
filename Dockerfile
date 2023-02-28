FROM python:3.10

RUN mkdir /MangaRead

WORKDIR /MangaRead/

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /MangaRead

CMD ["python", "manage.py", "runserver", "0.0.0:8000"]