$(document).ready(function () {
    $('.likes').on ('click', function () {
        console.log ('----> IT DETECTS THE CLICK');
        $.ajax({
            type: 'GET',
            url: '/instadraw/like/'+$(this).attr('id'),
            data: {},
            success: function (result) {
                console.log ('response', result['response']);
                $('.likes').text(result['response']);
            }
        });

        return false;
    });

    $('.edit_comment').on("click",function(){
        $(".form"+$(this).attr('id')).toggle();
        //$("#"+$(this).attr('id')).hide();

        return false;
    });
    $('.edit_description').on("click",function(){
        console.log('Here');
        $(".form"+$(this).attr('id')).toggle();
        //$("#"+$(this).attr('id')).hide();

        return false;
    });
});