#!/bin/bash

# Activate environment (opsional, sesuaikan path)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run generator.py --server.port 8502 --server.enableCORS false
