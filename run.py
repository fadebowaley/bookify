import os
from app import create_app, db
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
            

#  Initialise the app configuration
app = create_app()


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
