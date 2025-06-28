.PHONY: setup add-account react start

setup:
	./setup.sh

add-account:
	source venv/bin/activate && python app.py add-account

react:
	source venv/bin/activate && python app.py react $(channel)

start:
	./start.sh
