$(document).ready(function() {
    $('#login-btn').click(function(event) {
        event.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        if (!username || !password) {
            alert('Please enter both username and password.');
            return;
        }

        $.ajax({
            url: '/login',
            type: 'POST',
            data: {username: username, password: password},
            success: function(response) {
                if (response.success) {
                    window.location.href = '/profile';
                } else {
                    alert('Login failed. Please try again.');
                }
            },
            error: function() {
                alert('Error occurred while processing your request.');
            }
        });
    });
});

$(document).ready(function() {
    $('#signup-btn').click(function(event) {
        event.preventDefault();

        var email = $('#email').val();
        var username = $('#username').val();
        var password1 = $('#password1').val();
        var password2 = $('#password2').val();

        if (!email || !username || !password1 || !password2) {
            alert('Please enter email, username, and password.');
            return;
        } else if (password1 != password2) {
            alert('Passwords don\'t match');
            return;
        }

        $.ajax({
            url: '/signup',
            type: 'POST',
            data: {email: email, username: username, password1: password1, password2: password2},
            success: function(response) {
                if (response.success) {
                    window.location.href = '/profile';
                } else {
                    alert('Signup failed. Please try again.');
                }
            },
            error: function() {
                alert('Error occurred while processing your request.');
            }
        });
    });
});
