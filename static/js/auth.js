$(document).ready(function() {
    $('#login-btn').click(function(event) {
        event.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

        const alert = (message, type) => {
        const wrapper = document.createElement('div')
        wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
        ].join('')

        alertPlaceholder.append(wrapper)}

        if (!username || !password) {
            alert('Please enter both username and password.', 'danger');
            return;
        }

        $.ajax({
            url: '/login',
            type: 'POST',
            data: {username: username, password: password},
            success: function(response) {
                if (response.success) {
                    window.location.href = '/home';
                } else {
                    alert('Login failed. Please try again.', 'danger');
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

        const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

        const alert = (message, type) => {
        const wrapper = document.createElement('div')
        wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
        ].join('')

        alertPlaceholder.append(wrapper)}

        if (!email || !username || !password1 || !password2) {
            alert('Please enter email, username, and password.', 'danger');
            return;
        } else if (password1 != password2) {
            alert('Passwords don\'t match', 'danger');
            return;
        }

        $.ajax({
            url: '/signup',
            type: 'POST',
            data: {email: email, username: username, password1: password1},
            success: function(response) {
                if (response.success) {
                    window.location.href = '/home';
                } else {
                    alert('Signup failed. Please try again.', 'success');
                }
            },
            error: function() {
                alert('Error occurred while processing your request.');
            }
        });
    });
});