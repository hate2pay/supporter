
                                $(document).ready(function() {
                                    $("#ajax_link").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Start Link test... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_json",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_mac").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Start MAC test... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_mac",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_ip").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> IP DHCP Snooping test... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_ip",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_cable").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Try to Test Cable ... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_cable",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_portstatus").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Portstatus Test ... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_portstatus",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_port").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Try to Activate Switchport ... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_port",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_info").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Loading Switch Info ... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_info",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_log").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Loading Switch Log... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_log",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
                                $(document).ready(function() {
                                    $("#ajax_multicast").click(function() {
                                    var input_string = $("#forminput").val();
                                    var network_ch = $("#network_ch").val();
                                    var port_ch = $("#port_ch").val();
                                    var switch_ch = $("#switch_ch").val();
                                    var userip = $("#userip").val();
                                    var allinfo = $("#allinfo").val();
                                    var vendor = $("#vendor").val();
                                    $('#result').html('<pre> Multicast Groups Information... </pre>');

                                    $.ajax({
                                            url : "/ajaxexample_multicast",
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
                                            csrfmiddlewaretoken: '{{ csrf_token }}'
                                            },
                                            success : function(json) {
                                            $('#result').html('<pre>' + json.server_response + '</pre>');
                                            },
                                            error : function(xhr,errmsg,err) {
                                            alert(xhr.status + ": " + xhr.responseText);
                                    }
                                    });
                                    return false;
                                    });
                                });
