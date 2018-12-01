cd /app/src/website/
pybabel init -i ./messages/messages_en.pot -d translations -l en
pybabel init -i ./messages/messages_ko.pot -d translations -l ko

pybabel compile -d translations

cd /app/src
python run.py
