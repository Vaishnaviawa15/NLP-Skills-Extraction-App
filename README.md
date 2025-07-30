🚀 NLP Skill Extractor
<p align="center">
A Streamlit web app that uses NLP to instantly extract hard and soft skills from job descriptions.
</p>

<p align="center">
<img alt="Python" src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.9%252B-blue%3Fstyle%3Dfor-the-badge%26logo%3Dpython">
<img alt="Streamlit" src="https://www.google.com/search?q=https://img.shields.io/badge/Streamlit-1.10%252B-red%3Fstyle%3Dfor-the-badge%26logo%3Dstreamlit">
<img alt="NLTK" src="https://www.google.com/search?q=https://img.shields.io/badge/NLTK-3.7%252B-green%3Fstyle%3Dfor-the-badge%26logo%3Dnltk">
</p>

<p align="center">
<!-- IMPORTANT: To make this work, record a short GIF of your app and upload it to a site like imgur.com. Then, replace the URL below with your GIF's URL. -->
<img src="https://www.google.com/search?q=https://i.imgur.com/your_gif_url_here.gif" alt="App Demo GIF" width="750"/>
</p>

📋 Table of Contents
About the Project

Key Features

Technologies Used

Project Workflow

Live Application

🎯 About the Project
For students and professionals, job descriptions are often dense and difficult to parse. This tool solves that problem by providing an automated, clear, and immediate analysis of job requirements. It helps users quickly identify the crucial skills needed for a role, understand industry trends, and pinpoint personal skill gaps for career development. This application is a key component of a larger capstone project on personalized career prediction.

✨ Key Features
Automated Skill Extraction: Instantly parses job descriptions to identify key skills.

Hard & Soft Skill Categorization: Intelligently separates technical abilities from interpersonal qualities.

Data-Driven Dictionary: Utilizes a skill dictionary built from analyzing thousands of real-world job postings.

Interactive Web Interface: A simple and user-friendly interface powered by Streamlit.

Real-Time Analysis: Provides immediate feedback with no wait time.

🛠️ Technologies Used
Python: Core programming language.

Streamlit: For building the interactive web application.

NLTK (Natural Language Toolkit): For NLP tasks like tokenization, stop word removal, and lemmatization.

Pandas: Used for data manipulation and analysis during the initial research phase.

⚙️ Project Workflow
The application's logic was developed through a systematic NLP process:

Data Analysis: Analyzed a large dataset of job postings to identify the most frequent skills.

Dictionary Creation: Built a custom, data-driven skill dictionary categorized into "Hard" and "Soft" skills.

Text Preprocessing: Established a pipeline to clean and prepare raw text for analysis (lemmatization, stop word removal, etc.).

Skill Extraction: Implemented a regex-based pattern matching system to find and extract skills from the processed text.

Validation: Evaluated the model's accuracy using metrics like Precision and Recall before deployment.

🌐 Live Application
You can access and use the live application here:

https://nlp-skills-extraction-app-mini.streamlit.app/
