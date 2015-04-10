#!/usr/bin/make

build: virtualenv lint test

virtualenv:
	virtualenv .venv
	.venv/bin/pip install pytest flake8 mock pyyaml charmhelpers charm-tools ecdsa bundletester

lint: virtualenv
	@echo Inspecting the code for fixable problems...
	.venv/bin/flake8 tests
	.venv/bin/juju-bundle proof

test: virtualenv
	@echo Starting tests...


func_test: virtualenv
	@echo functional tests...
	@.venv/bin/bundletester -v -F -l DEBUG

release: check-path virtualenv
	@.venv/bin/pip install git-vendor
	@.venv/bin/git-vendor sync -d ${KUBERNETES_BUNDLE_BZR}

check-path:
	ifndef KUBERNETES_BUNDLE_BZR
		$(error KUBERNETES_BUNDLE_BZR is undefined)
	endif

clean:
	rm -rf .venv
	find -name *.pyc -delete
