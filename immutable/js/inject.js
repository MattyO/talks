function inject_code(code_string, element_id){
    //alert("including code functions");
    $("#" + element_id).append("<pre>" + code_string + "</pre>");
}

function is_special_comment(line, label){
    return line.trim().indexOf("### " + label ) == 0;
}

function is_special_comment_end(line, label){
    return line.trim().indexOf("### end " + label) == 0;
}

function get_label(data, comment_delimiter){
    var data_array =  data.split('\n');
    var the_example = new Array();
    var is_recording = false;

    for( var i = 0 ; i < data_array.length; i++){

        if( is_special_comment_end(data_array[i], comment_delimiter)){
            is_recording = false;
        }

        if(is_recording){
            the_example.push(data_array[i]);
        }

        if(is_special_comment(data_array[i], comment_delimiter)){
            is_recording = true;
        }

    }
    return the_example.join("\n");
}

function inject_example(filename, element_id, label){
    $.ajax({
        url: "code/" + filename,
        dataType: "text",
        error: function(request, status_string, error_string){
            alert(error_string);
        },
        success: function(data, text_status){

            if( label != null){
                code_subset = get_label(data, label);
                if(code_subset != ""){
                    data = code_subset;
                }

            }
            inject_code(data , element_id);
        }
    });
}


            //$.ajax({
            //        url:"code/functional_tools_test.py",
            //        dataType:"text",
            //        error: function(request, status_string, error_string){
            //            alert(error_string);
            //        },
            //        success:function(data, text_status){
            //            var data_array =  data.split('\n')
            //            for( var i = 0 ; i < data_array.length; i++){ 
            //                console.log(data_array[i]);
            //            }
            //        }
            //        });

