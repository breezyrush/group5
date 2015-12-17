/**
 * Created by Lemmeister on 12/17/2015.
 */

function add_genre() {
    var genre = $('input[name=genre]').val();
    $.ajax({
        type: 'get',
        url: '/addGenre/',
        data: {'genre': genre},
        success: function(data) {

        }
    });
}

$(document).ready(function() {

});