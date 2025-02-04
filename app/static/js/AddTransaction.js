

const transactionForm = document.getElementById("addTransactionForm")
transactionForm.addEventListener('submit', async(event) => {
    event.preventDefault()

    const formData = new FormData(transactionForm)
    const data = {
        amount : formData.get("amount"), //get(name)
        category : formData.get("category"),
        transaction_date : formData.get("transaction_date"),
        description : formData.get("description")
    }
    console.log("form data ",data)

    await axios.post(
        '/add-transaction',
        data,
        { withCredentials: true } // Include credentials (cookies) in the request
    )
    .then((res) => {
        console.log("Message from server: ", res);
        if (res.status === 201) {
            alert('Transaction added successfully!');
            window.location.href = '/add-transaction'; // Redirect to AddTransaction page
        }
    })
    .catch((error) => {
        console.log("Login failed: ", error);

        // Show an error message to the user
        if (error.response && error.response.data && error.response.data.error) {
            alert(error.response.data.error);
        } else {
            alert('An unexpected error occurred. Please try again.');
        }
    });
    
});