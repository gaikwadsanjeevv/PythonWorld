from app import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-generated unique ID
    amount = db.Column(db.Float, nullable=False)  # Required decimal value
    description = db.Column(db.String(255))  # Optional string
    category = db.Column(db.String(50))  # Category like "Food", "Transport"
    date = db.Column(db.DateTime, nullable=False)  # Required datetime

    def __repr__(self):
        return f"<Expense {self.id}: {self.amount} {self.category}>"
