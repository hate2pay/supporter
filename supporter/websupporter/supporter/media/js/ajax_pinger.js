$(document).ready(function() {
    $("#run").click(function() {
        setTimeout(function() {
            location.reload(); 
        }, 2000)
    $.ajax({
        url : "/pinger/run",
        type : "GET",
        dataType: "json",
        data : {
        },
        success : function(json) {
        $('#result').html('<pre>' + json.server_response + '</pre>');
        //setTimeout(function(){$('#result > pre').fadeOut('fast')},50000);
        }
    });//ajax_end 
    });//click end
});
$(document).ready(function() {
    $(".pinger_info > #stop").click(function() {
        setTimeout(function() {
            location.reload(); 
        }, 2000)
    $.ajax({
        url : "/pinger/stop",
        type : "GET",
        dataType: "json",
        data : {
        },
        success : function(json) {
        $('#result').html('<pre>' + json.server_response + '</pre>');
        setTimeout(function(){$('#result > pre').fadeOut('fast')},5000);
        }
    });//ajax_end
    });//click end
});
/*setInterval(function(){
        $.ajax({
        url : "/pinger/stop",
        type : "GET",
        dataType: "json",
        data : {
        },
        success : function(json) {
        $('#result').html('<pre>' + json.server_response + '</pre>');
        setTimeout(function(){$('#result > pre').fadeOut('fast')},5000);
        }
        });
}, 6000);*/
