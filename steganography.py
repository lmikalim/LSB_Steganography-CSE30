# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes
class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def convertToBinary(text):
        if type(text) == str:
            return ''.join([format(ord(char), '08b') for char in text])
        elif type(text) == int:
            return(text,'08b')

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)
        # convert into binary
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == 'huffman':
            self.codec = HuffmanCodes(delimiter = self.delimiter)
        binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            index = 0
            binaryMessage = self.convertToBinary(message)
            length = len(self.convertToBinary(message))
            returnImage = image.copy()
            # your code goes here
            # you may create an additional method that modifies the image array
            for values in returnImage:
                for pixel in values: ##iterating through the [r.g.b] values that make up the image
                    r,g,b= self.convertToBinary(pixel)
                    ##rgb values to binary
                    if index < length:  ##if at the end of sequence/least valuable bit
                        ## set hide data by adding binary Message at index in the last value of RED
                        pixel[0] = int(r[:-1] + binaryMessage[index],2)
                        index +=1 
                    if index < length:  ##if at the end of sequence/least valuable bit
                        ## set hide data by adding binary Message at index in the last value of GREEN
                        pixel[1] = int(r[:-1] + binaryMessage[index],2)
                        index +=1 
                    if index < length:  ##if at the end of sequence/least valuable bit
                        ## set hide data by adding binary Message at index in the last value of BLUE
                        pixel[2] = int(r[:-1] + binaryMessage[index],2)
                        index +=1 
                    if index >= length:
                        break

            

            cv2.imwrite(fileout,returnImage)
            
    

#     def decode(self, filein, codec):
#         image = cv2.imread(filein)
#         print(image) # for debugging      
        
#         # convert into text
#         if codec == 'binary':
#             self.codec = Codec(delimiter = self.delimiter) 
#         elif codec == 'caesar':
#             self.codec = CaesarCypher(delimiter = self.delimiter)
#         elif codec == 'huffman':
#             if self.codec == None or self.codec.name != 'huffman':
#                 print("A Huffman tree is not set!")
#                 flag = False
#         if flag:
#             # your code goes here
#             # you may create an additional method that extract bits from the image 
# array
#             binary_data = ?
#             # update the data attributes:
#             self.text = self.codec.decode(binary_data)
#             self.binary = ?              
        
#     def print(self):  #prints encoded and decoded messages in text and binary forms
#         if self.text == '':
#             print("The message is not set.")
#         else:
#             print("Text message:", self.text)
#             print("Binary message:", self.binary)          
#     def show(self, filename):
#         plt.imshow(mpimg.imread(filename))
#         plt.show()