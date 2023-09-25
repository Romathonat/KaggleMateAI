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

KaggleMateAI offers a conversational CLI experience. To start interacting with the tool, simply run:

``` bash
kagglemateai
```

Example interaction:

    **KaggleMateAI**: Give me the description of the problem you want to tackle
    **You**: I'm working on a text classification problem with this and that contraint ...
    **KaggleMateAI**: Here are some Kaggle competitions that might be relevant [Title - Descriptions - URL]
    ...
    Which one do you want to choose ?
    **You**: The first one
    **KaggleMateAI**: Here is a summary of the problem tackled here, and why it is linked to your problem [description]
    Here is also the list of possible solutions    
    [solution name - URL]
    ...
    **You**: Tell me more about solution 2
    **KaggleMateAi"**: [description + step by step with code to apply to your problem]

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.