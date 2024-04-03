document.addEventListener('DOMContentLoaded', function () {
    // Wait for the DOM to be fully loaded
    const headerElement = document.querySelector('header');

    // It Checks if the <header> element exists
    if (headerElement) {
        // It Updates text color to red (#FF0000)
        headerElement.style.color = '#FF0000';
    }
});
