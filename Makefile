SHELL := /bin/bash
GIT_SHA = $(shell git describe --tags --always)
GIT_BRANCH = $(shell git symbolic-ref --short -q HEAD)
BRANCH_VALID := $(shell [[ $(shell git symbolic-ref --short -q HEAD) =~ ^((release|feature|support|hotfix|bugfix)\/([a-zA-Z0-9][ A-Za-z0-9_.-]*)|(develop|staging|master))$$ ]] && echo matched)
TAG ?= $(GIT_BRANCH)-$(GIT_SHA)
TAG_ESC := $(subst /,-,$(TAG))
TAG_ESC := $(subst \,-,$(TAG_ESC))
IMAGE_NAME = django_starterkit
REPO_URL = id.dkr.ecr.region.amazonaws.com/$(IMAGE_NAME)
DOCKER_IMAGE = $(REPO_URL):$(TAG_ESC)

all: image

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

image:         ## Build the docker image
	docker build -t current -t $(IMAGE_NAME) -t $(DOCKER_IMAGE) .

push:          ## Push image to AWS ECR
	docker push $(DOCKER_IMAGE) .

services:      ## Creates necessary services for development
	docker-compose -f ./docker/docker-compose.services.yml up --force-recreate

services-d:    ## Creates necessary services for development in background
	docker-compose -f ./docker/docker-compose.services.yml up -d

services-down:      ## Creates necessary services for development
	docker-compose -f ./docker/docker-compose.services.yml down

dev-run:       ## Run app locally
	docker-compose -f ./docker/docker-compose.yml -f ./docker/docker-compose.override.dev.yml up --force-recreate

dev-ssh:       ## SSH to the container
	docker-compose -f ./docker/docker-compose.yml -f ./docker/docker-compose.override.dev.yml exec server bash

dev-down:      ## Tear down app 
	docker-compose -f ./docker/docker-compose.yml -f ./docker/docker-compose.override.dev.yml down

dev-migrate:   ## Apply migrations
	docker-compose -f ./docker/docker-compose.yml -f ./docker/docker-compose.override.dev.yml run server migrate

dev-init-data:   ## Apply migrations
	docker-compose -f ./docker/docker-compose.yml -f ./docker/docker-compose.override.dev.yml run server init-data

clean: services-down dev-down
	rm -rf ./docker/data-test

test:          ## Run tests
	docker-compose -f ./docker/docker-compose.yml -f ./docker/docker-compose.override.dev.yml run server test

ci-test:       ## Run tests in CI
	docker-compose -f ./docker/docker-compose.yml run server test

lints:         ## Run lints
	# Code Style
	docker-compose -f ./docker/docker-compose.yml run server pylint --rcfile pylintrc project
	# Code Security
	docker-compose -f ./docker/docker-compose.yml run server bandit --ini bandit.ini -r project
	# Code Complexity (A:1-5, B:6-10, C:11-20, D:21-30, E:31-40, F:40+)
	docker-compose -f ./docker/docker-compose.yml run server radon cc --min C project
	# Code Maintainability (A:100-20, B:19-10, C:9-0)
	docker-compose -f ./docker/docker-compose.yml run server radon mi --min B project
	# Djang checks https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
	docker-compose -f ./docker/docker-compose.yml run server python manage.py check --deploy

tag:           ## Check and return docker tag name
ifneq ($(BRANCH_VALID),matched)
	$(error Wrong branch name!)
endif
	@echo $(TAG_ESC)
