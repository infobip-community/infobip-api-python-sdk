DOCKERFILE ?= -f Dockerfile
IMAGE_NAME ?= infobip_python_whatsapp_client
ENV ?= development
TAG ?= latest

.PHONY: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: build
build: ## Build the docker image. Check Makefile for "env" and "tag" arguments usage.
build: env ?= ${ENV}
build: tag ?= ${TAG}
build:
	docker build -t ${IMAGE_NAME}_${env}:${tag} --target ${env} ${DOCKERFILE} .

.PHONY: run
run: ## Run the container. Check Makefile for "env" and "tag" arguments usage.
run: env ?= ${ENV}
run: tag ?= ${TAG}
run:
	docker run -it --rm ${IMAGE_NAME}_${env}:${tag} /bin/sh
