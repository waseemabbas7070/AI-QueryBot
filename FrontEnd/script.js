function sendMessage() {
    const input = document.getElementById('user-input');
    const output = document.getElementById('chat-output');
    const question = input.value.trim();
    
    if (question) {
        // Display user's question
        output.innerHTML += `<p><strong>You:</strong> ${question}</p>`;
        
        // Make API call to backend
        fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                output.innerHTML += `<p><strong>AI:</strong> ${data.answer}</p>`;
            } else {
                output.innerHTML += `<p><strong>AI:</strong> Error: ${data.error}</p>`;
            }
            output.scrollTop = output.scrollHeight;
        })
        .catch(error => {
            output.innerHTML += `<p><strong>AI:</strong> Sorry, an error occurred: ${error.message}</p>`;
            output.scrollTop = output.scrollHeight;
        });
        
        input.value = '';
    }
}

document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Check if API is healthy on page load
fetch('/api/health')
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch(error => console.error('API health check failed:', error));