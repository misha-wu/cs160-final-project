document.querySelector('.spinnerContainer').style.display = 'none';
document.getElementById('translationContainer').style.display = 'none';

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
});

function submitForm(formElement) {
    var spinnerContainer = document.querySelector('.spinnerContainer');
    spinnerContainer.style.display = 'block'; // Show the spinner container immediately upon form submission

    formElement.submit();

    fetch('/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formElement)
    })
        .then(response => response.json())
        .then(data => {
            // Use the fetched data
            console.log(data);
            document.getElementById('data').innerText = JSON.stringify(data);
        })
        .catch(error => console.error('Error fetching data:', error));
}

function translateText(word_dict) {
    const processId = setTimeout(function () {
        document.getElementById('translationContainer').style.display = 'block'; // Display the translation container
        word_dict.forEach(block => { // Ensure this loop iterates over all blocks
            createDivFromInput(block);
        });
    }, 1500);

    window.processTimeout = processId; // Store the timeout ID for potential future use
}

function adjustFontSize(div) {
    var maxFontSize = 16;  // Maximum font size in pixels
    var minFontSize = 10;  // Minimum font size in pixels
    var scalingFactor = 100;  // Adjust this based on needs
    var contentLength = div.textContent.length;

    var idealFontSize = Math.max(minFontSize, maxFontSize - (contentLength / scalingFactor));
    div.style.fontSize = idealFontSize + 'px';
}

function createDivFromInput(input) {
    try {
        var container = document.getElementById('picContainer');  // Reference to the picContainer
        var rect = container.getBoundingClientRect();  // Get dimensions of the picContainer

        // Get the image element
        var img = document.querySelector('.picContainer img');

        // Wait for the image to load
        img.onload = function() {
            // Get the width and height of the image
            var width = img.width;
        };

        // Create a new div element for the translated text and set its properties
        var div = document.createElement('div');
        div.style.position = 'absolute';
        div.style.left = (input.x / 100 * img.width + (input.w / 100 * img.width)) + 'px';  // Convert percentage to pixels
        div.style.top = ((input.y / 100 * 320)+80) + 'px';
        div.style.width = ((input.w * img.width) *3) + 'px';
        div.style.height = (input.h * 320) + 'px';
        div.classList.add('box');
        div.textContent = input.translation; // Use translation as the text content
        document.body.appendChild(div);  // Append the div to the picContainer

        adjustFontSize(div);  // Assuming adjustFontSize is defined correctly elsewhere

        // Create sentence cards for each keyword
        createKeywordCards(input.keywords, true);
    } catch (error) {
        console.error('Error creating div:', error);
    }
}


function createKeywordCards(keywords, append = false) {
    const container = document.getElementById('translationContainer');
    if (!append) {
        container.innerHTML = ''; // Clear only if not appending
    }

    keywords.forEach(kw => {
        let card = document.createElement('div');
        card.classList.add('sentenceCard');

        let original = document.createElement('p');
        original.classList.add('original');
        original.textContent = kw.phrase;

        let pronunciation = document.createElement('p');
        pronunciation.classList.add('pronunciation');
        pronunciation.textContent = kw.romaji;

        let translation = document.createElement('p');
        translation.classList.add('translation');
        translation.textContent = kw.english;

        // Create Save button
        let saveButton = document.createElement('button');
        saveButton.classList.add('saveButton');
        saveButton.innerHTML = `<i class="fa fa-save"></i> Save`;
        saveButton.onclick = function() {
            saveTranslation(kw);
        };

        card.appendChild(original);
        card.appendChild(pronunciation);
        card.appendChild(translation);
        card.appendChild(saveButton); // Append the Save button to the card

        container.appendChild(card);
    });
}

function saveTranslation(keyword) {
    let savedCards = JSON.parse(localStorage.getItem('savedSentenceCards')) || [];
    savedCards.push(keyword);
    localStorage.setItem('savedSentenceCards', JSON.stringify(savedCards));
    
    showModal(); // Show the modal instead of using alert
}

function showModal() {
    document.getElementById('saveModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('saveModal').style.display = 'none';
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


