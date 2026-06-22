import gradio as gr
from transformers import pipeline

# Carrega o modelo Whisper explicitamente configurado para a tarefa de transcrição pura
transcribers = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcrever_audio(audio_path):
    if audio_path is None:
        return "Por favor, envie ou grave um áudio primeiro!"
    
    # Força a tarefa de transcrição pura (sem traduzir) com detecção automática de idioma
    resultado = transcribers(audio_path, generate_kwargs={"task": "transcribe"})
    return resultado["text"]

# Cria a interface do usuário
interface = gr.Interface(
    fn=transcrever_audio,
    inputs=gr.Audio(type="filepath", label="Grave ou envie seu áudio (mp3, wav, m4a...)"),
    outputs=gr.Textbox(label="Texto Transcrito"),
    title="Meu Transcritor Pessoal",
    description="Suba um arquivo de áudio ou grave direto do microfone para transcrever de graça, sem assinaturas!"
)

# Roda o aplicativo
if __name__ == "__main__":
    interface.launch()