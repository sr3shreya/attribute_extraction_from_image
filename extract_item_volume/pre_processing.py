"""
Apply Pre-Processing rules over extracted text
"""
import re
from extract_item_volume.variables import *

class PreProcess:
    """
    class_name: Pre_Process
    contain methods to perform text cleaning.
    """

    def UpperCase(self,df):

        """
        converts all the text to uppercase
        parameters: takes paddle_ocr_output as df
        return: NA
        """

        df.loc[:,'PaddleOcr_output']=df['PaddleOcr_output'].str.upper()

    def RemoveSpecialChars(self,df):

        """
        removes special characters from the text
        parameter: default parameter and df as input.
        return: NA
        """

        for spl_char in del_chars:
            df.loc[:,'PaddleOcr_output']=df['PaddleOcr_output'].str.replace(spl_char,'',regex=True)

    def Space(self,ip_text):

        """
        function removes extra space in between digit and
        parameters : default parameter self,
                   : x: row wise text and removes extra space
        returns    : clean text
        """

        if type(ip_text)==str:
            split_str = [space for space in re.split(r'([-+]?\d*\.\d+|\d+)', ip_text) if space]
            # new regex = [-+]?\d*\.*\d+
            result_text = " ".join(split_str)
            return result_text
        else:
            return 'None'

    def remove_space(self,ip_text):
        if type(ip_text)==str:
            result_text = re.sub(' +', ' ', ip_text)
            return result_text
        else:
            return 'None'

    def HasNumbers(self,inputstring):

        """
        method checks whether a digit (numeric) is present in the text or not
        parameters:   self(default)
                  :   inputString - row-wise text from df
        returns   :   True if the digit is present
                  :   and False if the digit is not present
        """

        return any(char.isdigit() for char in inputstring)

    def WordCount(self,ip_str):

        """
        method counts the number of words : this method was
        parameters :  self(default)
                   :  x - text against each asin
        returns    : word count in the string
        """

        return len(ip_str.split())

    def CheckUnit(self,df):
        """
        method checks whether the unit of measurement is present in the text or not.
        li_unit : captures all the possible combination of UoM extracted from OCR Model
        6 units associated with item_volume : litre, pint, quart, milli-litre, fluid ounce, gallon

        parameters :   default parameter(self)
                   :   dataframe

        returns    :
        """
        df['has_unit']=''
        #li_unit=['FL','F1','FI','FLOZ','FL.OZ.','FL. OZ.','FL.OZ','F.OZ','FL.O','FL.Z','F1OZ','FI0Z','FIOZ','F10Z','F.O','F1.OZ','F1.0Z.','F1.0Z','FOZ','FL O','FL 0','FL.Z','FL.OZ.','FLUID','ML','MILLILITRES','MLS','MILLILITRE','MILLI','LITRES','LITRE','LT.','LT','LTS','LTRS','PINT','PT','PINTS','QUARTS','QUART','QT','GALLON','GALLONS','GAL','L']

        for index in range(0,len(df)):

            '''
            check whether the text has datatype as 'str' and any of the word has units present from the list defined 
            assign value as 'True' to column_name : 'has_unit'
            assign value as 'False' to column_name : 'has_unit'
            '''

            if type(df['PaddleOcr_output'][index])==str and any(word in ((df['PaddleOcr_output'][index]).split()) for word in li_unit):
                df.loc[index,'has_unit']=True
            else:
                df.loc[index,'has_unit']=False

    def MasterPreprocess(self,df):
        """

        method calls all the methods present in the class for text pre-processing
        parameters :  default(self)
                   :  takes paddle_output_df as input and calls other functions to perform text_preprocessing
        returns    : df having cleaned text and couple of new columns

        """

        self.UpperCase(df)
        self.RemoveSpecialChars(df)
        df.loc[:, 'PaddleOcr_output'] = df['PaddleOcr_output'].apply(self.Space)
        df.loc[:, 'PaddleOcr_output'] = df['PaddleOcr_output'].apply(self.remove_space)
        df.loc[:, 'has_digit'] = df['PaddleOcr_output'].apply(self.HasNumbers)
        df.loc[:, 'word_count'] = df['PaddleOcr_output'].apply(self.WordCount)
        self.CheckUnit(df)
        return df

