install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py
lint_consumer:
	pylint --disable=R,C kafka_consumer.py
lint_producer:
	pylint --disable=R,C kafka_producer.py
#test:
#	python -m pytest -vv --cov=hello test_cicd_etl.py

all: install lint_consumer lint_producer format