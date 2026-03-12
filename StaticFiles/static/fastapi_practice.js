
// practice.js - JavaScript file for FastAPI static file practice

// Show alert when button is clicked
function showMessage() {
    alert("Hello from JavaScript! Your FastAPI static JS file is working.");
}

// Change text dynamically
function changeText() {
    const p = document.getElementById("dynamic-text");
    p.innerText = "The text has been changed using JavaScript.";
}

// Simple counter example
let count = 0;

function increaseCounter() {
    count++;
    document.getElementById("counter").innerText = count;
}

// Simulate fetching data from API
async function fetchData() {
    try {
        const response = await fetch("/api/data");
        const data = await response.json();
        console.log("Data from FastAPI:", data);
        document.getElementById("api-data").innerText = JSON.stringify(data);
    } catch (error) {
        console.error("Error fetching API:", error);
    }
}

// Run when page loads
document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript loaded successfully with FastAPI static files.");
});
