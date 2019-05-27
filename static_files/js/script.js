$('[data-id="likes"]').on('click', function () {
    var $btn = $(this);
    $.get($(this).data('url'), function (e) {
        if (e.status === 'ok') {
            $btn.closest('div#like').find('#like-counter').html(e.counter);
        }
    });
});

$('body').on('click', '#comment-edit', function () {
    var com = $(this);
    $.get($(this).data('url'), function (e) {
        com.closest('div#comments').replaceWith(e);
    })
});

$('body').on('click', '.save', function () {
    var com = $(this);
    var data = com.closest('#comment-edit-form').find('form').serialize();
    $.post($(this).data('url'), data, function (e) {
        if (e.status === 'ok') {
            location.reload();
        }
    })
});

$('body').on('click', '.cancel', function () {
    location.reload();
});

$(document).ready(function () {
    $('[data-btn="modal"]').on('click', function () {
        var selector = $(this).data('target'),
            el = $(selector);
        $.get($(this).data('url'), function (e) {
            $('div.modal-body').html(e);

            if (el.hasClass('in')) {
                el.removeClass('in');
                el.removeClass('show');
            } else {
                el.addClass('in show');
                el.hide()
            }

        })
    });
    $('body').on('click', '[data-close="modal"]', function () {
        $(this).closest('.modal').removeClass('in show')
    })
})