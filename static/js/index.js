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

$(document).ready(function() {
    $('#watch-later-btn').click(function(event) {
        var username = this.getAttribute('username');
        var movie_title = this.getAttribute('movie_title');
        var movie_year = this.getAttribute('movie_year');
        var movie_rated = this.getAttribute('movie_rated');
        var movie_released = this.getAttribute('movie_released');
        var movie_runtime = this.getAttribute('movie_runtime');

        const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

        const alert = (message, type) => {
            const wrapper = document.createElement('div')
            wrapper.innerHTML = [
                `<div class="alert alert-${type} alert-dismissible" role="alert">`,
                `   <div>${message}</div>`,
                '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close">&times;</button>',
                '</div>'
            ].join('')

            alertPlaceholder.append(wrapper)
        
            setTimeout(() => {
                wrapper.remove();
            }, 3000);}
        
        $.ajax({
            url: '/watch_later',
            type: 'POST',
            data: {username:username, movie_title:movie_title, movie_year:movie_year, movie_rated:movie_rated,
            movie_released:movie_released, movie_runtime:movie_runtime},
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

        const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

        const alert = (message, type) => {
            const wrapper = document.createElement('div')
            wrapper.innerHTML = [
                `<div class="alert alert-${type} alert-dismissible" role="alert">`,
                `   <div>${message}</div>`,
                '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
                '</div>'
            ].join('')

            alertPlaceholder.append(wrapper)
        
            setTimeout(() => {
                wrapper.remove();
            }, 3000);}
        
        $.ajax({
            url: '/favorites',
            type: 'POST',
            data: {username:username, movie_title:movie_title, movie_year:movie_year, movie_rated:movie_rated,
            movie_released:movie_released, movie_runtime:movie_runtime},
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
    $('.delete-fav-btn').click(function(event) {
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
    $('.delete-wl-btn').click(function(event) {
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