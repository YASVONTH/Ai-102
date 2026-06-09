# AI Email Writer using Streamlit and Gemini AI

## Overview

AI Email Writer is a simple web application built using Streamlit and Google's Gemini AI model. The application generates professional email content based on user input. Users can enter a topic, request, or brief description, and the AI automatically creates a well-structured email.

## Features

* User-friendly Streamlit interface
* AI-powered email generation using Gemini 2.5 Flash
* Instant email creation
* Simple and lightweight implementation
* Suitable for professional, academic, and personal emails

## Technologies Used

* Python
* Streamlit
* Google Generative AI (Gemini API)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-email-writer.git
cd ai-email-writer
```

### 2. Install Required Packages

```bash
pip install streamlit google-generativeai
```

### 3. Configure API Key

Replace the API key in the code with your own Gemini API key.

```python
genai.configure(api_key="YOUR_API_KEY")
```

### 4. Run the Application

```bash
streamlit run app.py
```

## Project Structure

```text
ai-email-writer/
│
├── app.py
├── README.md
└── requirements.txt
```

## Usage

1. Open the application in your browser.
2. Enter the email topic or request in the text box.
3. Click the **Submit** button.
4. The AI generates a professional email based on your input.

## Sample Input

```text
Write an email requesting leave for two days due to personal reasons.
```

## Sample Output

```text
Subject: Leave Request

Dear Manager,

I hope you are doing well. I would like to request leave for two days due to personal reasons. I kindly request you to approve my leave.

Thank you for your understanding.

Best Regards,
Employee
```

## Future Enhancements

* Email subject generation
* Multiple email tone options (Formal, Casual, Professional)
* Copy-to-clipboard feature
* Email export as PDF
* Email templates for various purposes

## Author

Yasvonth V.L.
B.E. Electronics and Communication Engineering (ECE)

## License

This project is open-source and available for educational and learning purposes.
