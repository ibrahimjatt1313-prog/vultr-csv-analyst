<<<<<<< HEAD
# Vultr CSV Analyst 🚀
*Agent Rush Hackathon Submission*

**Vultr CSV Analyst** is an autonomous, AI-driven data analysis platform that converts natural language analytical prompts into secure, executable Python code. Built for high-speed automated data exploration, it leverages **Google Gemini LLMs** for code generation and provides robust sandboxed execution for deep-dive dataset telemetry.

---

## ✨ Key Features

* **Autonomous Code Generation:** Powered by **Gemini 3.8 Flash**, translating user prompts into clean, optimized pandas and NumPy operations.
* **Dual-Mode Secure Sandbox:** 
  * *Production Mode:* Isolated Docker containers with strict resource caps (Memory & CPU limits, air-gapped network).
  * *Local Development Mode:* Intelligent local secure execution fallback for seamless testing.
* **Advanced Diagnostics:** Automatically computes schema overviews, null-value counts, descriptive summary statistics, median/skew metrics, and ranked feature correlations.
* **Hackathon-Ready UI:** Sleek, responsive dashboard featuring real-time execution counters, security guard status indicators, and clean diagnostic output panels.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Uvicorn, Python
* **AI Engine:** Google GenAI SDK (`google-genai`) & Gemini LLM
* **Data Science Tools:** pandas, NumPy, scikit-learn (optional pipelines)
* **Infrastructure / Security:** Docker, subprocess sandboxing containment filters
* **Frontend:** HTML5, Tailwind CSS, JavaScript

---

## ⚙️ Quick Start & Installation

### 1. Clone & Set Up Virtual Environment
```bash
git clone [https://github.com/ibrahimjatt1313-prog/vultr-csv-analyst.git](https://github.com/ibrahimjatt1313-prog/vultr-csv-analyst.git)
cd vultr-csv-analyst
python -m venv venv
# On Windows:
venv\Scripts\activate
=======
# vultr-csv-analyst
>>>>>>> 8d57875c0b6b79fbfa77b2611b2f1958a7816276
