

const loginform = document.getElementById("loginForm");

loginform.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(loginform);
    const data = {
        username: formData.get("username"), // Get value by name
        password: formData.get("password")
    };

    console.log("Form data: ", data);

    // Validate input
    if (!data.username || !data.password) {
        alert('Please enter both username and password.');
        return;
    }

    try {
        const res = await axios.post('/login', data); // Use apiClient for the API call
        console.log("Message from server: ", res);

        if (res.status === 200) {
            alert('Login successful!');
            window.location.href = '/dashboard'; // Redirect to dashboard
        }
    } catch (error) {
        console.error("Login failed: ", error.response?.status, error.response?.data);

        // Show appropriate error message
        if (error.response && error.response.data && error.response.data.error) {
            alert(error.response.data.error);
        } else {
            alert('An unexpected error occurred. Please try again.');
        }
    }
});
