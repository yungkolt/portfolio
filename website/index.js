document.addEventListener('DOMContentLoaded', () => {
    const viewerCountElement = document.getElementById('viewer-count');
    fetch('https://7pjovyx7427xl26l6uvpa5sjhi0qffow.lambda-url.us-east-1.on.aws/')
        .then(response => response.json())
        .then(data => {
            viewerCountElement.textContent = data.views;
        })
        .catch(error => console.error('Error fetching viewer count:', error));
});