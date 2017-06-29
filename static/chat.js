$('#chat-form').on('submit', function(event){
    event.preventDefault();
    $.ajax({
        url : '/send',
        type : 'POST',
        data : { 'msgbox' : $('#chat-msg').val() },
        success : function(json){
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="ChatLog__entry ChatLog__entry_mine"><p class="ChatLog__message">' + json.msg + '</p></li>');
        }
    });
});

var myVar;

function myFunction() {
    myVar = setInterval(getmessage, 500);
}

function getmessage() {
    $.get('/message', function(messages){
            $('#msg-list').html(messages);
	    $('#sl').scrollTop($('#sl')[0].scrollHeight); 
        });
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
