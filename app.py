from record import record_audio
from speech_text import transcribe_speech
from actions import perform_action

def process_command(duration=5, language="zh"):
    print("开始处理命令 (Starting command processing)")
    audio_data = record_audio(duration=duration)
    print("音频录制完成，开始识别 (Audio recording complete, starting recognition)")
    text = transcribe_speech(audio_data, language=language)
    if text:
        print(f"识别文本: {text} (Recognized text: {text})")
        result = perform_action(text)
    else:
        print("识别失败，没有文本返回 (Recognition failed, no text returned)")
        result = {"status": "failed", "command": None}
    return text, result
