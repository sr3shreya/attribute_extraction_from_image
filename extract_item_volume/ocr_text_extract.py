"""
Paddle_OCR to extract text from the images.
Pre-requisite:
                images_folder is placed on desktop
                image_folder name is hardcoded : 'run_test'
"""

import os
from paddleocr import PaddleOCR
from extract_item_volume.variables import *



class PaddleText:
    """
    class_name: Paddle_Text
    contains method: text_extract
    """
    def TextExtract(self,df):

        """
        - loads opensource OCR model named Paddle.
        - Reads images from the path (local system)
        - extracts text against each image and stores in df against image_name

        parameter:  blank input_df to add data as df
        returns:    df containing asin name and the text extracted
        """
        ocr_model = PaddleOCR(lang='en', use_angle_cls=True)
        # to pass only the images (file format: .jpg, .jpeg, .png)
        file_format = ['.jpg', '.jpeg', '.png']

        '''
        iterate over images all the images and pass it to ocr
        '''
        for image in os.listdir(path):
            if any(item in image for item in file_format):
                image_path = os.path.join(path, image)
                text_results = ocr_model.ocr(image_path, )[0]
                temp_text = ''
                for box, text in text_results:
                    temp_text += text[0] + ' '
                '''
                append data to dictionary with format image_filename and paddle_output
                convert dictionary to dataframe named df
                '''
                dictionary = {'img_filename': image, 'PaddleOcr_output': temp_text}
                df = df.append(dictionary, ignore_index=True)
        return df
