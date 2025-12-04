<div align="center">

# <strong>ACADEMATE: Intelligent College AI Agent</strong>

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge&logo=github&logoColor=white)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/sahilaw22/google-ai-agent-course-capstone)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

</div>

---

<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=1976D2&center=true&vCenter=true&random=false&width=680&height=90&lines=Unify+College+Knowledge,+Answers+in+Seconds;Trustworthy+Audit-Ready+Intelligence" alt="Typing SVG" />
</div>

---

## 🚀 Why Academate?

**College life is full of fragmented information:** portals, PDFs, emails, and confusion. Academate provides a smarter way for students and faculty to ask, “When is my next exam?” or “Who teaches Data Structures?” and get instant, complete, and audit-ready answers. Powered by Google Gemini 2.5 Flash Lite and GenAI Agent Development Kit, Academate transforms static campus data into interactive intelligence, saving time and reducing error.

---

## 🌟 Key Features

<table align="center">
<tr>
<td align="center"><b>Natural Q&A</b><br>Ask about exams, results, staff, timetable, campus events</td>
<td align="center"><b>Deterministic Tools</b><br>Gemini planner invokes robust, documented Python functions</td>
<td align="center"><b>Session Memory</b><br>Remembers the context of multi-turn conversations</td>
</tr>
<tr>
<td align="center"><b>Observability</b><br>Structured logs for audits & traceability</td>
<td align="center"><b>Evaluation Harness</b><br>Automated testing for reliable answers</td>
<td align="center"><b>Complete Coverage</b><br>Onboard new departments or datasets quickly</td>
</tr>
</table>

---

🏗️ Architecture Overview

![Architecture Diagram](assets/graph_image.png)

* **Gemini LLM:** Understands and plans answers from conversational queries.
* **CSV-backed Tools:** Deterministic Python functions provide reliable information from campus datasets.
* **Session Memory:** Maintains chat history and context.
* **Observability:** Logs every interaction for transparency and governance.
* **Evaluation Harness:** Ensures every answer meets college-grade standards before going live.

---

## 🧮 Tech Stack

<div align="center">

  **Languages:**  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
  ![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)

  **AI Model:**  
  ![Google Gemini 2.5 Flash Lite](https://img.shields.io/badge/Gemini-2.5_Flash_Lite-blue?style=for-the-badge)

  **Framework:**  
  ![Google_ADK](https://img.shields.io/badge/Google_ADK-4285F4?style=for-the-badge)

  **Data:**  
  ![CSV](https://img.shields.io/badge/CSV-FFD700?style=for-the-badge)

  **Quality & DevOps:**  
  ![Session Memory](https://img.shields.io/badge/Session_Memory-6A1B9A?style=for-the-badge)
  ![Structured Logs](https://img.shields.io/badge/Structured_Logs-00897B?style=for-the-badge)

</div>

---

## 📦 Project Structure

```
chatbot/
 ├─ agent.py           # ADK web/cli entry
 ├─ runtime.py         # Gemini core and router
 ├─ tools.py           # Custom campus Q&A tools
 ├─ datasets.py        # Loads & caches campus data
 ├─ memory.py          # Session/context management
 ├─ observability.py   # Structured logs
 ├─ evaluation.py      # Evaluation/test harness
data/
 └─ *.csv              # Timetable, exams, faculty, results
tests/
 └─ test_agent.py      # Unit tests
Academate-College-Chatbot.ipynb  # Walkthrough, reproducibility
logs/
 └─ agent.log          # Interaction logs
```

---

## 🛠️ How to Get Started

### Prerequisites

- Python **3.10+**
- Pip
- Google Cloud Project (**Gemini API enabled**)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/sahilaw22/google-ai-agent-course-capstone.git
   cd google-ai-agent-course-capstone
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment
   - Copy `.env.example` to `.env` and provide your Google API key:
   ```ini
   GOOGLE_API_KEY=your_api_key_here
   AGENT_MODEL=gemini-2.5-flash-lite
   ```

### Running the Agent

- **Web Interface (Recommended):**
  ```bash
  python api/server.py
  # Access: http://localhost:8000
  ```
  
- **ADK Web Interface:**
  ```bash
  adk web Academate
  # Access: http://127.0.0.1:8000
  ```
  
- **Command Line:**
  ```bash
  python -m chatbot.main
  ```

### Testing

```bash
python tests/test_agent.py
python -c "from chatbot.evaluation import run_evaluations; print(run_evaluations())"
```

---

## 🚀 Deployment

Deploy Academate to the cloud with **Vercel** or **Netlify** for global access!

### Quick Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/sahilaw22/google-ai-agent-course-capstone)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/sahilaw22/google-ai-agent-course-capstone)

### Deployment Guide

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

**Key Features:**
- ✅ Web-based chat interface
- ✅ Serverless deployment (no server management)
- ✅ Automatic scaling
- ✅ Free tier available on both platforms
- ✅ Custom domain support

**Required Environment Variables:**
- `GOOGLE_API_KEY` - Your Google Gemini API key
- `AGENT_MODEL` - (Optional) Default: `gemini-2.5-flash-lite`
- `AGENT_TEMPERATURE` - (Optional) Default: `0.7`

---

## 🧪 Sample Queries

- When is my next lab exam?
- Show me the AI timetable.
- Who teaches Ethics?
- Get my SGPA for student ID 2024XYZ.
- Which events are scheduled next week?

---

## 🤝 Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingIdea`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

<div align="center">
MIT License https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge
</div>

---

<div align="center">

![Wave](https://capsule-render.vercel.app/api?type=wave&color=gradient&height=70&section=footer&animation=twinkling)
<br>
Made with passion by <strong>Sahil</strong>
</div>
