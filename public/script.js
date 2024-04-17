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
