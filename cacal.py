import ffmpeg

# Исходное видео
input_video = 'in.mp4'

# Название выходного файла
output_video = 'output6.mp4'
output_audio = 'output_audio2.aac'  # Указываем файл для сохранения аудио

# Создаем процесс конвертации
ffmpeg.input(input_video).output(output_video, vf='scale=1080:1920', vcodec='libx264', acodec='aac', strict='experimental').run()
ffmpeg.input(input_video).output(output_audio, acodec='aac', map='a').run()
