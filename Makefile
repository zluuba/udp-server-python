install-dev-dep:
	pip install -r requirements_dev.txt

server:
	python3 udp_server/server.py

client:
	python3 udp_server/client.py

test:
	pytest tests

lint:
	flake8 server

typing:
	mypy server

test-coverage:
	pytest --cov=server tests/

check:
	make test
	make lint
	make typing
	make test-coverage