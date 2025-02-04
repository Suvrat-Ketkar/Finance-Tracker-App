

document.getElementById("viewTransactions").addEventListener("click", () => {
    handleNavigation('/view-transactions');
});

document.getElementById("addTransaction").addEventListener("click", () => {
    handleNavigation('/add-transaction');
});

document.getElementById("viewAnalytics").addEventListener("click", () => {
    handleNavigation('/analytics');
});

// Function to handle navigation with Axios
async function handleNavigation(url) {
    try {
        const response = await axios.get(url, { withCredentials: true });
        if (response.status === 200) {
            // Redirect to the page if the request is successful
            window.location.href = url;
        }
    } catch (error) {
        console.error("Navigation failed: ", error);

        // Show an error message to the user
        if (error.response && error.response.data && error.response.data.error) {
            alert(error.response.data.error);
        } else {
            alert('An unexpected error occurred. Please try again.');
        }
    }
}
