# Real-Time RAG App with ChromaDB & Ollama

## 📌 Project Overview
This is a **Real-Time Retrieval-Augmented Generation (RAG) application** that:
- **Ingests new text files** in real time.
- **Stores document embeddings in ChromaDB**.
- **Retrieves relevant documents** for user queries.
- **Generates AI responses using a local model** (Llama 3 or Mistral via Ollama).

## 🚀 Features
✅ **Real-time data ingestion** (auto-detects new files in `data/` folder)
✅ **Fast retrieval** using ChromaDB
✅ **AI-generated answers** powered by a local LLM (Llama 3 / Mistral via Ollama)
✅ **Interactive Web UI** built with Streamlit
✅ **Completely offline (No OpenAI API needed)**

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/real-time-rag-app.git
cd real-time-rag-app
```

### **2️⃣ Create & Activate Virtual Environment**
```sh
python -m venv env  # Create virtual environment
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Install Ollama & a Local Model**
1. Download & Install Ollama: [https://ollama.com](https://ollama.com)
2. Pull a model (choose one):
   ```sh
   ollama pull llama3   # Llama 3 model
   ollama pull mistral  # Mistral model
   ```

---

## 🚀 Running the App
### **1️⃣ Start Real-Time Ingestion**
```sh
python ingest.py
```
📂 **Add new text files to `data/` folder** – they will be automatically indexed!

### **2️⃣ Query the Data in Terminal**
```sh
python vector_store.py
```
💬 **Enter your question**, and the system will retrieve relevant documents & generate an AI response using Ollama!

### **3️⃣ Run the Web UI**
```sh
streamlit run app.py
```
🌐 Open `http://localhost:8501` in your browser to use the interactive UI.

---

## 📁 Folder Structure
```
real-time-rag-app/
│── data/                  # Folder for text documents
│── env/                   # Virtual environment (not uploaded)
│── vector_db/             # ChromaDB vector database (not uploaded)
│── ingest.py              # Real-time ingestion script
│── vector_store.py        # Retrieval and AI response script
│── app.py                 # Streamlit Web UI
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
│── .gitignore             # Ignore unnecessary files
```

---

## 📌 Notes
- **This project runs fully offline** (no OpenAI API required).
- **Replace `llama3` with `mistral`** in `vector_store.py` and `app.py` if you prefer Mistral.
- **Make sure Ollama is running before testing AI responses!**



