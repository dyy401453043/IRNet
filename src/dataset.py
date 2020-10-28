# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# -*- coding: utf-8 -*-
"""
# @Time    : 2019/5/25
# @Author  : Jiaqi&Zecheng
# @File    : utils.py
# @Software: PyCharm
"""

import copy

import src.rule.semQL as define_rule
from src.models import nn_utils


class Example:
    """

    """
    def __init__(self, src_sent, tgt_actions=None, vis_seq=None, tab_cols=None, col_num=None, sql=None,
                 one_hot_type=None, col_hot_type=None, schema_len=None, tab_ids=None,
                 table_names=None, table_len=None, col_table_dict=None, cols=None,
                 table_col_name=None, table_col_len=None,
                  col_pred=None, tokenized_src_sent=None,
        ):

        self.src_sent = src_sent
        self.tokenized_src_sent = tokenized_src_sent
        self.vis_seq = vis_seq
        self.tab_cols = tab_cols
        self.col_num = col_num
        self.sql = sql
        self.one_hot_type=one_hot_type
        self.col_hot_type = col_hot_type
        self.schema_len = schema_len
        self.tab_ids = tab_ids
        self.table_names = table_names
        self.table_len = table_len
        self.col_table_dict = col_table_dict
        self.cols = cols
        self.table_col_name = table_col_name
        self.table_col_len = table_col_len
        self.col_pred = col_pred
        self.tgt_actions = tgt_actions
        self.truth_actions = copy.deepcopy(tgt_actions)

        self.sketch = list()
        if self.truth_actions:
            for ta in self.truth_actions:
                if isinstance(ta, define_rule.C) or isinstance(ta, define_rule.T) or isinstance(ta, define_rule.A):
                    continue
                self.sketch.append(ta)

    def __str__(self):
        str = ''
        str += "src_sent:{}\n".format(self.src_sent)
        str += "vis_seq:{}\n".format(self.vis_seq)
        str += "tab_cols:{}\n".format(self.tab_cols)
        str += "col_num:{}\n".format(self.col_num)
        str += "sql:{}\n".format(self.sql)
        str += "one_hot_type:{}\n".format(self.one_hot_type)
        str += "col_hot_type:{}\n".format(self.col_hot_type)
        str += "schema_len:{}\n".format(self.schema_len)
        str += "tab_ids:{}\n".format(self.tab_ids)
        str += "tab_names:{}\n".format(self.table_names)
        str += "tab_len:{}\n".format(self.table_len)
        str += "table_col_name:{}\n".format(self.table_col_name)
        str += "table_col_len:{}\n".format(self.table_col_len)
        str += "col_pred:{}\n".format(self.col_pred)
        str += "tgt_actions:{}\n".format(self.tgt_actions)
        return str
# src_sent:[['what'], ['are'], ['name'], ['of'], ['table', 'product'], ['that'], ['are'], ['not'], ["'"], ['white'], ["'"], ['in'], ['color'], ['and'], ['are'], ['not'], ['measured'], ['by'], ['unit'], ["'"], ['handful'], ["'"], ['?']]
# vis_seq:("What are the names of products that are not 'white' in color and are not measured by the unit 'Handful'?", [['count', 'number', 'many'], ['characteristic', 'type', 'code'], ['characteristic', 'type', 'description'], ['color', 'code'], ['color', 'description'], ['product', 'category', 'code'], ['product', 'category', 'description'], ['unit', 'of', 'measure'], ['characteristic', 'id'], ['characteristic', 'data', 'type'], ['characteristic', 'name'], ['other', 'characteristic', 'detail'], ['product', 'id'], ['product', 'name'], ['typical', 'buying', 'price'], ['typical', 'selling', 'price'], ['product', 'description'], ['other', 'product', 'detail'], ['product', 'characteristic', 'value']], 'SELECT t1.product_name FROM products AS t1 JOIN ref_product_categories AS t2 ON t1.product_category_code  =  t2.product_category_code JOIN ref_colors AS t3 ON t1.color_code  =  t3.color_code WHERE t3.color_description  =  "white" AND t2.unit_of_measure != "Handful"')
# tab_cols:[['count', 'number', 'many'], ['characteristic', 'type', 'code'], ['characteristic', 'type', 'description'], ['color', 'code'], ['color', 'description'], ['product', 'category', 'code'], ['product', 'category', 'description'], ['unit', 'of', 'measure'], ['characteristic', 'id'], ['characteristic', 'data', 'type'], ['characteristic', 'name'], ['other', 'characteristic', 'detail'], ['product', 'id'], ['product', 'name'], ['typical', 'buying', 'price'], ['typical', 'selling', 'price'], ['product', 'description'], ['other', 'product', 'detail'], ['product', 'characteristic', 'value']]
# col_num:19
# tab_names:[['reference', 'characteristic', 'type'], ['reference', 'color'], ['reference', 'product', 'category'], ['characteristic'], ['product'], ['product', 'characteristic']]
# tab_len:6
# table_col_name:[['characteristic', 'type', 'code', 'characteristic', 'type', 'description'], ['color', 'code', 'color', 'description'], ['product', 'category', 'code', 'product', 'category', 'description', 'unit', 'of', 'measure'], ['characteristic', 'id', 'characteristic', 'type', 'code', 'characteristic', 'data', 'type', 'characteristic', 'name', 'other', 'characteristic', 'detail'], ['product', 'id', 'color', 'code', 'product', 'category', 'code', 'product', 'name', 'typical', 'buying', 'price', 'typical', 'selling', 'price', 'product', 'description', 'other', 'product', 'detail'], ['product', 'id', 'characteristic', 'id', 'product', 'characteristic', 'value']]
# table_col_len:6
# col_pred:None
# tgt_actions:[Root1(3), Root(3), Sel(0), N(0), A(none), C(13), T(4), Filter(Filter and Filter Filter), Filter(Filter = A), A(none), C(4), T(1), Filter(Filter != A), A(none), C(7), T(2)]



class cached_property(object):
    """ A property that is only computed once per instance and then replaces
        itself with an ordinary attribute. Deleting the attribute resets the
        property.

        Source: https://github.com/bottlepy/bottle/commit/fa7733e075da0d790d809aa3d2f53071897e6f76
        """

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


class Batch(object):
    def __init__(self, examples, grammar, cuda=False):
        self.examples = examples

        if examples[0].tgt_actions:
            self.max_action_num = max(len(e.tgt_actions) for e in self.examples)
            self.max_sketch_num = max(len(e.sketch) for e in self.examples)

        self.src_sents = [e.src_sent for e in self.examples]
        self.src_sents_len = [len(e.src_sent) for e in self.examples]
        self.tokenized_src_sents = [e.tokenized_src_sent for e in self.examples]
        self.tokenized_src_sents_len = [len(e.tokenized_src_sent) for e in examples]
        self.src_sents_word = [e.src_sent for e in self.examples]
        self.table_sents_word = [[" ".join(x) for x in e.tab_cols] for e in self.examples]

        self.schema_sents_word = [[" ".join(x) for x in e.table_names] for e in self.examples]

        self.src_type = [e.one_hot_type for e in self.examples]
        self.col_hot_type = [e.col_hot_type for e in self.examples]
        self.table_sents = [e.tab_cols for e in self.examples]
        self.col_num = [e.col_num for e in self.examples]
        self.tab_ids = [e.tab_ids for e in self.examples]
        self.table_names = [e.table_names for e in self.examples]
        self.table_len = [e.table_len for e in examples]
        self.col_table_dict = [e.col_table_dict for e in examples]
        self.table_col_name = [e.table_col_name for e in examples]
        self.table_col_len = [e.table_col_len for e in examples]
        self.col_pred = [e.col_pred for e in examples]

        self.grammar = grammar
        self.cuda = cuda

    def __len__(self):
        return len(self.examples)


    def table_dict_mask(self, table_dict):
        return nn_utils.table_dict_to_mask_tensor(self.table_len, table_dict, cuda=self.cuda)

    @cached_property
    def pred_col_mask(self):
        return nn_utils.pred_col_mask(self.col_pred, self.col_num)

    @cached_property
    def schema_token_mask(self):
        return nn_utils.length_array_to_mask_tensor(self.table_len, cuda=self.cuda)

    @cached_property
    def table_token_mask(self):
        return nn_utils.length_array_to_mask_tensor(self.col_num, cuda=self.cuda)

    @cached_property
    def table_appear_mask(self):
        return nn_utils.appear_to_mask_tensor(self.col_num, cuda=self.cuda)

    @cached_property
    def table_unk_mask(self):
        return nn_utils.length_array_to_mask_tensor(self.col_num, cuda=self.cuda, value=None)

    @cached_property
    def src_token_mask(self):
        return nn_utils.length_array_to_mask_tensor(self.src_sents_len,
                                                    cuda=self.cuda)


