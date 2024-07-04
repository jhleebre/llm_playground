function submitOnCtrlEnter(event) {
    if (event.ctrlKey && event.key === 'Enter') {
        document.getElementById('sendButton').click();
    }
}

function showLoading() {
    document.getElementById('sendButton').disabled = true;
    document.getElementById('loading').style.display = 'block';
}

function hideLoading() {
    document.getElementById('sendButton').disabled = false;
    document.getElementById('loading').style.display = 'none';
}

function scrollToBottom() {
    var chatHistory = document.getElementById('history');
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

window.onload = function() {
    scrollToBottom();
    hideLoading();
}
