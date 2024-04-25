document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".container");
    const title = document.querySelector(".title");

    // Show the container with animation
    container.style.display = "flex";
    container.style.animation = "fadeInFromRight 1.5s ease-in-out";

    // Show the title after a delay
    setTimeout(function () {
        title.style.visibility = "visible";
    }, 500); // Delay in milliseconds, matches animation delay
});

document.addEventListener("DOMContentLoaded", function () {
    const japaneseBtn = document.querySelector(".languageContainer .language:first-child");
    const englishBtn = document.querySelector(".languageContainer .language:last-child");
    const container = document.querySelector(".container");
    const title = document.querySelector("#title");
    const translationContainer = document.getElementById('translationContainer');

    // Show the container with animation
    container.style.display = "flex";
    container.style.animation = "fadeInFromRight 1.5s ease-in-out";

    // Show the title after a delay
    setTimeout(function () {
        title.style.visibility = "visible";
    }, 500); // Delay in milliseconds, matches animation delay

    // Event listener for English button
    englishBtn.addEventListener("click", function() {
        translationContainer.style.display = 'block'; // Show the processing animation
        translateText(); // Assuming translateText() is the function to start the translation process
    });

    // Event listener for Japanese button (optional functionality)
    japaneseBtn.addEventListener("click", function() {
        // Optional: Code to handle when Japanese is selected, if needed
        alert("Japanese selected"); // For example purposes, replace with your actual function
    });
});

function translateText() {
    // Simulate translation process
    const processId = setTimeout(function () {
        const systemMessage = document.querySelector(".systemMessage");
        systemMessage.textContent = "Translation complete!"; // Update message after "processing"
    }, 5000); // Adjust time as needed for your use case

    // Store the timeout ID in a global variable for cancellation
    window.processTimeout = processId;
}

function stopProcessing() {
    clearTimeout(window.processTimeout); // Stop the simulated processing
    const translationContainer = document.getElementById('translationContainer');
    translationContainer.style.display = 'none'; // Hide the processing animation
    const systemMessage = document.querySelector(".systemMessage");
    systemMessage.textContent = "Processing canceled."; // Optional feedback message
}

function handleFileUpload(input) {
    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (event) {
            const imageUrl = event.target.result;
            console.log("Image URL:", imageUrl);
            // Update the src attribute of the img tag with the data URL
            document.getElementById("uploadedImage").src = imageUrl;
        };
        reader.readAsDataURL(file);
    }
}

