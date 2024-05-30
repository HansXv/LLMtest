import json
import uuid
import re

def parse_qa(entry):

    pattern = r"Question: (.+?)\\nAnswer: (.+?)\\n"
    matches = re.findall(pattern, entry['input'])
    qa_pairs = []

    for match in matches:
        question, answer = match

        question = question.strip().replace("\\n", " ")
        answer = answer.strip().replace("\\n", " ")
        qa_pairs.append((question, answer))

    return qa_pairs

def process_data(input_json_file, output_json_file):
    with open(input_json_file, 'r') as file:
        data = json.load(file)

    output_data = []

    for entry in data:
        qa_pairs = parse_qa(entry)
        for question, answer in qa_pairs:
            output_data.append({
                "id": str(uuid.uuid4()),  # 生成一个唯一标识符
                "Question": question,
                "Answer": answer
            })

    with open(output_json_file, 'w') as file:
        json.dump(output_data, file, indent=4)


# 示例用法
process_data('test.json', 'output.json')
