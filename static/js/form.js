/*$(document).ready(function() {

    $('form').on('submit', function(event){

        $.ajax({
            data:{sCodCor : $('#sCodCor').val()},
            type: 'POST',
            url: '/searchItem'
        })
        .done(function(data){
            if(data.error){
                $('#sCodCor').text(data.error).show();
            }
            else{
                $('#sCodCor').text(data.sCodCor).show();
            }
        })
        event.preventDefault();

    });
}); */