import time
# Implementation of Affine Cipher in Python 

# Extended Euclidean Algorithm for finding modular inverse 
# eg: modinv(7, 26) = 15 
def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 

def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None # modular inverse does not exist 
    else: 
        return x % m 


# affine cipher encrytion function 
# returns the cipher text 
def encrypt(text, key): 
    ''' 
    C = (a*P + b) % 26 
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
            + ord('A')) for t in text.upper().replace(' ', '') ]) 


# affine cipher decryption function 
# returns original text 
def decrypt(cipher, key): 
    ''' 
    P = (a^-1 * (C - b)) % 26 
    '''
    if modinv(key[0], 26) == None:
        print("\n\n[ERROR] Modular inverse does not exist\n\n")
        return ''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26)
             + ord('A')) for c in cipher ]) 


# Driver Code to test the above functions 
def main(): 
    # declaring text and key 
    #text = 'AFFINE CIPHER'
    text = 'Computer Security'
    #key = [17, 20] 
    key = [13,13]
    
    # calling encryption function 
    affine_encrypted_text = encrypt(text, key) 
    
    print('Encrypted Text: {}'.format( affine_encrypted_text )) 
    
    # calling decryption function 
    print('Decrypted Text: {}'.format
    ( decrypt(affine_encrypted_text, key) )) 


if __name__ == '__main__': 
    main() 
# This code is contributed by 
# Bhushan Borole 
