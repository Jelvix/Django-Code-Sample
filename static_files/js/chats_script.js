$(document).ready(function () {
    var msgArea = $('#msgArea'),
        elementMessage = $('#message'),
        room_id = $('[data-room]').data('room');

    function scrollDown() {
        $('.pre-scrollable').animate({
            scrollTop: $('.pre-scrollable')[0].scrollHeight
        }, 200);
    }

    webSocket = new WebSocket('ws://' + window.location.host + `/room/${room_id}/`);
    webSocket.onmessage = function (message) {
        var data = JSON.parse(message.data),
            className = 'message-alien';
        if (data.sender_id === $('form').find('input[name="sender_id"]').val())
            className = 'message-mine';

        $('.post_text:last').after(`<p class="post_text" id="${className}"><strong>` + data.text + '</strong><br>'
            + data.sender + '</span><br><span>' + data.creation_date + '</span></p>')
        scrollDown()
    };


    scrollDown();

    $('#btnSubmit').on('click', function () {
        if ($('form').find('textarea').val().trim().length > 0) {
            webSocket.send(
                JSON.stringify({
                    'text': $('form').find('textarea').val(),
                    'sender_id': $('form').find('input[name="sender_id"]').val()
                })
            )
            $('textarea').val('')
            scrollDown();
        }
    })
})