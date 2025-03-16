# Import necessary libraries and configure settings
# -*- coding: utf-8 -*-
import torch
import torchaudio

# If you're using torch._dynamo features, ensure you have PyTorch 2.0+.
# Otherwise, you can comment out the following lines:
torch._dynamo.config.cache_size_limit = 64
torch._dynamo.config.suppress_errors = True
torch.set_float32_matmul_precision('high')

import ChatTTS
from IPython.display import Audio

# Initialize and load the model:
chat = ChatTTS.Chat()
chat.load(compile=False)  # Set to True for better performance if desired
print("Model loaded successfully!")

# Define the text input for inference (Support Batching)
texts = [
    "四川美食主要以麻辣鲜香为主，较为著名的就是四川火锅。 不管是寒冷的冬季还是炎热的夏季，都是当地人非常喜爱的。 另外还有宫保鸡丁、干烧鱼、回锅肉、麻婆豆腐、夫妻肺片"
    ]

# Perform inference and play the generated audio
wavs = chat.infer(texts)
Audio(wavs[0], rate=24000, autoplay=True)

# Convert the generated audio (assumed to be a NumPy array) to a 2D tensor.
# torchaudio.save expects a tensor with shape [channels, samples].
wav_tensor = torch.from_numpy(wavs[0])
if wav_tensor.ndim == 1:
    wav_tensor = wav_tensor.unsqueeze(0)  # Convert from [samples] to [1, samples]

# Save the generated audio to output.wav at a sample rate of 24000 Hz.
torchaudio.save("output.wav", wav_tensor, 24000)


