# MockLLM-ChatTTS Quick Start and Fine-tuning Guide

## Environment

- **Python Version**: Python 3.10+
Make sure Python 3.10+ is installed and active in your environment.

## Installation

Install the required dependencies with:

```bash
pip install -r requirements.txt
```
## Generate Audio
Run the following command to generate a sample audio file (output.wav):
```
python test.py
```
You can modify the text content inside test.py to generate audio from your custom input.

## Fine-tuning
You can fine-tune the DVAE and GPT modules using your own dataset.

## Prepare Your Data
Prepare your .wav audio files and create a .list file formatted according to the provided examples.

## Fine-tune DVAE
Run the following command:
```
CUDA_VISIBLE_DEVICES=0 python examples/finetune/finetune.py \
  --color \
  --save_folder ./saved_models \
  --data_path yours.list \
  --tar_path data/Xz.tar \
  --batch_size 32 \
  --epochs 10 \
  --train_module dvae
```
## Fine-tune GPT Speaker
Run the following command:
```
CUDA_VISIBLE_DEVICES=0 python -m examples.finetune.finetune \
  --color \
  --save_folder ./saved_models \
  --data_path yours.list \
  --tar_path data/Xz.tar \
  --batch_size 32 \
  --epochs 10 \
  --train_module gpt_speaker
```
Make sure to update data_path to point to your dataset's .list file.

## Post-training Steps
After fine-tuning, compute the SHA256 hash of your trained model and Update the corresponding SHA256 value in sha256_map.json with the output from this script. (need to be updated in the future)

