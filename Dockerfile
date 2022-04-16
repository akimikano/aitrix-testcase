FROM python:3

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=0.1.0 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip3 install poetry

RUN poetry install

CMD python manage.py migrate && python manage.py collectstatic --no-input && gunicorn -b 0.0.0.0:8000 --log-level info --reload -w 4 apps:application
