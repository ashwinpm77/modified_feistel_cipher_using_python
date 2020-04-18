# Feistel Cipher (Modified)

import sys

# key_constants = [
#     '0x9E3779B9', '0x78DDE6E6', '0xE3779B99', '0x8DDE6E67',
#     '0x3779B99E', '0xDDE6E678', '0x779B99E3', '0xDE6E678D',
#     '0x3C6EF373', '0xF1BBCDCC', '0xC6EF3733', '0x1BBCDCCF',
#     '0x6EF3733C', '0xBBCDCCF1', '0xEF3733C6', '0xBCDCCF1B'
# ]

# Key Constants
key_constants = [
    '10011110001101110111100110111001',
    '01111000110111011110011011100110',
    '11100011011101111001101110011001',
    '10001101110111100110111001100111',
    '00110111011110011011100110011110',
    '11011101111001101110011001111000',
    '01110111100110111001100111100011',
    '11011110011011100110011110001101',
    '00111100011011101111001101110011',
    '11110001101110111100110111001100',
    '11000110111011110011011100110011',
    '00011011101111001101110011001111',
    '01101110111100110111001100111100',
    '10111011110011011100110011110001',
    '11101111001101110011001111000110',
    '10111100110111001100111100011011'
]



# s_box = [
#     '0x2989A1A8', '0x05858184', '0x16C6D2D4', '0x13C3D3D0', '0x14445054', '0x1D0D111C', '0x2C8CA0AC', '0x25052124',
#     '0x1D4D515C', '0x03434340', '0x18081018', '0x1E0E121C', '0x11415150', '0x3CCCF0FC', '0x0ACAC2C8', '0x23436360',
#     '0x28082028', '0x04444044', '0x20002020', '0x1D8D919C', '0x20C0E0E0', '0x22C2E2E0', '0x08C8C0C8', '0x17071314',
#     '0x2585A1A4', '0x0F8F838C', '0x03030300', '0x3B4B7378', '0x3B8BB3B8', '0x13031310', '0x12C2D2D0', '0x2ECEE2EC',
#     '0x30407070', '0x0C8C808C', '0x3F0F333C', '0x2888A0A8', '0x32023230', '0x1DCDD1DC', '0x36C6F2F4', '0x34447074',
#     '0x2CCCE0EC', '0x15859194', '0x0B0B0308', '0x17475354', '0x1C4C505C', '0x1B4B5358', '0x3D8DB1BC', '0x01010100',
#     '0x24042024', '0x1C0C101C', '0x33437370', '0x18889098', '0x10001010', '0x0CCCC0CC', '0x32C2F2F0', '0x19C9D1D8',
#     '0x2C0C202C', '0x27C7E3E4', '0x32427270', '0x03838380', '0x1B8B9398', '0x11C1D1D0', '0x06868284', '0x09C9C1C8',
#     '0x20406060', '0x10405050', '0x2383A3A0', '0x2BCBE3E8', '0x0D0D010C', '0x3686B2B4', '0x1E8E929C', '0x0F4F434C',
#     '0x3787B3B4', '0x1A4A5258', '0x06C6C2C4', '0x38487078', '0x2686A2A4', '0x12021210', '0x2F8FA3AC', '0x15C5D1D4',
#     '0x21416160', '0x03C3C3C0', '0x3484B0B4', '0x01414140', '0x12425250', '0x3D4D717C', '0x0D8D818C', '0x08080008',
#     '0x1F0F131C', '0x19899198', '0x00000000', '0x19091118', '0x04040004', '0x13435350', '0x37C7F3F4', '0x21C1E1E0',
#     '0x3DCDF1FC', '0x36467274', '0x2F0F232C', '0x27072324', '0x3080B0B0', '0x0B8B8388', '0x0E0E020C', '0x2B8BA3A8',
#     '0x2282A2A0', '0x2E4E626C', '0x13839390', '0x0D4D414C', '0x29496168', '0x3C4C707C', '0x09090108', '0x0A0A0208',
#     '0x3F8FB3BC', '0x2FCFE3EC', '0x33C3F3F0', '0x05C5C1C4', '0x07878384', '0x14041014', '0x3ECEF2FC', '0x24446064',
#     '0x1ECED2DC', '0x2E0E222C', '0x0B4B4348', '0x1A0A1218', '0x06060204', '0x21012120', '0x2B4B6368', '0x26466264',
#     '0x02020200', '0x35C5F1F4', '0x12829290', '0x0A8A8288', '0x0C0C000C', '0x3383B3B0', '0x3E4E727C', '0x10C0D0D0',
#     '0x3A4A7278', '0x07474344', '0x16869294', '0x25C5E1E4', '0x26062224', '0x00808080', '0x2D8DA1AC', '0x1FCFD3DC',
#     '0x2181A1A0', '0x30003030', '0x37073334', '0x2E8EA2AC', '0x36063234', '0x15051114', '0x22022220', '0x38083038',
#     '0x34C4F0F4', '0x2787A3A4', '0x05454144', '0x0C4C404C', '0x01818180', '0x29C9E1E8', '0x04848084', '0x17879394',
#     '0x35053134', '0x0BCBC3C8', '0x0ECEC2CC', '0x3C0C303C', '0x31417170', '0x11011110', '0x07C7C3C4', '0x09898188',
#     '0x35457174', '0x3BCBF3F8', '0x1ACAD2D8', '0x38C8F0F8', '0x14849094', '0x19495158', '0x02828280', '0x04C4C0C4',
#     '0x3FCFF3FC', '0x09494148', '0x39093138', '0x27476364', '0x00C0C0C0', '0x0FCFC3CC', '0x17C7D3D4', '0x3888B0B8',
#     '0x0F0F030C', '0x0E8E828C', '0x02424240', '0x23032320', '0x11819190', '0x2C4C606C', '0x1BCBD3D8', '0x2484A0A4',
#     '0x34043034', '0x31C1F1F0', '0x08484048', '0x02C2C2C0', '0x2F4F636C', '0x3D0D313C', '0x2D0D212C', '0x00404040',
#     '0x3E8EB2BC', '0x3E0E323C', '0x3C8CB0BC', '0x01C1C1C0', '0x2A8AA2A8', '0x3A8AB2B8', '0x0E4E424C', '0x15455154',
#     '0x3B0B3338', '0x1CCCD0DC', '0x28486068', '0x3F4F737C', '0x1C8C909C', '0x18C8D0D8', '0x0A4A4248', '0x16465254',
#     '0x37477374', '0x2080A0A0', '0x2DCDE1EC', '0x06464244', '0x3585B1B4', '0x2B0B2328', '0x25456164', '0x3ACAF2F8',
#     '0x23C3E3E0', '0x3989B1B8', '0x3181B1B0', '0x1F8F939C', '0x1E4E525C', '0x39C9F1F8', '0x26C6E2E4', '0x3282B2B0',
#     '0x31013130', '0x2ACAE2E8', '0x2D4D616C', '0x1F4F535C', '0x24C4E0E4', '0x30C0F0F0', '0x0DCDC1CC', '0x08888088',
#     '0x16061214', '0x3A0A3238', '0x18485058', '0x14C4D0D4', '0x22426260', '0x29092128', '0x07070304', '0x33033330',
#     '0x28C8E0E8', '0x1B0B1318', '0x05050104', '0x39497178', '0x10809090', '0x2A4A6268', '0x2A0A2228', '0x1A8A9298'
# ]

# Substitution Box
s_box = [
    '00101001100010011010000110101000',
    '00000101100001011000000110000100',
    '00010110110001101101001011010100',
    '00010011110000111101001111010000',
    '00010100010001000101000001010100',
    '00011101000011010001000100011100',
    '00101100100011001010000010101100',
    '00100101000001010010000100100100',
    '00011101010011010101000101011100',
    '00000011010000110100001101000000',
    '00011000000010000001000000011000',
    '00011110000011100001001000011100',
    '00010001010000010101000101010000',
    '00111100110011001111000011111100',
    '00001010110010101100001011001000',
    '00100011010000110110001101100000',
    '00101000000010000010000000101000',
    '00000100010001000100000001000100',
    '00100000000000000010000000100000',
    '00011101100011011001000110011100',
    '00100000110000001110000011100000',
    '00100010110000101110001011100000',
    '00001000110010001100000011001000',
    '00010111000001110001001100010100',
    '00100101100001011010000110100100',
    '00001111100011111000001110001100',
    '00000011000000110000001100000000',
    '00111011010010110111001101111000',
    '00111011100010111011001110111000',
    '00010011000000110001001100010000',
    '00010010110000101101001011010000',
    '00101110110011101110001011101100',
    '00110000010000000111000001110000',
    '00001100100011001000000010001100',
    '00111111000011110011001100111100',
    '00101000100010001010000010101000',
    '00110010000000100011001000110000',
    '00011101110011011101000111011100',
    '00110110110001101111001011110100',
    '00110100010001000111000001110100',
    '00101100110011001110000011101100',
    '00010101100001011001000110010100',
    '00001011000010110000001100001000',
    '00010111010001110101001101010100',
    '00011100010011000101000001011100',
    '00011011010010110101001101011000',
    '00111101100011011011000110111100',
    '00000001000000010000000100000000',
    '00100100000001000010000000100100',
    '00011100000011000001000000011100',
    '00110011010000110111001101110000',
    '00011000100010001001000010011000',
    '00010000000000000001000000010000',
    '00001100110011001100000011001100',
    '00110010110000101111001011110000',
    '00011001110010011101000111011000',
    '00101100000011000010000000101100',
    '00100111110001111110001111100100',
    '00110010010000100111001001110000',
    '00000011100000111000001110000000',
    '00011011100010111001001110011000',
    '00010001110000011101000111010000',
    '00000110100001101000001010000100',
    '00001001110010011100000111001000',
    '00100000010000000110000001100000',
    '00010000010000000101000001010000',
    '00100011100000111010001110100000',
    '00101011110010111110001111101000',
    '00001101000011010000000100001100',
    '00110110100001101011001010110100',
    '00011110100011101001001010011100',
    '00001111010011110100001101001100',
    '00110111100001111011001110110100',
    '00011010010010100101001001011000',
    '00000110110001101100001011000100',
    '00111000010010000111000001111000',
    '00100110100001101010001010100100',
    '00010010000000100001001000010000',
    '00101111100011111010001110101100',
    '00010101110001011101000111010100',
    '00100001010000010110000101100000',
    '00000011110000111100001111000000',
    '00110100100001001011000010110100',
    '00000001010000010100000101000000',
    '00010010010000100101001001010000',
    '00111101010011010111000101111100',
    '00001101100011011000000110001100',
    '00001000000010000000000000001000',
    '00011111000011110001001100011100',
    '00011001100010011001000110011000',
    '00000000000000000000000000000000',
    '00011001000010010001000100011000',
    '00000100000001000000000000000100',
    '00010011010000110101001101010000',
    '00110111110001111111001111110100',
    '00100001110000011110000111100000',
    '00111101110011011111000111111100',
    '00110110010001100111001001110100',
    '00101111000011110010001100101100',
    '00100111000001110010001100100100',
    '00110000100000001011000010110000',
    '00001011100010111000001110001000',
    '00001110000011100000001000001100',
    '00101011100010111010001110101000',
    '00100010100000101010001010100000',
    '00101110010011100110001001101100',
    '00010011100000111001001110010000',
    '00001101010011010100000101001100',
    '00101001010010010110000101101000',
    '00111100010011000111000001111100',
    '00001001000010010000000100001000',
    '00001010000010100000001000001000',
    '00111111100011111011001110111100',
    '00101111110011111110001111101100',
    '00110011110000111111001111110000',
    '00000101110001011100000111000100',
    '00000111100001111000001110000100',
    '00010100000001000001000000010100',
    '00111110110011101111001011111100',
    '00100100010001000110000001100100',
    '00011110110011101101001011011100',
    '00101110000011100010001000101100',
    '00001011010010110100001101001000',
    '00011010000010100001001000011000',
    '00000110000001100000001000000100',
    '00100001000000010010000100100000',
    '00101011010010110110001101101000',
    '00100110010001100110001001100100',
    '00000010000000100000001000000000',
    '00110101110001011111000111110100',
    '00010010100000101001001010010000',
    '00001010100010101000001010001000',
    '00001100000011000000000000001100',
    '00110011100000111011001110110000',
    '00111110010011100111001001111100',
    '00010000110000001101000011010000',
    '00111010010010100111001001111000',
    '00000111010001110100001101000100',
    '00010110100001101001001010010100',
    '00100101110001011110000111100100',
    '00100110000001100010001000100100',
    '00000000100000001000000010000000',
    '00101101100011011010000110101100',
    '00011111110011111101001111011100',
    '00100001100000011010000110100000',
    '00110000000000000011000000110000',
    '00110111000001110011001100110100',
    '00101110100011101010001010101100',
    '00110110000001100011001000110100',
    '00010101000001010001000100010100',
    '00100010000000100010001000100000',
    '00111000000010000011000000111000',
    '00110100110001001111000011110100',
    '00100111100001111010001110100100',
    '00000101010001010100000101000100',
    '00001100010011000100000001001100',
    '00000001100000011000000110000000',
    '00101001110010011110000111101000',
    '00000100100001001000000010000100',
    '00010111100001111001001110010100',
    '00110101000001010011000100110100',
    '00001011110010111100001111001000',
    '00001110110011101100001011001100',
    '00111100000011000011000000111100',
    '00110001010000010111000101110000',
    '00010001000000010001000100010000',
    '00000111110001111100001111000100',
    '00001001100010011000000110001000',
    '00110101010001010111000101110100',
    '00111011110010111111001111111000',
    '00011010110010101101001011011000',
    '00111000110010001111000011111000',
    '00010100100001001001000010010100',
    '00011001010010010101000101011000',
    '00000010100000101000001010000000',
    '00000100110001001100000011000100',
    '00111111110011111111001111111100',
    '00001001010010010100000101001000',
    '00111001000010010011000100111000',
    '00100111010001110110001101100100',
    '00000000110000001100000011000000',
    '00001111110011111100001111001100',
    '00010111110001111101001111010100',
    '00111000100010001011000010111000',
    '00001111000011110000001100001100',
    '00001110100011101000001010001100',
    '00000010010000100100001001000000',
    '00100011000000110010001100100000',
    '00010001100000011001000110010000',
    '00101100010011000110000001101100',
    '00011011110010111101001111011000',
    '00100100100001001010000010100100',
    '00110100000001000011000000110100',
    '00110001110000011111000111110000',
    '00001000010010000100000001001000',
    '00000010110000101100001011000000',
    '00101111010011110110001101101100',
    '00111101000011010011000100111100',
    '00101101000011010010000100101100',
    '00000000010000000100000001000000',
    '00111110100011101011001010111100',
    '00111110000011100011001000111100',
    '00111100100011001011000010111100',
    '00000001110000011100000111000000',
    '00101010100010101010001010101000',
    '00111010100010101011001010111000',
    '00001110010011100100001001001100',
    '00010101010001010101000101010100',
    '00111011000010110011001100111000',
    '00011100110011001101000011011100',
    '00101000010010000110000001101000',
    '00111111010011110111001101111100',
    '00011100100011001001000010011100',
    '00011000110010001101000011011000',
    '00001010010010100100001001001000',
    '00010110010001100101001001010100',
    '00110111010001110111001101110100',
    '00100000100000001010000010100000',
    '00101101110011011110000111101100',
    '00000110010001100100001001000100',
    '00110101100001011011000110110100',
    '00101011000010110010001100101000',
    '00100101010001010110000101100100',
    '00111010110010101111001011111000',
    '00100011110000111110001111100000',
    '00111001100010011011000110111000',
    '00110001100000011011000110110000',
    '00011111100011111001001110011100',
    '00011110010011100101001001011100',
    '00111001110010011111000111111000',
    '00100110110001101110001011100100',
    '00110010100000101011001010110000',
    '00110001000000010011000100110000',
    '00101010110010101110001011101000',
    '00101101010011010110000101101100',
    '00011111010011110101001101011100',
    '00100100110001001110000011100100',
    '00110000110000001111000011110000',
    '00001101110011011100000111001100',
    '00001000100010001000000010001000',
    '00010110000001100001001000010100',
    '00111010000010100011001000111000',
    '00011000010010000101000001011000',
    '00010100110001001101000011010100',
    '00100010010000100110001001100000',
    '00101001000010010010000100101000',
    '00000111000001110000001100000100',
    '00110011000000110011001100110000',
    '00101000110010001110000011101000',
    '00011011000010110001001100011000',
    '00000101000001010000000100000100',
    '00111001010010010111000101111000',
    '00010000100000001001000010010000',
    '00101010010010100110001001101000',
    '00101010000010100010001000101000',
    '00011010100010101001001010011000'
]




# Feistel Function
def f_with_s_box(data, key):
    inter = xor(data, key)
    key_comp = complement(key)
    index = int(key_comp[-8:], 2)
    inter = xor(inter, s_box[index])
    return inter


# XOR function
def xor(a, b):
    output = ""
    for _ in range(len(a)):
        if a[_] == b[_]:
            output += "0"
        else:
            output += "1"
    return output
# Complement function
def complement(a):
    output = ""
    for _ in range(len(a)):
        if a[_] == "0":
            output += "1"
        else:
            output += "0"
    return output

# Key Generator Function
def key_generator(initial_key, no_of_keys):
    keys = []
    key = initial_key
    l = len(key)
    for _ in range(0, no_of_keys):
        L = key[:int(l/2)]
        R = key[int(l/2):]
        L = (L+L[0])[1:]
        R = (R+R[0])[1:]
        key = R+L
        keys.append(xor(xor(L, R), key_constants[_]))
    return keys

# Function to convert hexadecimal array to binary string
def hex_key_to_bin(hex_array):
    bin_string = ""
    for i in hex_array:
        x = bin(int(i, 16))[2:]
        xl = len(x)
        if xl < 8:
            x = ("0"*(8-xl)) + x
        bin_string += x
    return bin_string
    


                      
# Encipher Fucntion
def encipher(plain_text_darray, keys, F):
    cipher = []
    for pt in plain_text_darray:
        pt1 = pt[0]
        pt2 = pt[1]
        pt_inter1 = pt1
        pt_inter2 = pt2
        for key in keys:
            L1, R1 = pt_inter1[:32], pt_inter1[32:]
            L2, R2 = pt_inter2[:32], pt_inter2[32:]
            inter1 = xor(L1, F(R1, key))
            inter2 = xor(L2, F(R2, key))
            pt_inter1 = R1+complement(inter2)
            pt_inter2 = R2+complement(inter1)
        cipher.append([inter1+R1, inter2+R2])
    return cipher


# Decipher Function
def decipher(cipher_text_darray, keys, F):
    plain_text = []
    for ct in cipher_text_darray:
        ct1 = ct[0]
        ct2 = ct[1]
        ct_inter1 = ct1
        ct_inter2 = ct2
        for key in keys:
            L1, R1 = ct_inter1[:32], ct_inter1[32:]
            L2, R2 = ct_inter2[:32], ct_inter2[32:]
            inter1 = xor(L1, F(R1, key))
            inter2 = xor(L2, F(R2, key))
            ct_inter1 = R1+complement(inter2)
            ct_inter2 = R2+complement(inter1)
        plain_text.append([inter2+R2, inter1+R1])
    return plain_text


# Function to convert text to binary array
def text_to_binarray(text):
    bin_array = []
    text_bin = ""
    for i in text:
        x = bin(ord(i))[2:]
        if len(x) < 8:
            text_bin += (("0"*(8-len(x))) + x)
        else:
            text_bin += x
    ptlen = len(text_bin)
    if ptlen%64 != 0:
        x = ptlen%64
        text_bin += ("0"*(64-x))
    ptlen = len(text_bin)
    for i in range(0, ptlen, 64):
        bin_array.append(text_bin[i:i+64])
    return bin_array


# Function to convert binary array to text
def bin_array_to_text(bin_array):
    text = ""
    for _ in bin_array:
        for __ in range(0, 64, 8):
            text += chr(int(_[__:__+8], 2))
    return text



# Function to convert binary array to hexadecimal
def bin_array_to_hex(bin_array):
    hex_ = "0x"
    for _ in bin_array:
        for __ in range(0, 64, 8):
            x = hex(int(_[__:__+8], 2))[2:]
            xl = len(x)
            if xl < 2:
                x = ("0"*(2-xl)) + x
            hex_ += x
    return hex_



# Function to convert binary array to array having array of two elements    
def bin_array_to_double_array(bin_array):
    arr = []
    l = len(bin_array)
    if l%2 == 1:
        bin_array.append(("0"*64))
    for i in range(0, l, 2):
        arr.append([bin_array[i], bin_array[i+1]])
    return arr

# Function to convert array having array of two elements to a single array
def double_array_to_bin_array(double_array):
    arr = []
    for i in double_array:
        arr.append(i[0])
        arr.append(i[1])
    return arr
            
    
# Function to remove nulls from the end of the deciphered text
def remove_null(string):
    ip = -1
    while string[ip] == '\x00':
        ip -= 1
    return string[:ip+1]



# def something(consts):
#     y = []
#     for i in consts:
#         x = bin(int(i, 16))[2:]
#         xl = len(x)
#         if xl < 32:
#             x = ("0"*(32-xl))+x
#         y.append(x)
#     return y
# len(something(s_box))


def main():
    if len(sys.argv) != 4:
        print("Enter proper commandline argument as\n<key_file> <e | d> <filename>\ne for encryption\nd for decryption\n<key_file> contains key (8 two digit hexadecimal seperated by space)\n<filename> contains the data")
    else:
        key = open(sys.argv[1], "r").read().split()[:8]
        option = sys.argv[2]
        file_data = open(sys.argv[3], "r").read()
        keys = key_generator(hex_key_to_bin(key), 16)
        if option == 'e':
            cipher_text = bin_array_to_text(double_array_to_bin_array(encipher(bin_array_to_double_array(text_to_binarray(file_data)), keys, f_with_s_box)))
            open("crypto_output", "w").write(cipher_text)
        elif option == 'd':
            keys.reverse()
            plain_text = remove_null(bin_array_to_text(double_array_to_bin_array(decipher(bin_array_to_double_array(text_to_binarray(file_data)), keys, f_with_s_box))))
            open("crypto_output", "w").write(plain_text)
        else:
            print("Invalid option")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Error: check filenames exist or not.")
