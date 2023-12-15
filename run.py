import os

# Import the Flask application object
from app import app

# Import all blueprints
from notes import notes_app
from auth import auth_app

# Register the blueprints
app.register_blueprint(notes_app)
app.register_blueprint(auth_app)

# Start the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)