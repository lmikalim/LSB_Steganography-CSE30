from codec import Codec

if __name__ == '__main__':
    text = 'hello' 
    #text = 'Casino Royale 10:30 Order martini' 
    print('Original:', text)
    
    c = Codec()
    binary = c.encode(text + c.delimiter)
    print('Binary:', binary)
    data = c.decode(binary)
    print('Text:', data) 
    
    # cc = CaesarCypher()
    # binary = cc.encode(text + cc.delimiter)
    # print('Binary:', binary)
    # data = cc.decode(binary)
    # print('Text:', data)
     
    # h = HuffmanCodes()
    # binary = h.encode(text + h.delimiter)
    # print('Binary:', binary)
    # data = h.decode(binary)
    # print('Text:', data)  