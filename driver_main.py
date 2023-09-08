"""
@shrsriv
Code designed to extract attribute value : item_volume from images.

1) OCR_text_extract.py - contains class for extracting text using Paddle OCR
                       - class_name : Paddle_Text
2) Pre_Processing.py   - contains class to perform pre-process on the text extracted from OCR model
                       - class_name : Pre_Process
3) Roberta_qna.py      - contains class for extracting attribute value from the text using Roberta QnA model
                       - class_name : Roberta_Attr
4) Post_Processing.py  - contains class to perform post-process on the output from QnA model to get attribute_value
                       - class_name : Post_Process
"""
import os
import pandas as pd
from extract_item_volume.ocr_text_extract import PaddleText
from extract_item_volume.pre_processing import PreProcess
from extract_item_volume.roberta_qna import RobertaAttr
from extract_item_volume.post_processing import PostProcess
from extract_item_volume.variables import *
"""
input_df: stores data w.r.t images 
NOTE: final output-sheet will be stored in the current working directory 
    : output file name is hardcoded: item_volume.xlsx
"""

input_df = pd.DataFrame(columns=['img_filename'])


"""
Class_name    : main (main driver class)
Function_name : __init__     
"""
class Main:
    def __init__(self):
        """
        Parameter     : default parameter - self
        Description   : init method or constructor
                      : contains object for each imported class

        1) ocr_obj:     object for class Paddle_Text
        2) pre_obj:     object for class Pre_Process
        3) roberta_obj: object for class Roberta_Attr
        4) post_obj:    object for class Post_Process
        """

        self.ocr_obj = PaddleText()
        self.pre_obj = PreProcess()
        self.roberta_obj = RobertaAttr()
        self.post_obj = PostProcess()


    def method_calls(self):
        """
        method call: text_extract from Paddle_Text()
        parameter  : input_df
        returns    : op_paddle

        method call : master_preprocess from Pre_Process()
        parameter  : op_paddle
        returns    : op_preprocess

        method call extract_attribute from Roberta_Attr()
        parameter  : op_preprocess
        returns    : op_roberta

        method call post_process from Post_Process()
        parameter  : op_roberta
        returns    : op_postprocess
        """

        op_paddle = self.ocr_obj.TextExtract(input_df)
        #op_paddle = pd.read_excel(os.getcwd() + '\\paddle_output.xlsx',engine='openpyxl')
        op_preprocess=self.pre_obj.MasterPreprocess(op_paddle)

        op_roberta=self.roberta_obj.ExtractAttribute(op_preprocess)
        #op_roberta = pd.read_excel(os.getcwd() + '\\item_volume_new_space_removal_only pre-process_no_postprocess.xlsx',
                                  #engine='openpyxl')

        op_postprocess=self.post_obj.MasterPostProcess(op_roberta)


        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(output_path+'\\'+op_filename, engine='xlsxwriter')
        # Write the dataframe data to XlsxWriter.
        op_postprocess.to_excel(writer, sheet_name='item_volume', index=False)
        writer.save()


master_class=Main()
master_class.method_calls()