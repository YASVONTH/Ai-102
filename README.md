# AI Content Generator using Gemini & Streamlit

## Overview

This project is a simple AI-powered content generation application built using **Python**, **Streamlit**, and **Google Gemini API**. It provides two useful tools:

1. **AI Email Writer** – Generates professional emails based on user input.
2. **AI Blog Post Generator** – Creates blog content for any topic provided by the user.

The application uses the Gemini 2.5 Flash model to generate high-quality text responses quickly.

## Features

### AI Email Writer

* Generates professional and well-structured emails.
* Accepts user requirements as input.
* Produces clear and formal email content instantly.

### AI Blog Post Generator

* Creates informative blog posts on any topic.
* Generates readable and engaging content.
* Useful for students, content creators, and bloggers.

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Gemini 2.5 Flash Model

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-content-generator.git
cd ai-content-generator
```

### Step 2: Install Required Packages

```bash
pip install streamlit google-generativeai
```

### Step 3: Run the Application

For Email Writer:

```bash
streamlit run email_writer.py
```

For Blog Generator:

```bash
streamlit run blog_generator.py
```

## Project Structure

```
AI-Content-Generator/
│
├── email_writer.py
├── blog_generator.py
├── requirements.txt
└── README.md
```

## How It Works

1. Enter a topic or prompt in the text box.
2. Click the **Submit** button.
3. The application sends the prompt to the Gemini model.
4. Gemini generates the requested content.
5. The generated output is displayed on the Streamlit interface.

## Example Use Cases

### Email Writer

Input:

```
Write a leave request email for two days.
```

Output:

```
A professional leave request email addressed to the manager.
```

### Blog Generator

Input:

```
Artificial Intelligence in Healthcare
```

Output:

```
A detailed blog post discussing AI applications in healthcare.
```

## Future Enhancements

* Email subject generation
* Multiple writing styles
* Content download option
* Blog length selection
* Dark mode interface
* PDF export functionality

## Author

**V. L. Yasvonth**
B.E Electronics and Communication Engineering (ECE)

## License

This project is developed for educational and learning purposes.
