document.getElementById('summarizeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var topic = document.getElementById('topic').value;
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'topic=' + encodeURIComponent(topic)
    })
    .then(response => response.text())
    .then(html => {
        document.querySelector('body').innerHTML = html;
    })
    .catch(error => console.error('Error:', error));
});
