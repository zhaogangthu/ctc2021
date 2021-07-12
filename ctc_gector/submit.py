# -*- coding: utf-8 -*-
# @File : submit.py 
# @Time    : 2021/7/9 17:24
# @Author  : zhaogang
from tqdm import tqdm
import Levenshtein
import sys
try:
    src = sys.argv[1]
except:
    src=''
try:
    out = sys.argv[2]
except:
    out=''
try:
    target = sys.argv[3]
except:
    target=''

def gen_submit_data(src,out,target):
    with open(target,'w',encoding='utf8') as f:
        print('创建文件',target)
    src_lines=[]
    tgt_lines=[]
    id_list=[]
    with open(src,encoding='utf8') as f:
        for line in f:
            line=line.strip()
            line=line.split('\t')
            id_list.append(line[0])
            src_lines.append(line[1])
    with open(out,encoding='utf8') as f:
        for line in f:
            line=line.strip()
            line=line.replace(' ','')
            tgt_lines.append(line)

    for sid,src_line,tgt_line in tqdm(zip(id_list,src_lines,tgt_lines)):
        edits = Levenshtein.opcodes(src_line, tgt_line)
        result = []
        for edit in edits:
            if "。" in tgt_line[edit[3]:edit[4]]: # rm 。
                continue
            if edit[0] == "insert":
                result.append((str(edit[1]), "缺失", "", tgt_line[edit[3]:edit[4]]))
            elif edit[0] == "replace":
                result.append((str(edit[1]), "别字", src_line[edit[1]:edit[2]], tgt_line[edit[3]:edit[4]]))
            elif edit[0] == "delete":
                result.append((str(edit[1]), "冗余", src_line[edit[1]:edit[2]], ""))

        out_line = ""
        for res in result:
            out_line +=  ', '.join(res) + ', '
        with open(target,'a',encoding='utf8') as f2:
            if out_line:
                f2.write(sid + ', ' + out_line.strip()+'\n')
            else:
                f2.write(sid + ', -1'+'\n')
if __name__=='__main__':
    #src='D:\software\CTC2021-main\ctc2021_qua/qua_input.txt'
    #out='D:\software\CTC2021-main\ctc_gector/qua_input_token_out3.txt'
    #target='D:\software\CTC2021-main/train_small/submit5.txt'
    gen_submit_data(src,out,target)