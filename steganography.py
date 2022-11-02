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


    def encode(self, filein, fileout, message, codec):
        ##each least significant bit of each rgb pixel
        image = cv2.imread(filein)
        print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec(self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(self.delimiter)
        elif codec == 'huffman':
            self.codec = HuffmanCodes(self.delimiter)
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
    
            print('Message is', message)
            print("binaryMessage is ",binary)
            length = len(binary)
            returnImage = image.copy()
            # your code goes here
            ##All even values end in 0
            ##so if num %2 == 0
            ## for encoding if even, then just add 1(adds 1 to the end)
            ##els if it's 1 and you want it to be 0, then you take away 1
            ## odd: if it's zero and you want it to be 0, do nothing
            for i,values in enumerate(image):
                for k,pixel in enumerate(values): ##iterating through the [r.g.b] values that make up the image
                    for j,color in enumerate(pixel):
                        if index >= length:
                                break
                        print('color:',color,'binary at index is',binary[index])
                        binaryColor = bin(color)
                        
                       
                        if color % 2 == 0:
                            
                            if int(binary[index]) == 1:
                                print('yes')
                                og = color
                                print("binary message at index is",binary[index], 'adding 1 to color' )
                               
                                image[i][k][j] = color +1
                                print("color has been changed to ",color, 'from ', og)
                            
                        else:
                            
                            if int(binary[index]) == 0:
                                print("yes")
                                og = color
                                print("binary message at index is",binary[index], 'subtracting to color' )
                                image[i][k][j] = color -1
                                print("color has been changed to ",color, 'from ', og)
                        index+=1
            print("image is now", image)
            cv2.imwrite(fileout,image)
            

    def decode(self, filein, codec):
        image = cv2.imread(filein)
        print(image) # for debugging      
        flag = True
        # convert into text
        if codec == 'binary':
            self.codec = Codec(self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(self.delimiter)
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # your code goes here
            # you may create an additional method that extract bits from the image array
            binary_data = ''
            for values in image:
                for pixel in values:
                    for color in pixel:
                        print(color)
                        if color % 2 == 0:
                        
                            binary_data+='0'
                        else:
                            binary_data+='1'

            # update the data attributes:
          

            self.text = self.codec.decode(binary_data.strip())
            self.binary = binary_data      
        
        return self.text       
        
    def print(self):  #prints encoded and decoded messages in text and binary forms
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)  

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()