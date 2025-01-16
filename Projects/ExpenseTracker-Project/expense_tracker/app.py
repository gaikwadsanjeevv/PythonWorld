from app import create_app
from app.routes import register_routes

app = create_app()

with app.app_context():
    from app import db
    db.create_all()  # Ensure database tables are created

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
