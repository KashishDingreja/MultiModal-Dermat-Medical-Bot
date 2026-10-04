import os
from groq import Groq


def record_audio(*args, **kwargs):
    """
    Placeholder retained for compatibility with the original project structure.
    Audio recording is handled by the Gradio microphone component.
    """
    return None


def transcribe_with_groq(
    GROQ_API_KEY,
    audio_filepath,
    stt_model="whisper-large-v3"
):
    """
    Transcribe an audio file using Groq's Whisper API.

    Parameters:
        GROQ_API_KEY: Groq API key.
        audio_filepath: Path to the recorded audio file.
        stt_model: Whisper model used for transcription.

    Returns:
        Transcribed text.
    """

    if not audio_filepath:
        return ""

    api_key = GROQ_API_KEY or os.environ.get("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not configured.")

    client = Groq(api_key=api_key)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=stt_model,
            response_format="text",
        )

    if hasattr(transcription, "text"):
        return transcription.text

    return str(transcription)
