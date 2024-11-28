# Text encryption/decryption - Final Assignment
# Create a command line interface where you can supply a message and a key value to encrypt the message using the Python cryptography module. 
# The message will be written to a file of the user's choice. 
# The script must be able to read text from a specified file and be able to decrypt a message using a supplied key value.
#
import os
import argparse
from cryptography.fernet import Fernet

# This function will generate a key to a key file in the same directory as this script, called myKey

def keyGenerator():
    
    # generates a binary key
    myKey = Fernet.generate_key()
    #this key can be used later when use Fernet to encrypt or decrypt a message
    
    # the key that was just generated is in binary format, so we need to 'write binary' instead of just 'write'
    with open("myKey", "wb") as file:
        file.write(myKey)

    print("Your key has been saved to the current directory, in a file called myKey")

# This function will encrypt a message with a key
def makeItASecret(myMessage, myKey, whereWeSaving):

    try:

        # error check if user doesnt type in a valid path for the Key File
        if not os.path.exists(myKey):

            print("ERROR: The key file you provided, " + myKey + ", does not exist.")

            return

        # read the key that was provided by the user, rb is used to 'read binary' data 
        with open(myKey, "rb") as file:
            myKey = file.read()

        # initialize the fernet object with the key that was just read, we'll use this to encrypt/decrypt
        fernet = Fernet(myKey)

        # error check if user doesnt type in a valid path for the Message File
        if not os.path.exists(myMessage):

            print("ERROR: The message file you provided, " + myMessage + ", does not exist.")

            return

        # read the message file provided by the user, its just plain text, so no need for 'b' this time 
        with open(myMessage, "r") as file:
            message = file.read()

        # convert the string message to bytes so we can use Fernet on it
        messageToBytes = message.encode()

        # encrypt the message that was just conveted to bytes with the key
        encryptedMsg = fernet.encrypt(messageToBytes)

        # write the encrypted message to a file in binary format
        with open(whereWeSaving, "wb") as file:
            file.write(encryptedMsg)

        print("Your encrypted message was saved to " + whereWeSaving)
        
    except Exception as x:
        print("ERROR: There was a problem during the encryption of your file. Details: " + str(x))

# This function will decrypt a message with a provided key file
def tellMeYourSecret(messageInABottle, myKey):

    try:
        
        # error check if user doesnt type in a valid path for the Key File
        if not os.path.exists(myKey):
            print("ERROR: The key file you provided, " + myKey + ", does not exist.")
            return

        # read the key file in binary format
        with open(myKey, "rb") as file:
            myKey = file.read()

        # initialize the fernet object with the key that was just read
        fernet = Fernet(myKey)

        # error check if user doesnt type in a valid path for the encrypted Message File
        if not os.path.exists(messageInABottle):

            print("ERROR: The encrypted message " + messageInABottle + " does not exist.")

            return

        # read the encrypted message from the file
        with open(messageInABottle, "rb") as file:
            encryptedMsg = file.read()

        # decrypt the message
        decryptedBytes = fernet.decrypt(encryptedMsg)
        
        # converts back to string
        decryptedMessage = decryptedBytes.decode()

        # print the message in plain txt 
        print("Decrypted message: ")
        print(decryptedMessage)

    except Exception as x:
        print("ERROR: There was a problem during the decryption of your file. Details: " + str(x))

# This function will handle the CLI args

def main():

    parser = argparse.ArgumentParser(description="Noah's encryption and decryption tool")
    
    # not expecting a value when the user does --generateKey, but still need to call the argument for the function, so added action="store_true"
    parser.add_argument('--generateKey', help="Generate a key and save it to a file", action="store_true")
    parser.add_argument('--encrypt', help="Path to the message to encrypt (also requires --key and --name)", type=str)
    parser.add_argument('--decrypt', help="Path to the message to decrypt (also requires --key)", type=str)
    parser.add_argument('--key', help="Key file for encryption/decryption", type=str)
    parser.add_argument('--name', help="Name for your encrypted message, saved to current directory", type=str)

    args = parser.parse_args()

    if args.generateKey:
        
        keyGenerator()
        
    elif args.encrypt:

        #make sure if theyre using encrpyt, theyre also gonna use key and name
        if not args.key or not args.name:
            
            print("ERROR: --encrypt requires --key and --name arguments.")
            
        else:
            makeItASecret(args.encrypt, args.key, args.name)
            
    elif args.decrypt:

        #make sure if theyre using decrypt, theyre also gonna use key 
        if not args.key:
            print("ERROR: --decrypt requires --key argument.")
        else:
            tellMeYourSecret(args.decrypt, args.key)
    else:
        print("No valid arguments provided. Use --help for help.")

main()
