#integration_test.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.pipeline_service import ResumePipelineService

service = ResumePipelineService()

# result = service.analyze(
#     "Python developer with ML experience",
#     "Looking for ML engineer"
# )

# print(result)

# resume = """
# Python developer with experience in machine learning,
# APIs, and backend systems.
# """

# jd = """
# We are looking for a machine learning engineer with experience in APIs and deployment.
# """

resume = """
Professional Summary
AI/ML Engineer with hands-on experience in building end-to-end machine learning systems, including data preprocessing,
model development, and deployment. Skilled in Python, Scikit-learn, and real-world ML applications such as healthcare
prediction, NLP, and recommendation systems. Strong software engineering background with experience in scalable systems
and cloud infrastructure. Passionate about solving real-world problems using data-driven and AI-powered solutions.
Technical Skills
Programming Languages: Python, SQL, C++
Machine Learning & Deep Learning: Scikit-learn, TensorFlow, PyTorch, Data Preprocessing, Feature Engineering
Data Analysis & Visualization: Pandas, NumPy, Matplotlib, Seaborn
NLP & Computer Vision: NLTK, Transformers, OCR (Tesseract)
Deployment & Backend: FastAPI, Streamlit, Docker
Cloud & DevOps: AWS (EC2, S3, IAM), Kubernetes (Basics)
Tools: Git, GitHub, Linux
Projects
HireSense AI: LLM-Based Resume Intelligence Engine | Python, OpenAI API, NLP, Sentence Transformers, Streamlit
• Developed an LLM-powered system to evaluate resumes against job descriptions using semantic similarity and
embedding techniques.
• Implemented cosine similarity-based scoring to quantify job-fit relevance between candidate resumes and job
requirements.
• Improved resume-job matching accuracy by leveraging transformer-based embeddings over traditional keyword
matching.
• Built a skill gap analysis module to identify missing keywords, competencies, and critical skills for targeted roles.
• Designed prompt-engineered pipelines using OpenAI API to generate actionable resume improvement suggestions.
• Utilized Sentence Transformers for efficient text embedding and contextual similarity matching.
• Deployed an interactive Streamlit application enabling real-time resume feedback and ATS-style evaluation.
• Enhanced user experience with clear scoring metrics, improvement insights, and structured feedback reports.
Customer Churn Prediction (End-to-End) | Python, Scikit-learn, Pandas, NumPy, Flask, Streamlit
• Developed an end-to-end machine learning model to predict customer churn using behavioral, service usage, and
billing data.
• Performed data cleaning, feature engineering, and exploratory data analysis (EDA) to uncover key churn patterns and
improve model performance.
• Trained and evaluated multiple classification models including Logistic Regression, Random Forest, and XGBoost,
achieving high accuracy and improved recall for churn class.
• Handled class imbalance using SMOTE to enhance prediction performance for minority churn cases.
• Deployed the model using Flask and Streamlit, enabling real-time churn prediction through an interactive interface.
• Identified key drivers of churn such as contract type, tenure, and monthly charges, supporting business
decision-making.
Spotify Songs’ Genre Segmentation | Python, Machine Learning, Pandas, NumPy, Scikit-learn
• Built a machine learning system to classify and segment songs into genres using audio features such as tempo, energy,
and danceability.
• Analyzed large datasets to identify patterns and correlations between musical attributes and genres.
• Applied clustering and classification techniques including K-Means and supervised learning models.
• Improved recommendation system capabilities through data-driven insights.
Image2Insight: OCR-Based Sentiment Analysis System | Python, NLP, NLTK, Pytesseract, VADER
• Designed and developed an end-to-end OCR and NLP pipeline to extract text from images and perform sentiment
analysis.
• Implemented text preprocessing techniques including cleaning, tokenization, and stopword removal to improve
analysis accuracy.
• Integrated Tesseract OCR for efficient text extraction and VADER for sentiment classification into positive, negative,
and neutral categories.
• Enabled automated analysis of visual text data for applications such as customer feedback interpretation and decision
support.
Internship
Corizo Edutech Nov 2025 – Dec 2025
Artificial Intelligence Intern
• Completed an internship focused on Artificial Intelligence and Machine Learning concepts and practical
implementation.
• Worked extensively with NumPy, Pandas, and Scikit-learn for data preprocessing, analysis, and model building.
• Implemented various machine learning algorithms including regression, classification, and clustering techniques.
• Gained hands-on experience in end-to-end ML workflows, from data cleaning and feature engineering to model
evaluation and optimization.
IITM Pravartak Technologies Foundation (TIH of IIT Madras) & L&T Edutech 11 Jun 2025 – 17 Sep 2025
Artificial Intelligence & Edge Computing Intern
• Completed a 14-week intensive internship focused on Artificial Intelligence and Edge Computing, jointly
conducted by IITM Pravartak Technologies Foundation and L&T Edutech.
• Gained hands-on experience in AI fundamentals, edge computing architectures, and deploying intelligent models
closer to data sources for low-latency processing.
• Worked on real-world use cases involving data preprocessing, model inference, and system-level understanding of
AI-enabled edge devices.
• Developed a strong foundation in applying AI solutions to industry-relevant problems with a focus on performance,
scalability, and efficiency.
LTI Mindtree Feb 2023 – Apr 2023
Cloud Engineer Intern Bengaluru, Karnataka
• Completed an internship focused on cloud computing technologies with hands-on experience in AWS services
including VPC, IAM, EC2, and S3.
• Gained practical experience in Terraform for infrastructure provisioning and AWS resource management.
• Worked on Kubernetes deployments, learning container orchestration fundamentals and basic deployment
strategies.
• Collaborated with team members to design scalable cloud architectures, following AWS best practices and
supporting Kubernetes workloads.
Experience
LTI Mindtree Jun 2024 – Present
Software Engineer (Platform & Distributed Systems)
• Engineered and maintained event-driven messaging solutions using Solace PubSub+ for CITI Bank across PROD,
COB, UAT, and SIT environments.
• Designed and implemented Message VPNs, client configurations, and bridges to enable secure and scalable
communication between distributed systems.
• Developed and automated backup, recovery, and monitoring processes, improving system reliability and reducing
manual intervention.
• Implemented secure certificate management and optimized endpoint configurations to ensure high availability and
data integrity.
• Collaborated in infrastructure upgrades, including hardware replacements and SAN migration, ensuring seamless
system performance with minimal downtime.
• Debugged and resolved production issues using log analysis and system tracing, enhancing application
performance and ensuring SLA compliance.

"""

jd = """
Description

GlobalLogic is a leading digital product engineering services company that helps clients design and build innovative products, platforms, and digital experiences. Operating as a Hitachi Group Company, We specialize in merging experience design, complex engineering, and data expertise across industries like automotive, healthcare, and technology.

Requirements

Required Skills & Qualifications

Bachelor's/Master's degree in Computer Science, AI, Data Science, or related field.

Strong programming skills in Python.

Experience with ML frameworks such as TensorFlow, PyTorch, or Scikit-learn.

Hands-on experience with data manipulation libraries (Pandas, NumPy).

Experience in model deployment using APIs, Docker, or cloud platforms (AWS/Azure/GCP).

Solid understanding of machine learning algorithms and deep learning architectures.

Knowledge of SQL and working with large-scale datasets.

Experience with version control systems (Git).

Preferred Qualifications

Experience with Generative AI and LLMs (OpenAI, Hugging Face, LangChain, etc.).

Exposure to vector databases and embeddings.

Knowledge of MLOps tools (MLflow, Kubeflow, Airflow).

Experience in building AI-powered chatbots or automation tools.

Familiarity with CI/CD pipelines.

Soft Skills

Strong analytical and problem-solving skills.

Excellent communication and collaboration abilities.

Ability to work in a fast-paced, dynamic environment.

Self-driven and innovation-oriented mindset.

Job responsibilities

Key Responsibilities

Design, develop, and deploy machine learning and deep learning models.

Build scalable AI solutions and integrate them into production systems.

Work with large datasets: data preprocessing, feature engineering, and model validation.

Develop NLP, computer vision, recommendation systems, or predictive analytics solutions (as applicable).

Fine-tune and deploy large language models (LLMs) where required.

Optimize models for performance, scalability, and reliability.

Implement MLOps pipelines for model monitoring, retraining, and versioning.

Collaborate with cross-functional teams to translate business requirements into AI solutions.

Stay updated with latest advancements in AI and emerging technologies.
"""

result = service.analyze(resume, jd)
print(result)


# print("First run")
# print(service.analyze("Python developer with ML experience", "Looking for ML engineer"))

# print("Second run")
# print(service.analyze("Python developer with ML experience", "Looking for ML engineer"))