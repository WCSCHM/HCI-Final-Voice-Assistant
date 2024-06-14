import wave
import json
from vosk import Model, KaldiRecognizer
from config import LANGUAGE_MODELS

# 加载VOSK模型
models = {lang: Model(path) for lang, path in LANGUAGE_MODELS.items()}

def clean_text(text):
    # 移除不必要的空格，并合并可能被分开的词
    text = text.replace(' ', '')
    return text

def transcribe_speech(audio_data, language="zh"):
    wf = wave.open("output.wav", "rb")
    model = models.get(language, models["zh"])
    rec = KaldiRecognizer(model, wf.getframerate())
    
    result_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result_dict = json.loads(result)
            result_text += result_dict.get("text", "")

    final_result = rec.FinalResult()
    final_result_dict = json.loads(final_result)
    result_text += final_result_dict.get("text", "")
    
    wf.close()
    
    cleaned_text = clean_text(result_text)
    print(f"识别结果: {cleaned_text} (Recognition Result: {cleaned_text})")
    return cleaned_text if cleaned_text else None
