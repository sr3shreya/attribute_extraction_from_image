1) OCR_text_extract.py:
   extracts text from image using paddle OCR.
2) Pre-processing.py:
   Apply Pre-Processing rules and perform text cleaning over extracted text.
   Eg. Dropping the texts where no numerical value is present
   COnverting ot lowercase
4) roberta_qna.py
   Pass pre-processed text to Pre-trained Roberta Model in order to extract attribute
5) post_processing.py
   Perform text cleaining in the output provided by roberta.
   Example: dropping outputs if the extracted attribute doesn't have numerical output
   Normalizing Units like m1 to mL, f1 ounce to fluid ounce
6) variables.py
   includes all the variables
