from flask import Flask

# Crea una nuova applicazione Flask
app = Flask(__name__)

# Definisci la homepage
@app.route('/')
def home():
    return "Ciao amore, questo è il mio primo sito, ti amo <3"

# Avvia il server
if __name__ == '__main__':
    app.run(debug=True)
pip freeze > requirements.txt
web: gunicorn app.py:app
