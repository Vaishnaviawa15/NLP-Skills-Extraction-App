NLP-Powered Skill Extractor for Job Descriptions
This repository contains the source code for an interactive web application that automatically extracts and categorizes key skills from job descriptions. This tool is a functional component of a larger capstone project focused on personalized career prediction for students.

Live Application: https://nlp-skills-extraction-app-miniproject.streamlit.app/

1. Project Overview & Problem Solved
Overview
In the vast landscape of job opportunities, understanding the specific requirements for a role is a critical first step. This project provides a web-based tool, built with Python and Streamlit, that leverages Natural Language Processing (NLP) to demystify job descriptions. By simply pasting in the text of a job posting, users can instantly receive a structured list of the essential "Hard Skills" (technical competencies) and "Soft Skills" (interpersonal qualities) required for the position.

The Problem It Solves
For students and aspiring professionals, job descriptions can often be dense, filled with jargon, and difficult to parse. This creates a significant challenge:

Lack of Clarity: It's hard to quickly identify the most crucial skills needed to qualify for a role.

Time-Consuming: Manually analyzing multiple job postings to understand industry trends is inefficient.

Skill Gap Identification: Students may not know which specific skills to focus on developing for their desired career path.

This tool directly addresses these issues by providing an automated, clear, and immediate analysis of job requirements, empowering users to make more informed decisions about their learning and career development.

2. Technical Workflow & Methodology
The application is the result of a systematic data analysis and NLP workflow performed in a series of data science notebooks. The core steps are outlined below.

Step 1: Data Loading & Skill Analysis
Dataset: The project began with a dataset of job postings (all_job_post.csv), which included columns for job descriptions and their associated ground-truth skill sets.

Skill Frequency Analysis: All skills from the dataset were extracted, cleaned (converted to lowercase, stripped of whitespace), and aggregated. A frequency count was performed using Python's collections.Counter to identify the most commonly required skills across thousands of job postings.

Step 2: Building a Data-Driven Skill Dictionary
Categorization Logic: Based on the frequency analysis, the most common skills were selected to form the foundation of our skill dictionary. A function was created to categorize these skills into "Hard Skills" and "Soft Skills" based on a predefined list of technical keywords (e.g., 'sql', 'python', 'data', 'management').

Final Dictionary (DATA_DRIVEN_SKILL_DB): The categorized lists were stored in a Python dictionary. This data-driven dictionary is more robust and relevant than a manually curated list, as it is based on real-world industry data.

Step 3: Text Preprocessing
To prepare the raw job description text for analysis, a standard NLP preprocessing pipeline was implemented:

Lowercasing: All text was converted to lowercase to ensure uniformity.

Punctuation Removal: All punctuation marks were removed using regular expressions.

Tokenization: The cleaned text was broken down into individual words or tokens using nltk.word_tokenize.

Stop Word Removal: Common but non-meaningful words (e.g., "the", "a", "in") were filtered out using NLTK's English stop words list.

Lemmatization: Words were converted to their base or root form (e.g., "running" -> "run", "studies" -> "study") using nltk.WordNetLemmatizer. This helps in matching different forms of the same skill.

Step 4: Skill Extraction Logic
Pattern Matching: The core extraction function iterates through every skill in our custom DATA_DRIVEN_SKILL_DB.

Regex Search: For each skill, it constructs a regular expression pattern (r"\b" + skill + r"\b") to search for the skill as a whole word within the preprocessed job description. The \b ensures that "java" matches "java" but not "javascript".

Output: The function returns a set of all unique skills found in the text.

Step 5: Evaluation
Before building the app, the model's performance was validated against the ground-truth data:

Metrics: Precision, Recall, and F1-Score were calculated to measure the accuracy of the extraction logic.

Error Analysis: False Positives (skills incorrectly extracted) and False Negatives (skills missed) were analyzed. This step was crucial for refining the skill dictionary and improving the model's recall.

3. How to Use the Application
The deployed Streamlit application is simple and intuitive:

Navigate to the application URL.

Find a job description you are interested in and copy its text.

Paste the text into the text area on the web page.

Click the "Extract Skills" button.

The application will display the extracted Hard and Soft Skills in two separate columns.

4. Technologies Used
Language: Python

Web Framework: Streamlit

NLP Library: NLTK (Natural Language Toolkit)

Data Manipulation (for analysis): Pandas
