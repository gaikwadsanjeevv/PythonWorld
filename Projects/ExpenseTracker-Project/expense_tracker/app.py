from flask import Flask, render_template
from app.routes import register_routes

# Create the Flask app
def create_app():
    app = Flask(__name__)

    # Register API routes
    register_routes(app)

    return app

app = create_app()

# Serve the index.html file from the templates folder
@app.route('/')
def index():
    return render_template('index.html')  # This will automatically look for 'templates/index.html'

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
