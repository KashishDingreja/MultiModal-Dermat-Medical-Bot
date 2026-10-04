# Multimodal AI Medical Assistant

A multimodal AI assistant prototype that combines **medical image analysis, voice input, speech-to-text, and text-to-speech** to support interactive medical/dermatology-related queries.

The application allows a user to provide a voice query and an image, processes the voice input using Whisper, analyzes the image and query using a LLaMA Vision model through Groq, and returns both a text and voice response through a Gradio interface.

> **Disclaimer:** This project is an educational prototype and is not intended to provide medical diagnosis or replace advice from a qualified healthcare professional. AI-generated responses may be inaccurate or incomplete.

## Features

* **Image + Text Analysis**
  Analyze an uploaded image together with a user's query using a LLaMA Vision model.

* **Voice Input**
  Convert spoken queries into text using OpenAI Whisper through the Groq API.

* **Multimodal AI Response**
  Combine the transcribed query and uploaded image as inputs to a vision-language model.

* **Text-to-Speech**
  Convert the generated response into spoken audio using Google Text-to-Speech (gTTS).

* **Optional ElevenLabs TTS**
  Includes an ElevenLabs-based text-to-speech implementation for alternative voice generation.

* **Gradio Interface**
  Provides a simple interface for microphone and image inputs and displays the transcript, generated response, and audio output.

## System Workflow

```text
                ┌──────────────────┐
                │      User        │
                └────────┬─────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
          Voice Input           Image Input
              │                     │
              ▼                     │
       Whisper via Groq             │
              │                     │
              ▼                     │
       Transcribed Query            │
              │                     │
              └──────────┬──────────┘
                         ▼
                 LLaMA Vision
                  via Groq API
                         │
                         ▼
                 Generated Response
                         │
                         ▼
                     gTTS
                         │
                         ▼
                  Voice Response
```

## Tech Stack

| Component             | Technology                   |
| --------------------- | ---------------------------- |
| Interface             | Gradio                       |
| Vision-Language Model | LLaMA Vision                 |
| Model API             | Groq                         |
| Speech-to-Text        | Whisper                      |
| Text-to-Speech        | Google Text-to-Speech (gTTS) |
| Alternative TTS       | ElevenLabs                   |
| Programming Language  | Python                       |

## Project Structure

```text
MultiModal-Dermat-Medical-Bot/
│
├── brain_of_the_doctor.py      # Image encoding and LLaMA Vision interaction
├── gradio_app.py               # Main Gradio application
├── voice_of_the_patient.py     # Voice transcription using Whisper via Groq
├── voice_of_the_doctor.py      # Text-to-speech implementations
├── Finetuning.ipynb            # Model experimentation / fine-tuning notebook
├── README.md
├── .env                        # API keys - do not commit
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/KashishDingreja/MultiModal-Dermat-Medical-Bot.git
cd MultiModal-Dermat-Medical-Bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

Install the required Python packages for the project:

```bash
pip install gradio groq gTTS pygame elevenlabs
```

If additional packages are required by your local environment, install them before running the application.

### 4. Configure API keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

The Groq API key is required for speech transcription and vision-model inference.

The ElevenLabs key is only required if the ElevenLabs TTS implementation is used.

**Never commit API keys or other secrets to GitHub.**

### 5. Run the application

```bash
python gradio_app.py
```

The Gradio interface will open locally.

## Usage

1. Open the Gradio interface.
2. Record a question using the microphone.
3. Upload an image for visual analysis.
4. Submit the inputs.
5. The application:

   * transcribes the voice query,
   * sends the query and image to the LLaMA Vision model,
   * generates a text response,
   * converts the response into speech.
6. Review the generated response and audio output.

## Dataset

The project was developed around dermatology-related use cases and references the **DermNet dataset** for medical image experimentation.

Dataset reference:

https://www.kaggle.com/datasets/shubhamgoel27/dermnet

The current application should be considered a multimodal AI prototype rather than a clinically validated image-classification system.

## Limitations

* The generated responses are produced by a general-purpose vision-language model and may contain incorrect or incomplete information.
* The system has not been clinically validated.
* Image analysis should not be treated as a medical diagnosis.
* Performance depends on the underlying model and API services.
* The current implementation is designed primarily as an educational and experimental project.

## Future Improvements

* Add retrieval-augmented generation (RAG) using reliable medical sources.
* Introduce structured medical response formats and stronger safety constraints.
* Add systematic evaluation using a curated medical image/query benchmark.
* Improve error handling and API failure recovery.
* Add persistent conversation history.
* Containerize and deploy the application.
* Improve accessibility and multilingual interaction.

## Disclaimer

This project is intended **for educational and research purposes only**. It should not be used for medical diagnosis, treatment decisions, or emergency situations. Always consult a qualified healthcare professional for medical concerns.
