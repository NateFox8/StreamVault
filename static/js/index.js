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
                    window.location.href = '/profile';
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

$(document).ready(function() {
    $('#watch-later-btn').click(function(event) {
        var username = this.getAttribute('username');
        var movie_title = this.getAttribute('movie_title');
        var movie_year = this.getAttribute('movie_year');
        var movie_rated = this.getAttribute('movie_rated');
        var movie_released = this.getAttribute('movie_released');
        var movie_runtime = this.getAttribute('movie_runtime');
        var movie_imdb_id = this.getAttribute('movie_imdb_id');
        var poster = this.getAttribute('poster');

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

        
        $.ajax({
            url: '/watch_later',
            type: 'POST',
            data: {username:username, movie_title:movie_title, movie_year:movie_year, movie_rated:movie_rated,
            movie_released:movie_released, movie_runtime:movie_runtime, movie_imdb_id:movie_imdb_id, poster:poster},
            success: function(response) {
                if (response.success) {
                    alert('Added to watch later', 'success')
                } else {
                    alert('Already in user\'s watch later', 'danger');
                }
            },
            error: function() {
                alert('Error occurred while processing your request.');
            }
        });

    });
});

$(document).ready(function() {
    $('#favorite-btn').click(function(event) {
        var username = this.getAttribute('username');
        var movie_title = this.getAttribute('movie_title');
        var movie_year = this.getAttribute('movie_year');
        var movie_rated = this.getAttribute('movie_rated');
        var movie_released = this.getAttribute('movie_released');
        var movie_runtime = this.getAttribute('movie_runtime');
        var movie_imdb_id = this.getAttribute('movie_imdb_id');
        var poster = this.getAttribute('poster');

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

        
        $.ajax({
            url: '/favorites',
            type: 'POST',
            data: {username:username, movie_title:movie_title, movie_year:movie_year, movie_rated:movie_rated,
            movie_released:movie_released, movie_runtime:movie_runtime, movie_imdb_id:movie_imdb_id, poster:poster},
            success: function(response) {
                if (response.success) {
                    alert('Added to favorites', 'success')
                } else {
                    alert('Already in user\'s favorites', 'danger');
                }
            },
            error: function() {
                alert('Error occurred while processing your request.');
            }
        });

    });
});

$(document).ready(function() {
    $('#delete-fav-btn').click(function(event) {
        var favorite_id = this.getAttribute('favorite_id');

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
        
        $.ajax({
            url: '/delete_fav',
            type: 'POST',
            data: {favorite_id:favorite_id},
            success: function(response) {
                if (response.success) {
                    alert('Removed from favorites', 'success');
                    setTimeout(function() {
                        location.reload();
                    }, 1500);
                } else {
                    alert('Failed to remove from favorites', 'danger');
                }
            },
            error: function() {
                alert('Error occurred while processing your request.');
            }
        });

    });
});

$(document).ready(function() {
    $('#delete-wl-btn').click(function(event) {
        var watch_later_id = this.getAttribute('watch_later_id');

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
        
        $.ajax({
            url: '/delete_watch_later',
            type: 'POST',
            data: {watch_later_id:watch_later_id},
            success: function(response) {
                if (response.success) {
                    alert('Removed from watch later', 'success');
                    setTimeout(function() {
                        location.reload();
                    }, 1500);
                } else {
                    alert('Failed to remove from watch later', 'danger');
                }
            },
            error: function() {
                alert('Error occurred while processing your request.');
            }
        });

    });
});

$(document).ready(function() {
    $('#search-input').on('input', function() {
        var query = $(this).val();
        $.ajax({
            url: '/search_suggestions',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                var suggestions = response.filter(name => name.toLowerCase().includes(query.toLowerCase()));
                var limitedSuggestions = suggestions.slice(0, 10);
                $('#search-input').autocomplete({
                    source: limitedSuggestions
                });
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});