document.addEventListener('DOMContentLoaded', function () {
    // Fetch transactions from the server
    axios.get('/api/get-transactions', {
        withCredentials: true, // Include credentials for session cookies
        headers: {
            'X-Requested-With': 'XMLHttpRequest' // Mark as an AJAX request
        }
    })
        .then(function (response) {
            const data = response.data; // Extract transactions data
            const tbody = document.querySelector('#transactionsTable tbody');

            // Loop through transactions and add them to the table
            data.transactions.forEach(function (transaction) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${transaction.amount}</td>
                    <td>${transaction.category}</td>
                    <td>${transaction.description || 'N/A'}</td>
                    <td>${transaction.transaction_date}</td>
                `;
                tbody.appendChild(row);
            });
        })
        .catch(function (error) {
            console.error('Error fetching transactions:', error);
            alert('Failed to load transactions. Please try again.');
        });
});


// document.addEventListener('DOMContentLoaded', function () {
//     // Ensure transactions are available
//     if (!transactions || transactions.length === 0) {
//         console.warn('No transactions found.');
//         return;
//     }

//     const tbody = document.querySelector('#transactionsTable tbody');

//     // Loop through transactions and add them to the table
//     transactions.forEach(function (transaction) {
//         const row = document.createElement('tr');
//         row.innerHTML = `
//             <td>${transaction.amount}</td>
//             <td>${transaction.category}</td>
//             <td>${transaction.description || 'N/A'}</td>
//             <td>${transaction.transaction_date}</td>
//         `;
//         tbody.appendChild(row);
//     });
// });

