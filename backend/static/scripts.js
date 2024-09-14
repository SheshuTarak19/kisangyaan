function toggleNav() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    const toggleButton = document.getElementById('nav-toggle');

    // Toggle sidebar open/close
    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        mainContent.classList.remove('shifted');
        toggleButton.textContent = '☰ Open Sidebar';
    } else {
        sidebar.classList.add('open');
        mainContent.classList.add('shifted');
        toggleButton.textContent = '× Close Sidebar';
    }
}

// scripts.js

// Function to toggle the sidebar visibility
function toggleNav() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar.style.display === 'block') {
        sidebar.style.display = 'none';
    } else {
        sidebar.style.display = 'block';
    }
}

// Voice search functionality
const startButton = document.getElementById('startVoice');
const voiceOutput = document.getElementById('voiceOutput');
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    voiceOutput.textContent = transcript;

    // Send the transcript to the backend
    fetch('/voice-search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: transcript }),
    });
};

startButton.addEventListener('click', () => {
    recognition.start();
});
function toggleNav() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    if (sidebar.style.transform === 'translateX(-250px)') {
        sidebar.style.transform = 'translateX(0)';
        mainContent.style.marginLeft = '250px';
    } else {
        sidebar.style.transform = 'translateX(-250px)';
        mainContent.style.marginLeft = '0';
    }
}
