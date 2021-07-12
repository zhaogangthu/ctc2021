#!/bin/bash


MODEL_PATH=/home/qa/zg/ctc2021/ctc2021_baseline/pytorch_bert_zh_model/
VOCAB_PATH=/home/qa/zg/ctc2021/ctc_gector/data/output_vocabulary/
#BASE_PATH=ctc2021_baseline/best.th
INPUT_FILE=/home/qa/zg/ctc2021/ctc2021_qua/qua_input_token.txt
OUTPUT_FILE=${INPUT_FILE}.output

#python segment.py < $INPUT_FILE > ${INPUT_FILE}.tok
src='/home/qa/zg/ctc2021/ctc2021_qua/qua_input.txt'
target='submit.txt'


CUDA_VISIBLE_DEVICES=1 python predict.py \
    --transformer_model $MODEL_PATH \
    --special_tokens_fix 0 \
    --iteration_count 3 \
    --model_path $MODEL_PATH/pytorch_model.bin \
    --vocab_path $VOCAB_PATH \
    --input_file $INPUT_FILE \
    --output_file $OUTPUT_FILE \
    --additional_confidence 0. \
    --min_error_probability 0.

#python convert_from_sentpair_to_edits.py ${INPUT_FILE}.tok $OUTPUT_FILE $INPUT_FILE > ${INPUT_FILE}.result
#out='D:\software\CTC2021-main\ctc_gector/qua_input_token_out2.txt'

python submit.py $src $OUTPUT_FILE $target
