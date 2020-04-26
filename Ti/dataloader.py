import csv
from torch.utils.data import TensorDataset

class InputFeature(object):
    def __init__(self,ans,input_ids):
        self.ans=ans
        self.input_ids=input_ids

def convert_data_to_feature(path):
    with open(path) as fl:
        reader = csv.DictReader(fl)
        for line in reader:
            