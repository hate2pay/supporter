$(document).ready(function() {
    $(".tools > div").click(function() {
    var testId = $(this).attr('value');
    var input_string = $("#forminput").val();
    var network_ch = $("#network_ch").val();
    var port_ch = $("#port_ch").val();
    var switch_ch = $("#switch_ch").val();
    var userip = $("#userip").val();
    var allinfo = $("#allinfo").val();
    var vendor = $("#vendor").val();
    switch (testId) {
        case '1':  $('#result').html('<pre> Start Link test... </pre>');
            break
        case '2':  $('#result').html('<pre> Start Cable test... </pre>');
            break
        case '3':  $('#result').html('<pre> Start MAC test... </pre>');
            break
        case '4':  $('#result').html('<pre> Start IP test... </pre>');
            break
        case '5':  $('#result').html('<pre> Start Switchport Status test... </pre>');
            break
        case '6':  $('#result').html('<pre> Try to Activate Switchport... </pre>');
            break
        case '7':  $('#result').html('<pre> Try to get Switch Information... </pre>');
            break
        case '8':  $('#result').html('<pre> Try to get Switch Log... </pre>');
            break
        case '9':  $('#result').html('<pre> Try to get Multicast Groups Information... </pre>');
            break
        default: $('#result').html('<pre> It doesn\'t work test... Test with such testId does not exist</pre>');
    }
    $.ajax({
        url : "/ajax_tools",
        type : "GET",
        dataType: "json",
        data : {
        client_response : input_string,
        network_ch : network_ch,
        port_ch : port_ch,
        switch_ch : switch_ch,
        userip : userip,
        allinfo : allinfo,
        vendor : vendor,
        test_id : testId
        },
        success : function(json) {
        $('#result').html('<pre>' + json.server_response + '</pre>');
        }
    });//ajax_end
    });//click end
});