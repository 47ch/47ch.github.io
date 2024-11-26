document.getElementById('loyalty-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let valid = true;

    // Validate mobile number
    const mobileNumber = document.getElementById('mobile-number').value;
    if (mobileNumber.trim() === '') {
        alert('Please enter your mobile number.');
        valid = false;
    }

    if (valid) {
        // Redirect to the registration page
        window.location.href = 'registration.html';
    }
});
