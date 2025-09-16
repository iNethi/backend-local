FROM python:3.10.15-alpine3.20

ENV PYTHONUNBUFFERED=1

COPY ./backend/requirements.txt /tmp/requirements.txt
COPY ./backend /backend
WORKDIR /backend
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
      build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \

    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["run.sh"]