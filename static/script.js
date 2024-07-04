// Function to submit the form when Ctrl+Enter is pressed
function submitOnCtrlEnter(event) {
    if (event.ctrlKey && event.key === 'Enter') {
        document.getElementById('sendButton').click();
    }
}

// Function to show the loading indicator and disable the send button
function showLoading() {
    document.getElementById('sendButton').disabled = true;
    document.getElementById('loading').style.display = 'block';
}

// Function to hide the loading indicator and enable the send button
function hideLoading() {
    document.getElementById('sendButton').disabled = false;
    document.getElementById('loading').style.display = 'none';
}

// Function to scroll to the bottom of the chat history
function scrollToBottom() {
    var chatHistory = document.getElementById('history');
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

// Function to initialize the page on load
window.onload = function() {
    scrollToBottom();
    hideLoading();
}
