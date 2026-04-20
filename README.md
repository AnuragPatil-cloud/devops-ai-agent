# 🚀 DevOps AI Agent — AWS Infrastructure Auditor (using AWS CLI)

An AI-powered DevOps agent that audits your AWS infrastructure using **AWS CLI + LangChain + Gemini (LLM)** and provides intelligent insights like a senior DevOps engineer.

---

## 📌 Project Overview

This project builds an **AI DevOps Agent** that:

* Connects to AWS using CLI
* Fetches infrastructure data (EC2, S3, VPC, CloudWatch)
* Uses Gemini AI to analyze resources
* Generates **automated DevOps recommendations**

---

## 🧠 How It Works

```
User Goal → AI Thinks → Calls AWS CLI → Gets Data → Analyzes → Final Answer
```

This follows the **ReAct (Reason + Act)** pattern:

* **Tools (AWS CLI)** → Real data
* **LLM (Gemini)** → Intelligence
* **Agent** → Connects both

---

## ⚙️ Tech Stack

* Python 3.12
* AWS CLI
* LangChain
* Google Gemini API
* Linux (Ubuntu)

---

## 📂 Project Structure

```
devops-ai-agent/
├── agent.py              # Agent logic (brain)
├── tools.py              # AWS tools (hands)
├── test.py               # Gemini test
├── requirements.txt      # Dependencies
├── README.md
└── .gitignore
```

---

## 🔧 Setup Instructions (Local Ubuntu)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AnuragPatil-cloud/devops-ai-agent.git
cd devops-ai-agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Configure AWS CLI

```bash
aws configure
aws sts get-caller-identity
```

---

### 5️⃣ Setup Environment Variables

Create `.env` file:

```bash
GOOGLE_API_KEY=your_api_key_here
```

---

### 6️⃣ Run Agent

```bash
python3 agent.py
```

---

## 📊 Example Output

```
> Entering new AgentExecutor chain...
Thought: I need to check S3 buckets
Action: get_s3_buckets
Observation: No S3 buckets found

...

✅ INFRASTRUCTURE SUMMARY
- EC2 instances running without monitoring
- No CloudWatch alarms configured
- Potential security risks detected
```

---

## 🛠️ Features

* AWS resource discovery
* Automated infrastructure audit
* AI-powered recommendations
* Modular tool-based architecture
* Extensible for DevOps use cases

---

## 🔥 Future Enhancements

* IAM security audit
* Cost optimization agent
* Slack/Email alerts
* Kubernetes integration
* CI/CD pipeline integration

---

## 🧠 Key Concepts

* ReAct AI Agents
* Infrastructure as Code mindset
* DevOps automation with AI
* AWS CLI integration with Python

---

## 🐛 Troubleshooting

| Issue                 | Fix                          |
| --------------------- | ---------------------------- |
| AWS credentials error | Run `aws configure`          |
| API key error         | Check `.env` file            |
| Module not found      | Activate virtual environment |
| LangChain errors      | Use compatible versions      |

---

## 📦 Requirements

Example `requirements.txt`:

```
langchain==0.1.16
langchain-community==0.0.32
langchain-google-genai==0.0.11
langchainhub
python-dotenv
rich
```

---

## 🚀 Resume Highlight

**Built an AI-powered DevOps agent using AWS CLI, LangChain, and Gemini to audit cloud infrastructure and generate automated insights and recommendations.**

---

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests.

---




