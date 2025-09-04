#  Week1

This repository contains the tasks completed as part of my daily learnings.

---
### Day1_Basics_of_Python
- Built a fully functional To-Do List application using **Streamlit**.
- Features:
  - Add, edit, delete tasks
  - Mark tasks as complete
  - Display completed and deleted tasks
  <img width="1912" height="882" alt="tasktrek" src="https://github.com/user-attachments/assets/e6b53fa0-9576-455a-aa06-79b964dbde30" />

### Day2_Basics_of_Cloud
  - **S3 Bucket:**
  - Created and uploaded folders/files to AWS S3.
- **EC2 Instance:**
  - Launched a virtual machine on AWS EC2.
- **Lambda Function:**
  - Developed a basic Python function deployed using AWS Lambda.

### Day3_Basics_of_GenAI
#### Task1_Rainbow_Response_HF
- Accepts custom prompts or uses default: _"Explain how rainbows are formed"_
- Uses **Groq LLM (LLaMA 3)** for generating explanations
- Displays AI explanation in clean paragraphs
- Generates a **vertical flowchart** visualizing the rainbow formation process
- Provides tips and fun facts about light, reflection, and dispersion
<img width="1910" height="1015" alt="r11" src="https://github.com/user-attachments/assets/c270ee1d-f869-48f2-a882-84636d909562" />
<img width="1918" height="1020" alt="r12" src="https://github.com/user-attachments/assets/c8feeeb7-8327-4325-9995-354741039011" />

#### Task2_Ocean_Poem_HF
Users can input their poem preferences:
- **Topic** – e.g., love, rain, friendship, stars
- **Tone** – emotional, funny, romantic, etc.
- **Length** – number of lines
  <img width="1915" height="886" alt="poem" src="https://github.com/user-attachments/assets/6cb81880-595d-4750-8a8b-afbb6d381f57" />

### Day4_Basics_of_RAG
#### Task1_TextSplitter_LangChain
- Loads text with `TextLoader` (for `.txt`) or `PyPDFLoader` (for `.pdf`)
- Splits documents into overlapping chunks for processing
- Prints the total number of chunks generated
#### Task2_RetrievalQA
- Build a simple PDF-based RAG chatbot using LangChain and Groq API.  
- Extract text from PDF, embed it, index it with FAISS, and use LLM to answer user queries.
- Features
  - Upload any **PDF** file
  - Automatic **text chunking**
  - **Semantic search** using FAISS
  - LLM-powered answers with **Groq LLaMA3**
  - Interactive **Streamlit UI**
  - Displays **retrieved context chunks**
<img width="1907" height="887" alt="image" src="https://github.com/user-attachments/assets/7118380a-3817-431c-a492-a4d176b922a9" />

### Day5_Amazon_Bedrock
#### Task1_Bedrock_Project_Deployment
Features
- Real-time chat interface using Bedrock LLM
- Clear Chat button to reset conversation
- Export chat as **PDF** or **TXT**
- Sidebar with static health & nutrition tips
<img width="1916" height="893" alt="bedrock" src="https://github.com/user-attachments/assets/5c71c5f5-f742-4fa3-ad67-3b5d51ae9e10" />

### Additional Task: AWS Lambda + Amazon Bedrock (Prompt-Response Integration)

As part of the additional task given, I successfully implemented a Lambda function that interacts with Amazon Bedrock to send a prompt and receive a response.

#### Tools & Technologies:
- AWS Lambda
- Amazon Bedrock (`meta.llama3-70b-instruct-v1:0`)
- Python (`boto3`)
- API Gateway (for external trigger)

