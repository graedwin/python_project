$(document).ready(function () {
    $('.likes').on ('click', function () {
        var likes_amout = $('.likes').text();

        console.log ($(this).attr('id'));

        $.ajax ({
            type: 'GET',
            url: '/instadraw/like/'+$(this).attr('id'),
            data: {},
            success: function (result) {
                console.log ('answer', result['answer']);
                $('.likes').text(result['response']);
            }
        })
        //document.forms["likes"].submit();
        //$(this).text(likes_amount+1);
        return false;
    });
});