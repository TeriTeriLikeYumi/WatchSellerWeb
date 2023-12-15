import os

# Import the Flask application object
from app import app

# Import all blueprints
from libs.notes import notes_app
from libs.auth import auth_app

# Register the blueprints
app.register_blueprint(notes_app)
app.register_blueprint(auth_app)

# Start the app
if __name__ == "__main__":
    app.run(debug=True)