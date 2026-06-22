# 🎙️ Personal Speech-to-Text (STT) com OpenAI Whisper & Gradio

Um transcritor de áudio pessoal, moderno e 100% gratuito, criado para fugir das assinaturas abusivas de ferramentas web atuais. A aplicação utiliza o modelo open-source **Whisper (base)** da OpenAI e possui uma interface responsiva criada em **Gradio**, hospedada gratuitamente no Hugging Face Spaces.

## 🚀 Tecnologias Utilizadas
* **Python 3.13**
* **OpenAI Whisper (via Transformers)** para transcrição de áudio por IA.
* **Gradio 6** para a interface de usuário (UI/UX) limpa e direta.
* **Hugging Face Spaces** para infraestrutura de deploy contínuo em CPU estável.

## 🛠️ Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone <seu-link-do-github>
Instale as dependências:

Bash
pip install -r requirements.txt

Execute o app:
Bash
python app.py

📈 Histórico de Atualizações (Changelog)
v1.0.0 (Lançamento): Interface funcional com suporte a upload de arquivos (.mp3, .wav, .m4a) e gravação via microfone. Inicialmente travado para processamento em português.
v1.1.0 (Correção de Bug de Idioma): Removido o hardcode de idioma (language="portuguese"), permitindo que o modelo utilize sua capacidade nativa de auto-detecção multilingue, evitando travamentos em áudios estrangeiros.
v1.2.0 (Ajuste de Pipeline & Task):** Corrigido o comportamento onde o modelo aplicava a tarefa nativa de `translate` (tradução automática para o idioma padrão do pipeline) em áudios estrangeiros. Adicionado o argumento `generate_kwargs={"task": "transcribe"}` para forçar o Speech-to-Text puro, garantindo que o áudio seja transcrito exatamente no idioma original em que foi falado.
