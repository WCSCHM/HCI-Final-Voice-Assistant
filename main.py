from app import process_command

if __name__ == "__main__":
    duration = 5  # 录音时长（秒）
    text, result = process_command(duration=duration)
    print(f"识别文本: {text}")
    print(f"执行结果: {result}")