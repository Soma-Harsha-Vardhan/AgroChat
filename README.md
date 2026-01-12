🌾 AgroChat — Multimodal AI Assistant for Crop Disease & Pest Diagnosis

AgroChat is a research-grade, AI-driven conversational assistant designed to help farmers, students, and agricultural professionals diagnose crop diseases and pest infestations using images, text queries, and environmental context.
It combines computer vision, large language models, and retrieval-augmented generation (RAG) to deliver accurate, explainable, and weather-aware agricultural recommendations.

📌 What makes AgroChat different?

Unlike traditional agriculture apps that only return a disease label or generic advice, AgroChat:

Understands plant and insect images

Reads user-written symptom descriptions

Uses agricultural knowledge bases

Considers real-time weather

And generates grounded, step-by-step treatment guidance

This makes AgroChat a true multimodal AI system, not just a chatbot.

🧠 Core AI Pipeline

AgroChat integrates four AI components:

1️⃣ Plant CNN (EfficientNet-B0)
Classifies plant leaf images into 15 disease categories.

2️⃣ Insect CNN (EfficientNet-B0)
Identifies harmful agricultural pests from images.

3️⃣ Retrieval-Augmented Generation (RAG)
A ChromaDB vector database retrieves:

Symptoms

Causes

Treatments

Preventive measures

4️⃣ Large Language Model (LLaMA-3.2 1B)
Generates natural-language explanations and actionable advice grounded in retrieved agricultural knowledge.

5️⃣ Weather-Aware Reasoning
A weather API injects humidity, rainfall, and temperature into the prompt so AgroChat can adapt recommendations (e.g., avoid spraying before rain).

🏗️ System Architecture
User (Image + Text)
        ↓
Frontend (Web UI)
        ↓
Backend (FastAPI)
        ↓
Plant CNN / Insect CNN
        ↓
RAG (ChromaDB Knowledge Retrieval)
        ↓
LLaMA 3.2 (LLM)
        ↓
Weather-Aware Prompting
        ↓
Final Diagnosis & Treatment Advice

🗂️ Datasets Used
Dataset	Purpose	Classes
PlantVillage	Plant disease detection	15 diseases
Farm Insect Dataset	Insect classification	15 pests

Images are resized to 224×224, normalized, and augmented for robustness.

📚 Knowledge Base

For every disease and pest, AgroChat stores:

Visual symptoms

Biological causes

Organic & chemical treatments

Environmental conditions

Fertilizer and crop-care guidelines

These are embedded using a sentence-transformer model and stored in ChromaDB for semantic search.

📊 Model Performance

The CNN models show:

High accuracy

Strong F1-scores

Balanced precision and recall

Using RAG improved:

Response accuracy by 22.7%

Context relevance by 27.4%

Reduced hallucinations by 74.9%

🖥️ Features

📷 Upload plant or insect images

💬 Ask natural-language questions

🌦️ Weather-aware advice

📊 Confidence-based diagnosis

📚 Knowledge-grounded responses

🧑‍🌾 Farmer-friendly explanations

🚀 Why AgroChat Matters

AgroChat is designed for real-world farming, especially in rural or low-connectivity environments:

Works with small models

Runs on low-cost hardware

Reduces dependency on experts

Prevents wrong chemical usage

Helps improve crop yield & safety

📌 Research Context

AgroChat is part of a research project titled:
“AgroChat: A Retrieval-Augmented Multimodal Assistant for Crop Disease and Pest Diagnosis”

It demonstrates how CNNs + RAG + Vision-Language Models can be combined to create trustworthy agricultural AI systems.

🛠️ Tech Stack

Python

FastAPI

PyTorch

EfficientNet-B0

LLaMA 3.2 (1B)

ChromaDB

Sentence Transformers

OpenWeather API
