# Coqui-Text-To-Speech-Synthesis

## Project Overview
This repository is dedicated to the Text-to-Speech synthesis project using the [coqui-TTS toolkit](https://github.com/coqui-ai/TTS/tree/dev), focusing on synthesizing five different sentences using three distinct TTS models. These models are accessible via the `list_models` command and were chosen to showcase a variety of voice synthesis capabilities. The project demonstrates practical applications and experimentation with modern speech synthesis techniques, using each of the three models to create the same set of sentences, testing different types of expressions such as questions and negations.

## Motivation
The goal of this project is to explore and understand the capabilities of different TTS models in producing clear and natural-sounding speech, aiding in the development of more effective communication tools and applications.

## Technologies Used
- Python
- coqui-TTS
- IPython for audio playback

## Installation
To set up this project for use or development, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/spymavro/Coqui-Text-To-Speech-Synthesis.git
   cd Coqui-Text-To-Speech-Synthesis
2. **Install the required Python packages**:

- Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
- It's recommended to create a virtual environment to keep dependencies required by different projects separate and to avoid conflicts:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
- Install the required packages:
  ```bash
  pip install -U pip
  pip install TTS
  pip install -U tensorflow
  # Uncomment to install the development version from GitHub
  # pip install git+https://github.com/coqui-ai/TTS@dev

3. **Proceed with project setup and usage as required**:
### Explanation:
- **Step 1**: Cloning the repository is straightforward; make sure to replace `spymavro` with your actual GitHub username.
- **Step 2**: This step covers:
  - Checking for Python installation.
  - Setting up a virtual environment, which is optional but recommended.
  - Direct installation of each required Python package using `pip`.

## Usage
- Navigate to the cloned directory in your terminal and execute the coqui_TTS script by running:
  ```bash
  python coqui_TTS.py 

**Note**: Next to `--text` write the text you want to synthesize and next to `--speaker_idx` select the speaker you want. Repeat the process for different models and sentences as required.

## Examples
Here are some examples of synthesized sentences using different models:
1. **Model 1 (xtts_v2)**: "Don't you agree that the last two weeks at the university were very tiring?"
2. **Model 2 (fast_pitch)**: "I went shopping at the supermarket at 6 pm because I was missing a lot of things and then I came home and cooked lasagna."
3. **Model 3 (tortoise-v2)**: "Do not use ready-made solutions from the internet. This way you will not learn to handle TTS systems correctly."

**Note**: The synthesized speech examples are demonstrated using various sentences and models. The synthesized outputs are saved as `.wav` files, which can be listened to using the IPython display in the notebook.

## Results
The results section will detail the evaluation of synthesized speech from three different models based on their intelligibility and naturalness, rated on a scale from 1 to 5. The evaluation process involves Mean Opinion Scores from multiple reviewers. Youn can check the documentation for Mean Opinion Scores at the slides [Speech Synthesis](https://speech.zone/media/images/Simon_King_Speech_Synthesis_slides_module05_reduced.pdf) by Simon King (University of Edinburgh).

## Contact
For any inquiries or collaboration requests, please reach out via GitHub or email at spyros.mauromatis@gmail.com.



