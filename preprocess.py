import json
from tqdm import tqdm
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('/models/preset/meta-llama/Meta-Llama-3.1-70B-Instruct')

# data = []
files = ['sg_90k_part1.json', 'sg_90k_part2.json']
# 打开JSON文件
for file_name in files:
    print(f"Processing file {file_name}")
    file = open(file_name, 'r', encoding='utf-8')
    # 加载JSON数据
    data = json.load(file)

    for conversation in tqdm(data):
        conversation_rounds = conversation["conversations"]
        for round_text in conversation_rounds:
            text = round_text["value"]
            tokens = tokenizer.tokenize(text)
            round_text["value"] = len(tokens)
            
    json_str = json.dumps(data, indent=4)
    output_file = open(f'processed_{file_name}', 'w', encoding='utf-8')
    output_file.write(json_str)