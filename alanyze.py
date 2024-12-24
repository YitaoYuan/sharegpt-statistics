import json
import sys
from tqdm import tqdm

files = ['sg_90k_part1.json', 'sg_90k_part2.json']
files = [f'processed_{file_name}' for file_name in files]

conversation_round_cnt = []
conversation_len = []
round_prompt_len = []
round_new_prompt_len = []
round_response_len = []

for file_name in files:
    print(f"Processing file {file_name}", file=sys.stderr)
    file = open(file_name, 'r', encoding='utf-8')
    data = json.load(file)
    for conversation in tqdm(data):
        conversation_rounds = conversation["conversations"]
        conversation_round_cnt.append(len(conversation_rounds))
        # conversation_len.append()
        prompt_len = 0
        for round_text in conversation_rounds:
            sender = round_text["from"]
            len_tokens = round_text["value"]
            
            if sender in ["user", "human"]:
                new_prompt_len = len_tokens
                round_new_prompt_len.append(new_prompt_len)
                round_prompt_len.append(prompt_len + new_prompt_len)
            else:
                round_response_len.append(len_tokens)
            
            prompt_len += len_tokens
            
        conversation_len.append(prompt_len)

print("conversation_round_cnt")
print(conversation_round_cnt)
print("conversation_len")
print(conversation_len)
print("round_prompt_len")
print(round_prompt_len)
print("round_new_prompt_len")
print(round_new_prompt_len)
print("round_response_len")
print(round_response_len)