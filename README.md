# Presenting Mangalingua - the AI Manga Translator and Japanese Learning App!
### Contributors: Apratim Banerjee, Michelle Wu, Chia-Jung Kuo, Yuhan Chen
Note: This project is part of the CS 160/260A course final project, [UI/UX Design and Development](https://www2.eecs.berkeley.edu/Courses/CS160) at UC Berkeley. This readme first dives into a brief introduction of the project and an app demo, followed by instructions to run the repo by yourself locally!

## Introduction
Many language-learners seek to broaden their abilities through consumption of media they already enjoy, such as movies, TV shows, and books. One such popular medium for Japanese language-learners is comics, or “manga”. However, there is a lack of a reliable tool to give valuable feedback on their learning. They also aren’t sensitive to the Japanese dialect and their references. Current learning apps generally cater to a broad range of language learners, offering structured lessons and exercise, whereas translation apps focus on general translation and fail to cover fictional aspects, cultural references, and nuances. 

We created an app that allows users to upload manga pages easily that get translated to English, with the translated text overlayed on top of the original text. It also uses AI to save specific vocabulary, nuances, and phrases relevant to the comic book. Users can save these into their word bank for easy reference and learning. We stuck to a minimalistic design for the web app, manga themed. We ensured all standard UI/UX practices were maintained, and Heuristic Evaluations not violated. 

For capturing the Japanese text from images, we used the Optical character recognition (OCR) model and Open Computer Vision (Open CV) libaries. We located and saved the conversation bubble location first. Then the Japanese text was extracted line by line, vertically and converted to English using GPT. Once the entire text within the bubble was translated, we overlayed it with the English text. This all happens in seconds and users can enjoy translated text in real-time. GPT also captured the verbs and nuances from the image as word cards that the user could save to their own word bank. 



## Customer and Market Research
We interviewed a varied set of subjects within a specific group of users. Interviewees varied in age (low to mid 20’s), gender, language fluency, occupancy, and hobbies. 
All target users were interested in learning languages, preferably through reading media, and had a cumbersome existing method of learning.

After doing market research, we realized that Language learners, both familiar with the language and beginners, currently rely on various online tools like Google Translate, Naver, and Easy German to translate media content such as books, switching between source text and translation apps to comprehend meanings. Desired tasks include smoother translations considering character names and nuances, a dictionary function for saving phrases and their translations, understanding grammatical structures, and comparing source text to translations for review. Users typically learn these tasks intuitively, iterating through different segments for translation and adjusting for inaccuracies. Tasks are predominantly performed at home, 
where users have the necessary privacy and time for learning. Users consume processed data to check understanding and utilize applications to support comprehension through translation and vocabulary analysis. They access tools like phones and computers to select text from images for translation and may use auxiliary apps to store personal vocabulary. Communication between users is unnecessary as the app is designed for solo use. Task frequency varies from every few days to once a day, serving as a supplement to other learning methods. Challenges arise when translations are incorrect, hindering comprehension and potentially leading to misunderstandings of context, interfering with language learning goals.

## Demo



## Run the app by yourself!

If you're here after accepting a GitHub Classroom assignment, you'll have your own copy of this starter repository in your GitHub account.
You can [clone it](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the typical way, using the `git` commandline tool.

It's important to **clone** the repository rather than just downloading its contents (say, as a ZIP file).
That way, you'll be able to [commit and push](https://docs.github.com/en/get-started/using-git/about-git) your changes back to the repository when you've finished the assignment, which you **are required to do** so that we can see and grade your code.

You're welcome to use a non-commandline Git client (like [GitHub Desktop](https://desktop.github.com/)) for your Git operations, but you'll need to use the commandline for the next step.
On Windows, this will probably be PowerShell; on macOS, you can use the zsh Terminal application; and other operating systems will have their own commandline software (e.g. `bash` and `gnome-terminal` on some Linux installations).
You may also be able to use a terminal built into your text editor, like VS Code or vim.

## Running the server

Make sure you have recent versions of `node` and `npm` installed (definitely at least version 12 of Node).
Installation instructions for most operating systems are available [on the Node.js website](https://nodejs.org/en/download).
You can check your `node` and `npm` versions using the following commands:

```bash
node --version
npm --version
```

Node.js is a tool that enables you to run JavaScript code outside of the web browser; it's a full-featured language runtime just like the `python3` or `java` command, and you can build desktop software using Node.js.
In this case, we'll use it to run a simple Web server that serves files from the project directory.
Although the code in `server.js` is written in JavaScript just like the JavaScript code within the `public/` directory, the code runs very differently.
In the &ldquo;real world&rdquo;, as a Web developer, you would run `server.js` on some computer you control in the cloud (say, an Amazon AWS server).
When people visit your website, they download HTML, CSS, and JavaScript code from your server, and that frontend code runs on their own computer.

Since you're developing this project locally, all of the code will live and run on your own computer.
Code in `server.js`, however, runs within the Node.js runtime, and the downloaded code in the `public/` directory will run within your web browser, which communicates with the web browser much as it would communicate with a real remote server when you typically brows the Internet.

### Installing the server dependencies

This repository contains a `package.json` file, which is the standard way to tell Node.js some information about the program, including what libraries are needed to run the server code.
The server software requires an external library called [Express](https://expressjs.com/), which makes it easy to develop Web servers.

Run the `install` command in `npm`, Node's default package manager:

```bash
npm install
```

This will read `package.json`, then look to the [NPM package repository](https://www.npmjs.com/) to grab the appropriate dependencies.

### Run the server

Run the server script on your development computer:

```bash
node server.js
```

This will start a long-running process (though you should be able to stop it with `Ctrl+C` or by closing your terminal window).
The server binds to `localhost:8000`, by default, meaning you should be able to access the web server by visiting [http://localhost:8000](http://localhost:8000) in your Web browser.

If you need to change the port or host, the server code will also accept a port number or host from the environment, which looks like this on macOS or Linux:

```
HOST=0.0.0.0 PORT=3000 node server.js
```

This is handy if you already have a process running on port 8000 or if you need to bind to a more public network interface (typically useful **if you want to connect to the server from other devices on your network**, like a mobile phone).

### Poke around

You may not need to make any changes to the server code for your assignment, but it doesn't hurt to read the code and try making some changes.
Since you're using version control, you can always reset the server code if you break anything!
Make sure to stop and restart the server each time you make changes.

I've written some code comments to point out various Express features that control the server's behavior.


### Competitors 
<li> Drops: This app demonstrates the application of Visual Mnemonic and interaction-based vocabulary learning. However, it’s still hard to bridge the real-world usage since the given teaching contents including vocabulary and illustrations are far from the user’s real life, which might increase the memory burden. 
 </li>
<li> Google Translate: While Google Translate is an accessible option, the quality of its results make it difficult for language learners to accurately translate entertainment content, which is often long-winded and context heavy. Our app will also support user-specific content – such as “saved” vocabulary and phrases – to engage learning better. </li>
<li> Jiandanci: The app successfully combines learning the vocabulary with language context with the help of media, enabling people to understand the way to use certain words. Unlike our app, Jiandanci is more focused on memorization and exams – both of which are very formal situations requiring a distinct set of vocabulary. This means that Jiandanci is not as applicable to our form of media – written and/or illustrated.
 </li>
<li> Pimsleur: A versatile and portable learning platform that combines audio-centric learning with comprehensive reading lessons, voice recognition, and gamified elements. It stands out in emphasis on practical conversational skills making it suitable for a wide range of learners. However, potential improvements in visual interaction could elevate the user experience, particularly incorporating media such as books, movies, and tv-shows as a learning tool for users. </li>
<li> Naver: This is a leisure app which can be used for advanced Korean learners with the means of media including news, songs, and video. It also helps learners to understand unfamiliar expressions with their built-in dictionary app. However, it takes some time to switch from the media to the dictionary. Besides, the built-in dictionary has a limited vocabulary and cannot always accurately translate slangs or new expressions. 
</li>
