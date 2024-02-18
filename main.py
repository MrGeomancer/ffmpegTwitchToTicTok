# import ffmpeg
#
# stream = ffmpeg.input(r'in.mp4')
# # stream = ffmpeg.filter(scale='1080:1920', setsar='1:1')
# stream = ffmpeg.filter(stream, 'scale', 'scale=1080:1920, setsar=1:1')
# output_stream = ffmpeg.output(stream,r'out2.mp4')
# ffmpeg.run(output_stream)

import ffmpeg

# Входной видеофайл
input_file = 'in.mp4'

# Задаем входной поток
stream = ffmpeg.input(input_file)

# Фильтры для растягивания и установки соотношения сторон
filter_options = 'scale=1080:1920,setsar=1:1'

# Добавляем фильтр матового стекла
frosted_glass_filter = 'gblur=sigma=3'

# boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg]

# Задаем выходной поток с использованием обоих фильтров
output_stream = ffmpeg.output(stream, 'output_frosted_glass_video5.mp4', vf=f'{filter_options},{frosted_glass_filter}', aspect='9:16')
ffmpeg.run(output_stream, capture_stderr=True, overwrite_output=True, capture_stdout=True)



# Запускаем команду
try:
    ffmpeg.run(output_stream, capture_stderr=True, overwrite_output=True, capture_stdout=True)
except ffmpeg.Error as e:
    print(e.stderr.decode())


