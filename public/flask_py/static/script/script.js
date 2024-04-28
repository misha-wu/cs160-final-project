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

function translateText(word_dict) {
  // Show spinnerContainer when the manga detector is processing
  document.querySelector('.spinnerContainer').style.display = 'block';

  // Charon: please change this interaction to show after the translation is completed
  const processId = setTimeout(function () {
      const systemMessage = document.querySelector(".systemMessage");
      systemMessage.innerText = "loading";
      document.querySelector('.spinnerContainer').style.display = 'none';

      setTimeout(function () {
          document.getElementById('translationContainer').style.display = 'block'; //Charon: please also insert the japanese & translation to the sentence card
          
          createDivFromInput('Hello,56,68,48,129'); //Charon: please replace the content with the right text and coordinations!
          document.getElementById('cancelButton').style.display = 'none';
      }, 10);
  }, 1500); 

  window.processTimeout = processId;
}


function translateText() {
    // Show spinnerContainer when the manga detector is processing
    document.querySelector('.spinnerContainer').style.display = 'block';
    console.log("Get here");
    // Charon: please change this interaction to show after the translation is completed
    const processId = setTimeout(function () {
        const systemMessage = document.querySelector(".systemMessage");

        document.querySelector('.spinnerContainer').style.display = 'none';

        setTimeout(function () {
            document.getElementById('translationContainer').style.display = 'block'; //Charon: please also insert the japanese & translation to the sentence card
            createDivFromInput('Hello,56,68,48,129'); //Charon: please replace the content with the right text and coordinations!
            document.getElementById('cancelButton').style.display = 'none';
        }, 10);
    }, 1500); 

    window.processTimeout = processId;
}

function createDivFromInput(input) {
    try {
        console.log(input);
        // Extract values from input string
        var values = input.split(',');

        // Extract values
        var translatedText = values[0].trim(); // Trim any leading or trailing spaces
        var x = parseInt(values[1].trim()); // Parse x coordinate as integer
        var y = parseInt(values[2].trim()); // Parse y coordinate as integer
        var w = parseInt(values[3].trim()); // Parse width as integer
        var h = parseInt(values[4].trim()); // Parse height as integer

        // Create a new div element
        var div = document.createElement('div');

        // Set position and size
        div.style.position = 'absolute'; // Set position to absolute
        div.style.left = x + 'px';
        div.style.top = y + 'px';
        div.style.width = w + 'px';
        div.style.height = h + 'px';

        // Add class for styling
        div.classList.add('box');

        // Set text content
        div.textContent = translatedText;

        // Append div to the body
        document.getElementById('picContainer').appendChild(div);
        
    } catch (error) {
        console.error('Error creating div:', error);
    }
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

function submitForm(formElement) {
    console.log(formElement);
    formElement.submit();
    fetch('/upload',  {
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

