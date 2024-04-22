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
            data: {email: email, username: username, password1: password1},
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

$(document).ready(function() {
    $('#watch-later-btn').click(function(event) {
        var username = this.getAttribute('username');
        var movie_title = this.getAttribute('movie_title');
        var movie_year = this.getAttribute('movie_year');
        var movie_rated = this.getAttribute('movie_rated');
        var movie_released = this.getAttribute('movie_released');
        var movie_runtime = this.getAttribute('movie_runtime');
        var movie_imdb_id = this.getAttribute('movie_imdb_id');
        
        $.ajax({
            url: '/watch_list',
            type: 'POST',
            data: {username:username, movie_title:movie_title, movie_year:movie_year, movie_rated:movie_rated,
            movie_released:movie_released, movie_runtime:movie_runtime, movie_imdb_id:movie_imdb_id},
            success: function(response) {
                if (response.success) {
                    alert('Added to watch later')
                } else {
                    alert('Already in user\'s watch later');
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
        
        $.ajax({
            url: '/favorites',
            type: 'POST',
            data: {username:username, movie_title:movie_title, movie_year:movie_year, movie_rated:movie_rated,
            movie_released:movie_released, movie_runtime:movie_runtime, movie_imdb_id:movie_imdb_id},
            success: function(response) {
                if (response.success) {
                    alert('Added to favorites')
                } else {
                    alert('Already in user\'s favorites');
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
        
        $.ajax({
            url: '/delete_fav',
            type: 'POST',
            data: {favorite_id:favorite_id},
            success: function(response) {
                if (response.success) {
                    alert('Deleted from favorites')
                } else {
                    alert('Failed to remove from favorites');
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
        
        $.ajax({
            url: '/delete_watch_later',
            type: 'POST',
            data: {watch_later_id:watch_later_id},
            success: function(response) {
                if (response.success) {
                    alert('Deleted from watch later')
                } else {
                    alert('Failed to remove from watch later');
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