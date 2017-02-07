$(function(){

    function loadBookForm(){
         var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'GET',
            dataType: 'json',
            beforeSend: function(){

                $('#modal-book').modal('show');
            },
            success: function(data){
                $('#modal-book .modal-content').html(data.html_form);

                 $('.calender').datepicker({
                    format: 'dd/mm/yyyy',
                    todayHighlight: true,
                    autoclose: true,
                    orientation: "bottom auto",
                    language: 'pt-BR',

                });

            }
        });
    };

    function saveBookForm(){

            var form = $(this);
            $.ajax({

                url: form.attr('action'),
                type: form.attr('method'),
                data: form.serialize(),
                dataType: 'json',

                success: function(data){

                    if(data.form_is_valid){

                        $('#modal-book').modal('hide');
                        $('#table-book tbody').html(data.html_table);

                         alert(data.success_message);

                    }else{

                        $('#modal-book .modal-content').html(data.html_form);

                    }
                },
            });
        return false;
    };



    // save book
        $('#add-new').click( loadBookForm );
        $('#modal-book').on('submit' , '.js-create-form', saveBookForm );


    // update book
        $('#table-book').on('click', '.js-update-btn' , loadBookForm);
        $('#modal-book').on('submit' , '.js-update-form', saveBookForm);

    // delete book
        $('#table-book').on('click', '.js-delete-btn' , loadBookForm);
        $('#modal-book').on('submit' , '.js-delete-form', saveBookForm);

    // load page

    //  search bottom


        $('.js-search-btn').click(function(){

           var form = $('.js-search-form');
           $.ajax({
                url: form.attr('action'),
                type: form.attr('method'),
                dataType: 'json',
                data:  form.serialize(),
                success: function(data){
                    $('#table-book tbody').html(data.html_table);
                    $('#pagination').html(data.html_pagination);


                },
           });

        });




});