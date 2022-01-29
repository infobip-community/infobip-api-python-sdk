FROM python:3.9.10-alpine AS base

ENV APP_GROUP whatsapp
ENV APP_USER whatsapp
ENV PROJECT_DIR /srv
ENV PYTHONUNBUFFERED 1

RUN set -ex \
    && addgroup \
      --system ${APP_GROUP} \
      --gid 1000 \
    && adduser \
      --system ${APP_USER} \
      --ingroup ${APP_GROUP} \
      --home ${PROJECT_DIR} \
      --uid 1000

WORKDIR ${PROJECT_DIR}/src

COPY requirements/common.txt /srv/requirements/

RUN set -ex && pip install -r /srv/requirements/common.txt

COPY src/ ${PROJECT_DIR}/src/

FROM base as production

RUN set -ex && rm -rf /srv/requirements

RUN set -ex && chown -R ${APP_USER}:${APP_USER} ${PROJECT_DIR}

USER ${APP_USER}


FROM base as development

COPY requirements/dev.txt /srv/requirements/

RUN set -ex \
    && pip install -r /srv/requirements/dev.txt \
    && rm -rf /srv/requirements

RUN set -ex && chown -R ${APP_USER}:${APP_USER} ${PROJECT_DIR}

USER ${APP_USER}