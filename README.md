# Hannah – An AI Therapist Chat App

**Hannah** is an AI-powered therapy chatbot built to provide a comforting, conversational companion for those experiencing loneliness or lacking someone to talk to. Designed for simplicity and privacy, Hannah offers an open, no-signup chat experience to anyone who starts the app locally.

> *Note: This app is not a substitute for professional mental health services.*

---

## 🧠 About the Project

Hannah was developed as a solo project for a hackathon and later expanded as a portfolio piece. The app is focused on a single, impactful feature: providing therapeutic conversations through a friendly AI chatbot using advanced language models via the OpenRouter API.

---

## ✨ Features

- 💬 **AI Chat Interface** – Talk to Hannah about your day, your thoughts, or just say hi.
- ⚡ **No Signup Required** – Just start the app and begin chatting.
- 🧩 **AI Integration** – Uses AI-generated responses via OpenRouter’s language models.
- 🛠️ **Lightweight Flask App** – Simple to run and easy to understand for developers.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A free API key from [OpenRouter.ai](https://openrouter.ai/)

### Clone and Run Locally

```bash
git clone https://github.com/neb1n/AI-Therapist.git
cd AI-Therapist
python3 -m venv venv
source venv/scripts/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
````

### Setup Environment Variables

Create a `.env` file in the root directory and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your-api-key-here
```

### Run the App

```bash
python main.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python, Flask
* **APIs & Libraries:**

  * [OpenRouter.ai](https://openrouter.ai/)
  * `requests`
  * `python-dotenv`
  * `Flask`

---

## 📂 Project Structure

```
app/
└── templates/
│   └── index.html
└── static/
│   └── style.css
└── main.py
└── __init__.py
└ requirements.txt
```

---

## 📌 Future Plans

* Add mood-tracking or journaling features
* Improve UI/UX design and accessibility
* Deploy the app for live use

---

## 🙋‍♂️ Author

Built with care by **\[Your Name]**
→ GitHub: [https://github.com/neb1n](https://github.com/neb1n)

Feel free to reach out with feedback, ideas, or collaboration proposals!
