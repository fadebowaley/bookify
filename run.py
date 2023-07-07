import os
from app import create_app, db
from dotenv import load_dotenv
from config import Config

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
            




if __name__ == '__main__':

    db.create_all()
    app.run(debug=True)
