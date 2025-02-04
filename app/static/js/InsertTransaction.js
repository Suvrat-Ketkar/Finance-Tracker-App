const transactionForm = document.getElementById("addTransactionForm");

transactionForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(transactionForm);
    const data = {
        amount: parseFloat(formData.get("amount")), // Ensure it's a number
        category: formData.get("category"),
        transaction_date: formData.get("transaction_date"),
        description: formData.get("description") || "No description provided" // Handle empty description
    };

    console.log("Form data:", data);

    // Simple client-side validation
    if (!data.amount || isNaN(data.amount) || data.amount <= 0) {
        alert("Please enter a valid amount.");
        return;
    }
    if (!data.category) {
        alert("Please select a transaction category.");
        return;
    }
    if (!data.transaction_date) {
        alert("Please select a transaction date.");
        return;
    }

    try {
        const response = await axios.post("/add-transaction", data, {
            withCredentials: true // Ensure cookies are sent
        });

        console.log("Server response:", response);
        
        if (response.status === 201) {
            alert("✅ Transaction added successfully!");
            window.location.href = "/add-transactions"; // Redirect to transactions list
        }
    } catch (error) {
        console.error("Transaction submission failed:", error);

        if (error.response && error.response.data && error.response.data.error) {
            alert(`⚠️ Error: ${error.response.data.error}`);
        } else {
            alert("An unexpected error occurred. Please try again.");
        }
    }
});
