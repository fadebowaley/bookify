from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

# Create users with different roles and email addresses
user = User(
    username='user',
    first_name='John',
    last_name='Doe',
    email='user@bookify.com',
    user_role=0
)
user.set_password('password')

author = User(
    username='author',
    first_name='Jane',
    last_name='Smith',
    email='author@bookify.com',
    user_role=1
)
author.set_password('password')

admin = User(
    username='admin',
    first_name='Admin',
    last_name='User',
    email='admin@bookify.com',
    user_role=2
)
admin.set_password('password')

# Add users to the database
db.session.add(user)
db.session.add(author)
db.session.add(admin)
db.session.commit()

print('Users created successfully.')
