$(document).ready(function () {
    $('.likes').on ('click', function () {

        $.ajax ({
            type: 'GET',
            url: '/instadraw/like/'+$(this).attr('id'),
            data: {},
            success: function (result) {
                console.log ('answer', result['answer']);
                $('.likes').text(result['response']);
            }
        })
        $('#edit_comment').on("click",function(){
            console.log('Here');
            $("#description"+$(this).attr('id')).hide();
            $(".form"+$(this).attr('id')).show();
            $("#"+$(this).attr('id')).hide();
            return false;
        })
        return false;
    });
});