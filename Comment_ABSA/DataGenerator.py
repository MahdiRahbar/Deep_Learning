# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:26:07 2020

@author: Mahdi Rahbar
"""

import pandas as pd
from callApi import *
import json
import ast 

#---------------------------------------------------------------
api_key = "cbb6763d-3535-ea11-80eb-98ded002619b"

baseUrl = "http://api.text-mining.ir/api/"
url = baseUrl + "Token/GetToken"
querystring = {"apikey":"{}".format(api_key)}
response = requests.request("GET", url, params=querystring)
_data = json.loads(response.text)
tokenKey = _data['token']
#---------------------------------------------------------------

class DataGenerator:

    def __init__(self, data_path, save_path):
        self.data_path = data_path
        self.save_path = save_path
        self.input_data = None
        self.ErrorListIndex = []
        self.output_data = []
        
        self.ErrorListIndex_formal = []
        self.output_data_2_formal = []

        self.data_length = 0
        self.counter_formal = 0
    
    def Data_Import(self):
        self.input_data = pd.read_csv(self.data_path)
        self.data_length = len(self.input_data)

    def Comment_Cleaner(self, str_data):

        """
        
        """
        i = self.counter 
        temp = []
                #####################      Text Normalizer       #########################
        try:
            baseUrl = "http://api.text-mining.ir/api/"
            url =  baseUrl + "PreProcessing/NormalizePersianWord"
            payload = u'{{\"text\":\"{}\", \"refineSeparatedAffix\":true}}'.format(str_data)


            temp=callApi(url, payload, tokenKey)
        except Exception as e: 
            print("The Error is : ", e)
            print("Error on iteration: {0} function: {1} ".format(i,"Text Normalizer"))
            self.ErrorListIndex.append(i)
                   
#         ################ Call Sentence Splitter ##################
        try:
            url =  baseUrl + "PreProcessing/SentenceSplitter"
            payload = u'''{\"text\":\"%s\",
                    \"checkSlang\": true,
                    \"normalize\": true,
                    \"normalizerParams\": {
                    \"text\": \"don't care\",
                    \"RefineQuotationPunc \": false
                    },
                    \"complexSentence\": true
                    }'''%format(temp)
            temp = callApi(url, payload, tokenKey)
            
        except Exception as e: 
            print("The Error is : ", e)
            print("Error on iteration: {0} function: {1} ".format(i,"Slang to Formal Converter"))
            self.ErrorListIndex.append(i)
            
        return temp

    def Comment_Cleaner_2_Formal(self, str_data):

        """
        
        """
        i = self.counter 
        temp = []
                #####################      Text Normalizer       #########################
        try:
            baseUrl = "http://api.text-mining.ir/api/"
            url =  baseUrl + "PreProcessing/NormalizePersianWord"
            payload = u'{{\"text\":\"{}\", \"refineSeparatedAffix\":true}}'.format(str_data)


            temp=callApi(url, payload, tokenKey)
        except Exception as e: 
            print("The Error is : ", e)
            print("Error on iteration: {0} function: {1} ".format(i,"Text Normalizer"))
            self.ErrorListIndex_formal.append(i)
                   
#         ################ Call Slang to Formal Converter ##################
        try:
            url =  baseUrl + "TextRefinement/FormalConverter"
            payload = u'\"{0}\"'.format(temp)
            temp = callApi(url, payload, tokenKey)
        except Exception as e: 
            print("The Error is : ", e)
            print("Error on iteration: {0} function: {1} ".format(i,"Slang to Formal Converter"))
            self.ErrorListIndex_formal.append(i)

            
#         ################ Call Sentence Splitter ##################
        try:
            url =  baseUrl + "PreProcessing/SentenceSplitter"
            payload = u'''{\"text\":\"%s\",
                    \"checkSlang\": true,
                    \"normalize\": true,
                    \"normalizerParams\": {
                    \"text\": \"don't care\",
                    \"RefineQuotationPunc \": false
                    },
                    \"complexSentence\": true
                    }'''%format(temp)
            temp = callApi(url, payload, tokenKey)
            
        except Exception as e: 
            print("The Error is : ", e)
            print("Error on iteration: {0} function: {1} ".format(i,"Slang to Formal Converter"))
            self.ErrorListIndex_formal.append(i)
            
        return temp

    def Adv_Disadv(self,input_data):
        """
        
        """
        i = self.counter 
        temp = []

        final_temp = []
        internal_list_temp = ast.literal_eval(input_data)
        for j in range(len(internal_list_temp)):
                #####################      Text Normalizer       #########################
            try:
                baseUrl = "http://api.text-mining.ir/api/"
                url =  baseUrl + "PreProcessing/NormalizePersianWord"
                payload = u'{{\"text\":\"{}\", \"refineSeparatedAffix\":true}}'.format(internal_list_temp[j])


                temp=callApi(url, payload, tokenKey)
            except Exception as e: 
                print("The Error is : ", e)
                print("Error on iteration: {0} function: {1} ".format(i,"Text Normalizer"))
                self.ErrorListIndex.append(i)
                continue


    #         ################ Sentence Tokenizer ##################
            try:
                url =  baseUrl + "PreProcessing/SentenceSplitter"
                payload = u'''{\"text\":\"%s\",
                        \"checkSlang\": true,
                        \"normalize\": true,
                        \"normalizerParams\": {
                        \"text\": \"don't care\",
                        \"RefineQuotationPunc \": false
                        },
                        \"complexSentence\": true
                        }'''%temp
                temp = callApi(url, payload, tokenKey)
                temp = ast.literal_eval(temp)

            except Exception as e: 
                print("The Error is : ", e)
                print("Error on iteration: {0} function: {1} ".format(i,"Sentence Tokenizer"))
                self.ErrorListIndex.append(i)

                continue
            for l in range(len(temp)):
                final_temp.append(temp[l])
        return final_temp
    
    def Adv_Disadv_2_Formal(self, input_data):
        """
        
        """
        i = self.counter 
        temp = []

        final_temp = []
        internal_list_temp = ast.literal_eval(input_data)
        for j in range(len(internal_list_temp)):
                #####################      Text Normalizer       #########################
            try:
                baseUrl = "http://api.text-mining.ir/api/"
                url =  baseUrl + "PreProcessing/NormalizePersianWord"
                payload = u'{{\"text\":\"{}\", \"refineSeparatedAffix\":true}}'.format(internal_list_temp[j])


                temp=callApi(url, payload, tokenKey)
            except Exception as e: 
                print("The Error is : ", e)
                print("Error on iteration: {0} function: {1} ".format(i,"Text Normalizer"))
                self.ErrorListIndex.append(i)
                continue

    #         ################ Call Slang to Formal Converter ##################
            try:
                url =  baseUrl + "TextRefinement/FormalConverter"
                payload = u'\"{0}\"'.format(temp)
                temp = callApi(url, payload, tokenKey)
            except Exception as e: 
                print("The Error is : ", e)
                print("Error on iteration: {0} function: {1} ".format(i,"Slang to Formal Converter"))
                self.ErrorListIndex.append(i)

                continue
    #         ################ Sentence Tokenizer ##################
            try:
                url =  baseUrl + "PreProcessing/SentenceSplitter"
                payload = u'''{\"text\":\"%s\",
                        \"checkSlang\": true,
                        \"normalize\": true,
                        \"normalizerParams\": {
                        \"text\": \"don't care\",
                        \"RefineQuotationPunc \": false
                        },
                        \"complexSentence\": true
                        }'''%temp
                temp = callApi(url, payload, tokenKey)
                temp = ast.literal_eval(temp)

            except Exception as e: 
                print("The Error is : ", e)
                print("Error on iteration: {0} function: {1} ".format(i,"Sentence Tokenizer"))
                self.ErrorListIndex.append(i)

                continue
            for l in range(len(temp)):
                final_temp.append(temp[l])
        return final_temp

    def PoS_Extractor(self, input_data):
        """
        
        """
        url =  baseUrl + "PosTagger/GetPos"
        temp_list = [] 
        new_list = list(input_data)
        for i in range(len(new_list)):
            sentence_POS = []
            payload = u'\"{0}\"'.format(new_list[i])                
            result = json.loads(callApi(url, payload, tokenKey))
            for phrase in result:
                sentence_POS.append("("+phrase['word']+","+phrase['tags']['POS']['item1']+")")
            temp_list.append(sentence_POS)
        return temp_list

    def Data_cleaner(self):
        for i in range(self.data_length):
            temp_data = pd.DataFrame(self.input_data)

            self.counter = i
            temp_data = []
            temp_data.append(self.input_data.iloc[i]["product_title"])
            temp_data.append(self.input_data.iloc[i]["recommend"])
            temp_data.append(self.input_data.iloc[i]["title"])
        #===========================================================================
            ### Comment Section 
            temp_data.append(self.input_data.iloc[i]["comment"])
            # Cleaning Comment
            Cleaned_Comment_Output = self.Comment_Cleaner(self.input_data.iloc[i]["comment"])
            temp_data.append(Cleaned_Comment_Output)
            temp_data.append(self.PoS_Extractor(Cleaned_Comment_Output))
        #===========================================================================
            ### Advantages Section 
            temp_data.append(self.input_data.iloc[i]["advantages"])
            # Cleaning Advantages
            Cleaned_Adv = self.Adv_Disadv(self.input_data.iloc[i]["advantages"])
            temp_data.append(Cleaned_Adv)
            temp_data.append(self.PoS_Extractor(Cleaned_Adv))
        #===========================================================================
            ### Disadvantages Section 
            temp_data.append(self.input_data.iloc[i]["disadvantages"])
            # Cleaning Disadvantages
            temp_DisAdv = self.Adv_Disadv(self.input_data.iloc[i]["disadvantages"])
            temp_data.append(temp_DisAdv)
            temp_data.append(self.PoS_Extractor(self.input_data.iloc[i]["disadvantages"]))
            
            self.output_data.append(temp_data)
        return self.output_data , self.ErrorListIndex




    def Data_cleaner_2_formal(self):
        temp_data = pd.DataFrame(self.input_data)


        for i in range(self.data_length):
            self.counter = i
            temp_data = []
            temp_data.append(self.input_data.iloc[i]["product_title"])
            temp_data.append(self.input_data.iloc[i]["recommend"])
            temp_data.append(self.input_data.iloc[i]["title"])
        #===========================================================================
            ### Comment Section 
            temp_data.append(self.input_data.iloc[i]["comment"])
            # Cleaning Comment
            Cleaned_Comment = self.Comment_Cleaner(self.input_data.iloc[i]["comment"])
            temp_data.append(Cleaned_Comment)
            temp_data.append(self.PoS_Extractor(Cleaned_Comment))
        #===========================================================================
            ### Advantages Section 
            temp_data.append(self.input_data.iloc[i]["advantages"])
            # Cleaning Advantages
            Cleaned_Adv = self.Adv_Disadv_2_Formal(self.input_data.iloc[i]["advantages"])
            temp_data.append(Cleaned_Adv)
            temp_data.append(self.PoS_Extractor(self.input_data.iloc[i]["advantages"]))
        #===========================================================================
            ### Disadvantages Section 
            temp_data.append(self.input_data.iloc[i]["disadvantages"])
            # Cleaning Disadvantages
            temp_DisAdv = self.Adv_Disadv_2_Formal(self.input_data.iloc[i]["disadvantages"])
            temp_data.append(temp_DisAdv)
            temp_data.append(self.PoS_Extractor(temp_DisAdv))
            
            self.output_data_2_formal.append(temp_data)

        return self.output_data_2_formal , self.ErrorListIndex_formal
