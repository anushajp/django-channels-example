$(function() {
    // When we're using HTTPS, use WSS too.
    // Correctly decide between ws:// and wss://
    console.log("hello from chat.js");
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    console.log("SDF")
    var ws_path = ws_scheme + '://' + window.location.host + window.location.pathname + "stream/";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);
    var socket1 = new ReconnectingWebSocket(ws_path);

    socket.onmessage = function(message)
    {
        // Decode the JSON
        console.log("Got message ");
        var data = JSON.parse(message.data);
        var from_user = data.from_user;
        var message = data.message;
        var newdiv = $("<div class='chat-message'>"+message+"<span class='message-by'> - "+from_user+"</span></div>");

        $(".chat-message:first").before(newdiv);
    };
    $("#send").click(function(){
        var msg = $("#message").val()
        var user = $("#username").val()
        socket.send(JSON.stringify({"msg":msg, "user":user}));
    });

    socket.onopen = function()
    {
        console.log("Connected to notification socket");
    }
    socket.onclose = function() { console.log("Disconnected to notification socket"); }
});