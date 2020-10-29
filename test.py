from torchsummary import summary
import torch
from src import args as arg
from src import utils
from src.models.model import IRNet
from src.rule import semQL

if __name__ == '__main__':
    arg_parser = arg.init_arg_parser()
    args = arg.init_config(arg_parser)
    grammar = semQL.Grammar()
    print('123')
    print(grammar.prod2id)
    print(grammar.type2id)
    # sql_data, table_data, val_sql_data,\
    # val_table_data= utils.load_dataset(args.dataset, use_small=args.toy)
    # model = IRNet(args, grammar)
    # summary(model)