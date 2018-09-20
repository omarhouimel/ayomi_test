$(document).on('submit',"#form",function(e)
{
    e.preventDefault();

    $.ajax({
        type:'Post',
        url:'/details',
        data:{
            email:$('#emailID').val(),
            csrfmiddlewaretoken:'{{ csrf_token }}'
        },
        success:function(){
            $('#myModal').modal('toggle');
            $('#userID').html($('#emailID').val());


        }
    })



}
)