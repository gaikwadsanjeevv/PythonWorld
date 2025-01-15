from flask import Flask, request, jsonify
from app.models import Expense
from app import db
from sqlalchemy import func
from datetime import datetime

def register_routes(app):
    # POST /expenses - Create a new expense
    @app.route('/expenses', methods=['POST'])
    def create_expense():
        """Create a new expense"""
        data = request.json
        try:
            # Convert the date string to a datetime object
            expense_date = datetime.fromisoformat(data['date'])

            # Create the Expense object
            expense = Expense(
                amount=data['amount'],
                description=data.get('description', ''),
                category=data.get('category', 'Other'),
                date=expense_date
            )
            db.session.add(expense)
            db.session.commit()
            return jsonify({'message': 'Expense created!', 'id': expense.id}), 201
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use ISO 8601 format: YYYY-MM-DDTHH:MM:SS'}), 400

    # GET /expenses - Fetch all expenses
    @app.route('/expenses', methods=['GET'])
    def get_expenses():
        """Fetch all expenses"""
        expenses = Expense.query.all()
        return jsonify([
            {
                'id': exp.id,
                'amount': exp.amount,
                'description': exp.description,
                'category': exp.category,
                'date': exp.date.isoformat()
            } for exp in expenses
        ])

    # PUT /expenses/<id> - Update an expense
    @app.route('/expenses/<int:expense_id>', methods=['PUT'])
    def update_expense(expense_id):
        """Update an expense by ID"""
        expense = Expense.query.get(expense_id)
        if not expense:
            return jsonify({'error': 'Expense not found'}), 404

        data = request.json
        if 'amount' in data:
            expense.amount = data['amount']
        if 'description' in data:
            expense.description = data['description']
        if 'category' in data:
            expense.category = data['category']
        if 'date' in data:
            try:
                expense.date = datetime.fromisoformat(data['date'])
            except ValueError:
                return jsonify({'error': 'Invalid date format. Use ISO 8601 format: YYYY-MM-DDTHH:MM:SS'}), 400

        db.session.commit()
        return jsonify({'message': 'Expense updated!'})

    # DELETE /expenses/<id> - Delete an expense
    @app.route('/expenses/<int:expense_id>', methods=['DELETE'])
    def delete_expense(expense_id):
        """Delete an expense by ID"""
        expense = Expense.query.get(expense_id)
        if not expense:
            return jsonify({'error': 'Expense not found'}), 404

        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense deleted!'})

    # GET /summary - Total expenses and breakdown by category
    @app.route('/summary', methods=['GET'])
    def get_summary():
        """Returns total expenses and breakdown by category"""
        total_expenses = db.session.query(func.sum(Expense.amount)).scalar()
        category_breakdown = db.session.query(
            Expense.category,
            func.sum(Expense.amount)
        ).group_by(Expense.category).all()

        summary = {
            "total_expenses": total_expenses or 0,
            "category_breakdown": {category: amount for category, amount in category_breakdown}
        }
        return jsonify(summary)

    # GET /highest-expense - Returns the highest expense and its details
    @app.route('/highest-expense', methods=['GET'])
    def get_highest_expense():
        """Returns the highest single expense and its details"""
        highest_expense = db.session.query(Expense).order_by(Expense.amount.desc()).first()
        if highest_expense:
            return jsonify({
                "id": highest_expense.id,
                "amount": highest_expense.amount,
                "description": highest_expense.description,
                "category": highest_expense.category,
                "date": highest_expense.date.isoformat()
            })
        else:
            return jsonify({"message": "No expenses found."}), 404

    # GET /monthly-summary/<year> - Monthly breakdown of expenses
    @app.route('/monthly-summary/<int:year>', methods=['GET'])
    def get_monthly_summary(year):
        """Returns a monthly breakdown of expenses for a given year"""
        monthly_data = db.session.query(
            func.strftime('%m', Expense.date).label('month'),
            func.sum(Expense.amount)
        ).filter(func.strftime('%Y', Expense.date) == str(year)).group_by('month').all()

        monthly_summary = {month: amount for month, amount in monthly_data}
        return jsonify({"year": year, "monthly_summary": monthly_summary})
