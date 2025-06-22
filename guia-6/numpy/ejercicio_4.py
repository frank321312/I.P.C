import numpy as np

x = np.arange(10)

y = 1/(x+1)

media = y.mean()

defirencia_media = y - media

print(f"media: {media}")
print(f"y - media: {defirencia_media}")
