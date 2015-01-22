var counterSocket = new WebSocket('ws://localhost:5000/counter');
counterSocket.onopen = function() {
    counterSocket.send('socket open');
};
counterSocket.onclose = function(evt) {
    alert('socket closed');
};

var blob;
counterSocket.onmessage = function(evt) {
    var counterSpan = document.getElementById('counter');
    console.log(evt);
    blob = evt.data;
    counterSpan.textContent = evt.data;

    // Wait a few seconds before incrementing. Increasing the visitors
    // constantly isn't accurate.
    setTimeout(sendMessage, 2000);
};

function sendMessage() {
    counterSocket.send('ping');
}
