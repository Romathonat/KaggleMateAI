# KaggleMateAI
## :warning: Project Status: Prototype Phase :warning:

This project is currently in the prototype phase and is subject to changes. While it aims to achieve the features listed below, please note that not all have been implemented yet. 

## Overview

KaggleMateAI is an open-source tool designed to assist data scientists and machine learning enthusiasts in navigating the vast landscape of Kaggle competitions. Utilizing Language Model (LLM) techniques, KaggleMateAI not only finds competitions that are similar to your machine learning problem description but also suggests top-performing solutions from those competitions.

## Features
- Competition Discovery: Find Kaggle competitions that match your specific machine learning problem.
- Solution Retrieval: Get top-performing Kaggle notebooks as potential solutions
- AI-Powered Generation: Utilizes state-of-the-art Language Models to understand the context and semantics of your machine learning problem to suggest solutions adapted to your problem.
- Up-to-Date: Constantly updated to include the latest Kaggle competitions.

## Installation

```bash
git clone https://github.com/romathonat/KaggleMateAI.git
cd KaggleMateAI
pip install -r requirements.txt
```

## Usage

```python

from kagglemateai import KaggleMateAI

# Initialize
km = KaggleMateAI(api_key="your_kaggle_api_key")

# Find competitions
competitions = km.find_competitions("your_problem_description")

# Get solutions
solutions = km.get_solutions(competitions)
```

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.