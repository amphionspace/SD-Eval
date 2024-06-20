from openai import OpenAI
from argparse import ArgumentParser
from tqdm import tqdm

import re
import json

from prompts import prompts

def find_number_in_brackets(text):
    # Regular expression pattern to find numbers within multiple square brackets
    patterns = [r"\[+\[+(-?\d+)\]+\]+", r"\[+(-?\d+)\]+", r"\[+\[+(-?[+-]?([0-9]*[.])?[0-9]+)\]+\]+", r"\[+(-?[+-]?([0-9]*[.])?[0-9]+)\]+"]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return float(match.group(1))  # Convert the matched number to an integer

    if text.split('Rating: ')[-1][0].isdigit():
        return float(text.split('Rating: ')[-1][0])

    return None  # No number found

parser = ArgumentParser()
parser.add_argument("-p", "--pred_path", type=str, help="Path to predicted results, which is a JSON dictionary with key, which is the utterance ID corresponding to the IDs in the subset JSON file, and value, which is the model output")
parser.add_argument("-o", "--output_path", type=str, help="Path to store the output for rating")
parser.add_argument("-a", "--api_key", type=str, help="api key for ChatGPT")
parser.add_argument("-t", "--test_set", type=str, default='test-emo', choices=['test-emo', 'test-acc', 'test-age', 'test-env'], help="Evaluate on which test subset")
parser.add_argument("-m", "--model", type=str, default='gpt-4o', help="Which GPT model to be used")
args = parser.parse_args()

# Read prediction and reference files
with open(f"data/{args.test_set}.json") as f:
    ref_json = json.load(f)

with open(args.pred_path) as f:
    pred_json = json.load(f)

assert len(pred_json) == len(ref_json), "Number of predictions and references do not match"

scores = []
client = OpenAI(api_key=args.api_key)
out_f = open(args.output_path, 'a')
for ref_utt_info in tqdm(ref_json):
    utt_id = ref_utt_info['utt_id']
    user_input = prompts[args.test_set]['user_input'].format(
        statement=ref_utt_info['transcript'],
        info=ref_utt_info['info'].title(),
        response=pred_json[utt_id]
    )

    model_input = [
        {"role": "system", "content": prompts[args.test_set]['sys']}, {"role": "user", "content": user_input}
    ]

    result = client.chat.completions.create(
        model=args.model,
        messages=model_input,
        seed=1337,
        temperature=0
    )

    response = result.choices[0].message.content
    score = find_number_in_brackets(response)

    results = {'utt_id': utt_id}
    results['score'] = score
    results['rate_details'] = response

    json.dump(results, out_f)
    out_f.write('\n')
    out_f.flush()
    scores.append(score)

out_f.close()
print('Average score:', sum(scores)/len(scores))
