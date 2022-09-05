from distutils.log import debug
from website import create_app

app = create_app()

if __name__ == '__main__' : #To run the app only on main.py not in any import etc.
    app.run(debug=True)

