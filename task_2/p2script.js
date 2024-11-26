document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let valid = true;

    // Validate name
    const name = document.getElementById('name').value;
    if (name.trim() === '') {
        document.getElementById('name-error').style.display = 'block';
        valid = false;
    } else {
        document.getElementById('name-error').style.display = 'none';
    }

    // Validate birthday
    const day = document.getElementById('day').value;
    const month = document.getElementById('month').value;
    const year = document.getElementById('year').value;
    if (day.trim() === '' || month.trim() === '' || year.trim() === '') {
        document.getElementById('dob-error').style.display = 'block';
        valid = false;
    } else {
        document.getElementById('dob-error').style.display = 'none';
    }

    // Validate email
    const email = document.getElementById('email').value;
    const noEmail = document.getElementById('no-email').checked;
    if (!noEmail && email.trim() === '') {
        document.getElementById('email-error').style.display = 'block';
        valid = false;
    } else {
        document.getElementById('email-error').style.display = 'none';
    }

    if (valid) {
        alert('Registration successful!');
        // Redirect to the next page or perform any other action
    }
});
