import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak("我的名字是lcwspr")
speaker.Speak("hello world")
