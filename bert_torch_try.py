import torch
from transformers import *

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

model.cuda()

input_ids = torch.tensor([tokenizer.encode('Try to encode something',add_special_tokens=True)]).cuda()
print(input_ids)
with torch.no_grad():
    last_hidden_states = model(input_ids)[0]
    print(last_hidden_states)