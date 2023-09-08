"""
Pass pre-processed text to Pre-trained Roberta Model
pre requisite: transformers for loading bert qna model
"""
from transformers import pipeline

model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

"""
class contains method: extract_attribute
"""
class RobertaAttr:

    def ExtractAttribute(self,df):

        """
        method checks whether the text has unit and digit present in it and passes relevant text to roberta QnA
        roberta takes text as context and provides answer relevant to the question asked.

        parameters :   default parameter(self)
                   :   dataframe output from pre_processing as df
        returns    : dataframe having new column : roberta_attr_Val - with answer provided by roberta

        """
        for index, row in (df[(df['has_unit'] == True) & (df['has_digit'] == True)]).iterrows():

            qa_input = {
                # what is item volume in fluid ounces or fl oz
                'question': 'What is item volume under net contents',
                'context': df['PaddleOcr_output'][index]}

            res = nlp(qa_input)
            # assign the answer to df column
            df.loc[index, 'roberta_attr_val'] = res['answer']
        # fill remaining values as None
        df['roberta_attr_val'].fillna('None', inplace=True)
        return df
