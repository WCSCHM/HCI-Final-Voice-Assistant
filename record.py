import pyaudio
import wave
import time

RATE = 16000
CHUNK = int(RATE / 10)

def record_audio(duration=5):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("正在录音...")
    frames = []

    end_time = time.time() + duration
    while time.time() < end_time:
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("录音结束")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    audio_data = b''.join(frames)
    
    # 保存音频到文件，检查音质
    with wave.open("output.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)
        wf.writeframes(audio_data)
    
    print("音频已保存为 output.wav")
    
    return audio_data