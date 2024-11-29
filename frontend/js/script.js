const socket = new WebSocket('ws://localhost:5001');

socket.onmessage = function(event) {
    const chatContent = document.getElementById('chatContent');
    const data = JSON.parse(event.data);
    chatContent.innerHTML += `<p>${data.sender}: ${data.message}</p>`;
};

function sendEmotion(emotion) {
    fetch('/emotion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ emotion })
    }).then(response => response.json())
      .then(data => console.log(data));
}

function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    const message = { sender: 'User', message: userInput };
    socket.send(JSON.stringify(message));
    document.getElementById('userInput').value = '';
}
