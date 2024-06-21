# SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words

[![huggingface](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-SD--Eval-blue)](https://huggingface.co/datasets/amphion/SD-Eval)
[![arXiv](https://img.shields.io/badge/arXiv-2406.13340-b31b1b.svg)](https://arxiv.org/abs/2406.13340)

SD-Eval is a benchmark dataset aimed at multidimensional evaluation of spoken dialogue understanding and generation.
SD-Eval focuses on paralinguistic and environmental information and includes 7,303 utterances, amounting to 8.76 hours of speech data.
The data is aggregated from eight public datasets, representing four perspectives: emotion, accent, age, and background sound.

## Preparations

```bash
git clone https://github.com/amphionspace/SD-Eval.git
cd SD-Eval
pip install -r requirements.txt
```

## Load SD-Eval

### Download Data
Firstly, please access and download the datasets you need by the following table.

| Test Set | Dataset    | Link |
| -------- | -------- | ------- |
| test-emo | RAVDESS <br> JL Corpus <br> MEAD | [Link](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)  <br> [Link](https://www.kaggle.com/datasets/tli725/jl-corpus)<br>[Link](https://wywu.github.io/projects/MEAD/MEAD.html)  |
| test-acc | VCTK <br> Common Voice v16.1 | [Link](https://datashare.ed.ac.uk/handle/10283/2651) <br> [Link](https://commonvoice.mozilla.org/en/datasets)   |
| test-age | MyST | [Link](https://boulderlearning.com/resources/request-the-myst-corpus/)|

For the required audio files for each subset, please refer to the JSON files in the [data](https://github.com/amphionspace/SD-Eval/tree/main/data) folder.
The audio files should be organized in a folder following the specified layout.
Let us assume that this folder is named ```audio_data``` and the path of the folder is named ```audio_path```.
The layout of the ```audio_data``` folder should be as:
```
  # audio_data
  # ├── RAVDESS-Speech
  # │   ├── Actor_0X
  # │       ├── XXX.wav
  # │       ├── ...
  # │   ├── ...
  # ├── JL_Corpus
  # │   ├── XXX.wav
  # │   ├── ...
  # ├── MEAD
  # │   ├── MEAD_wav
  # │       ├── WXXX
  # │           ├── audio
  # │               ├── XXX
  # │                   ├── level_X
  # │                       ├── XXX.wav
  # │                       ├── ...
  # │       ├── ...
  # ├── VCTK 
  # │   ├── XXX.flac
  # │   ├── ...
  # ├── common_voice
  # │   ├── XXX.mp3
  # │   ├── ...
  # ├── myst
  # │   ├── XXX.flac
  # │   ├── ...
```

Note that you may need to convert the m4a files of MEAD into wav files. An example script for converting using ffmpeg is 
```bash
for file in MEAD/*/audio/*/*/*.m4a; do
    new_path="${file/MEAD/"MEAD_wav"}"
    parentdir="$(dirname "$new_path")"
    mkdir -p ${parentdir}
    ffmpeg -i "$file" -acodec pcm_s16le -ar 16000 -ac 1 "${new_path%.m4a}.wav"
done
```

### Huggingface Datasets
Then you can load SD-Eval using the Huggingface Datasets. Please use the  ```audio_path``` as the ```data_dir``` as introduced before. Note that the synthesized speech data for test-env and test-age can be downloaded on [Huggingface](https://huggingface.co/datasets/amphion/SD-Eval/tree/main/archive) and will be loaded automatically using Huggingface Datasets.

```python
from datasets import load_dataset

# Load test-emo subset
dataset = load_dataset("amphion/SD-Eval", 'test-emo', data_dir='audio_path')

# Load test-acc subset
dataset = load_dataset("amphion/SD-Eval", 'test-acc', data_dir='audio_path')

# Load test-age subset
dataset = load_dataset("amphion/SD-Eval", 'test-age', data_dir='audio_path')

# Load test-env subset; we provide the audio data on Huggingface, so loading test-env does not need to set data_dir
dataset = load_dataset("amphion/SD-Eval", 'test-env')
```

You can also use your own code to load SD-Eval. In this way, please change the ```wav_path``` in JSON files accordingly.

## LLM Evaluation
Here is an example of using GPT-4o for evaluating the test-emo subset. Please change the path for model output and API key accordingly.

```bash
python3 llm_eval.py \
    --output_path results/test-emo \
    --test_set test-emo \
    --model gpt-4o \
    --pred_path path_to_model_output \
    --api_key ChatGPT_api_key \
```

## Citation
```
@article{ao2024sdeval,
  title   = {SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words},
  author  = {Junyi Ao and Yuancheng Wang and Xiaohai Tian and Dekun Chen and Jun Zhang and Lu Lu and Yuxuan Wang and Haizhou Li and Zhizheng Wu},
  eprint={2406.13340},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  year={2024}
}
```

## License
The dataset is licensed under the CC BY-NC 4.0 [license](LICENSE_dataset).
Code is licensed under the Apache 2.0 [license](LICENSE).

## Disclaimer
Your access to and use of this dataset are at your own risk. We do not guarantee the accuracy of this dataset. The dataset is provided “as is” and we make no warranty or representation to you with respect to it and we expressly disclaim, and hereby expressly waive, all warranties, express, implied, statutory or otherwise. This includes, without limitation, warranties of quality, performance, merchantability or fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. In no event will we be liable to you on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this public license or use of the licensed material. The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.
