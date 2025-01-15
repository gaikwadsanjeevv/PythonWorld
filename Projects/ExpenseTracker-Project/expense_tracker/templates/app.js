const form = document.getElementById('expenseForm');
const expensesDiv = document.getElementById('expenses');

// Base API URL
const apiUrl = 'http://127.0.0.1:5000';

// Fetch all expenses
async function fetchExpenses() {
    const response = await fetch(`${apiUrl}/expenses`);
    const expenses = await response.json();
    expensesDiv.innerHTML = expenses.map(expense => `
        <div>
            <p><strong>Amount:</strong> ${expense.amount}</p>
            <p><strong>Description:</strong> ${expense.description}</p>
            <p><strong>Category:</strong> ${expense.category}</p>
            <p><strong>Date:</strong> ${expense.date}</p>
        </div>
        <hr>
    `).join('');
}

// Add a new expense
form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const newExpense = {
        amount: document.getElementById('amount').value,
        description: document.getElementById('description').value,
        category: document.getElementById('category').value,
        date: document.getElementById('date').value
    };
    await fetch(`${apiUrl}/expenses`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newExpense)
    });
    form.reset();
    fetchExpenses(); // Refresh expenses
});

// Initial fetch
fetchExpenses();
