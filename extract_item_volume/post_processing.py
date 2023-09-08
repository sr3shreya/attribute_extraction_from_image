"""
Apply Post_processing rules over the extracted value from Roberta
"""
import re
from extract_item_volume.variables import *
"""
class post_process contains methods to clean the output extracted from QnA model
"""

class PostProcess:


    def ReplaceNonDigit(self,df):
        """
        method to replace output as None if there is no digit present in the text
        parameters  :default(self), output dataframe from roberta having attribute values present against each image
        returns     : NA

        """
        for attr in df['roberta_attr_val']:
            # check if digit is not present
            if any(str.isdigit(cha_r) for cha_r in attr) == False:
                df['roberta_attr_val'] = df['roberta_attr_val'].replace(attr, 'None')


    def RemoveExtraSpace(self,df):
        """
        method to remove extra spaces present within the words
        parameters  :  default(self), dataframe
        returns     :  NA

        """
        df.roberta_attr_val = df.roberta_attr_val.str.replace('  ', ' ')


    def IsFloat(self,str):
        '''
        python treats decimal value as string , hence split the data over "." and check if there are digits present
        edge_case  : digits are identified as letters - for eg. 1 as l or z as 2
        parameters : str - word from the text
        returns    : if digit is present returns True else False
        '''
        s1 = str.lstrip(' ')
        s2 = s1.split('.')
        return all(n.isdigit() for n in s2) and len(s2) <= 2


    def RenameUnits(self,df):
        """
        method takes up roberta_attribute_value, identifies the presence of any unit from the above list of unitsy.
        if the unit is identified, it replaces the occurrences with standardized naming convention eg: floz for all occurrence of item_volume present in fluid ounce

        parameters : default(self), dataframe
        return: NA
        """
        for index, row in df[df['roberta_attr_val'] != 'None'].iterrows():

            li_attr_word = []
            for word in row['roberta_attr_val'].split():
                if word.isdigit() or self.IsFloat(word):
                    li_attr_word.append(word)
                elif word in fl_oz:
                    li_attr_word.append('floz')
                elif word in ml:
                    li_attr_word.append('ml')
                elif word in litre:
                    li_attr_word.append('litre')
                elif word in quart:
                    li_attr_word.append('quart')
                elif word in pint:
                    li_attr_word.append('pint')
                elif word in gallon:
                    li_attr_word.append('gallon')
                else:
                    continue
                df['roberta_attr_val'][index] = ' '.join(li_attr_word)


    def DropOnlyNumerics(self,df):
        """
        method identifies wherever the normalised units are not present and roberta has provided only integer as o/p,
        replace the attribute_Value with None
        parameters : dataframe
        returns    : NA
        """

        numerical_value = []

        for index, row in df[df['roberta_attr_val'] != 'None'].iterrows():
            '''
            iterate through rows , split the attribute value check for the normalised unit, if it is  not present then replace the value by none.
            '''
            attr_split=[]
            attr_split = row['roberta_attr_val'].split()
            if any(substr in final_units for substr in attr_split):
                continue
            else:
                numerical_value.append([index, df['roberta_attr_val'][index], df['PaddleOcr_output'][index]])
                df.loc[index, 'roberta_attr_val'] = 'None'


    def SegregateUnits(self,df):
        """
        method to segregate attribute_value using a seperator "," if more than 2 are present
        parameters:  df
        returns : dataframe containing cleaned and segregated attribute value along with unit
        """
        df['item_volume'] = ''
        regex = r"(\d*[.]?\d+) ([a-zA-Z]+)"
        for index, row in df[df['roberta_attr_val'] != 'None'].iterrows():

            match = re.findall(regex, row['roberta_attr_val'])
            temp_li = []
            if len(match)>0:
                for word in range(0, len(match)):
                    temp_li.append(' '.join(match[word]))
                    attr_val = ','.join(temp_li)

                df.loc[index, 'item_volume'] = attr_val
            else:
                df.loc[index, 'item_volume']='None'
        df.loc[:, 'item_volume'] = df['item_volume'].replace('', 'None')
        return df

    #def UpperLimit(self, df):
        #for

    def MasterPostProcess(self,df):
        """
        method is used to call all the post-processing methods required to clean the attribute_value
        parameters:  df - output dataframe from roberta
        returns:     final dataframe having item_volume against each image
        """
        self.ReplaceNonDigit(df)
        self.RemoveExtraSpace(df)
        #df['roberta_attr_val'] = df['roberta_attr_val'].apply(self.remove_extra_decimal_of_unit)
        self.RenameUnits(df)
        self.DropOnlyNumerics(df)
        df_item_volume=self.SegregateUnits(df)
        return df_item_volume




