# Code-Mixed Sentiment Analysis in Indonesian E-Government

This repository contains the source code, datasets, and documentation for the research paper: **"Code-Mixed Sentiment Analysis in Indonesian E-Government: A Controlled Benchmark of Monolingual vs Multilingual Transformers"**.

This study evaluates the performance of monolingual (IndoBERT) and multilingual (mBERT) Transformer models in classifying public sentiment within three major Indonesian e-government mobile applications (SATUSEHAT, SIGNAL, and IKD). The primary focus of this research is to address the *code-mixing* phenomenon—the pervasive blending of informal Indonesian (*slang*) with English technical terms—using a *controlled benchmarking* approach.

## 📂 Repository Structure

The computational pipeline is divided into 5 main stages that should be executed sequentially:

* **`01_Data_Scraping.py`** : Script to extract user reviews from the Google Play Store utilizing the `google-play-scraper` library.
* **`02_Preprocessing_and_Cleaning.py`** : Handles data cleaning, case folding, and Indonesian slang normalization. Crucially, it is designed to retain *code-mixed* English technical terms (e.g., 'error', 'bug', 'login') to preserve their original socio-technical context.
* **`03_WordCloud_Exploration.py`** : Generates Word Cloud visualizations to explore lexical features and identify dominant foreign technical terminology across different applications.
* **`04_Model_Finetuning_IndoBERT_mBERT.ipynb`** : The core experimental Jupyter Notebook for fine-tuning the pre-trained `indobenchmark/indobert-base-p1` and `bert-base-multilingual-cased` models. 
* **`05_Evaluation_and_Confusion_Matrix.py`** : Script to evaluate model performance using standard metrics (F1-Score, Precision, Recall, Accuracy) and to render high-resolution *Confusion Matrix* visualizations for error analysis.

## 📊 Dataset

The datasets used in this study are located in the `dataset/` directory.

* `raw_dataset.csv` : The original, unedited reviews extracted from the Google Play Store (Total: 14,204 reviews).
* `cleaned_dataset.csv` : The preprocessed dataset, ready for model training and evaluation.

*(Note: The datasets are provided strictly for academic reproducibility. If the files are unavailable directly in this repository due to GitHub's file size limitations, please contact the corresponding author for access).*

## 🚀 How to Run

### Prerequisites
Ensure you have Python 3.8+ installed. It is highly recommended to use a virtual environment.

### Installation & Execution
1. **Clone this repository:**
   ```bash
   git clone https://github.com/nicholaslaverino/proyek-analisis-sentimen.git
   cd your-repo-name

Install the required dependencies:
pip install -r requirements.txt

Run the pipeline:
Execute the scripts sequentially from 01 to 05.

Note: For stage 04 (Model Fine-Tuning), we strongly recommend executing the notebook in Google Colab or a local environment with GPU (CUDA) acceleration enabled to reduce training time.