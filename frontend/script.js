async function sendMessage() {
  const messageInput = document.getElementById('message');
  const chatBox = document.getElementById('chat-box');
  const message = messageInput.value.trim();
  
  if (!message) return;

  chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;
  messageInput.value = '';

  const response = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: message })
  });

  const data = await response.json();
  chatBox.innerHTML += `<p><b>Gemini:</b> ${data.response}</p>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
