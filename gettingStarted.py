
def welcome_assignment_answers(question):

    if question == "Are encoding and encryption the same? - Yes/No":
        return "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        return "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        return "No"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        return "mTCP"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        return "No"
    elif question == "What is the SHA256 hashing value to the following message: 'NYU Computer Networking' - Use SHA256 hash generator and use the answer in your code":
        return "883c13da6a24949c9a23231b60119e2ace58459da4f8bbdd812cc37764548bdd"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        return "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        return int(2)
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        return int(3)
    else:
        return 'The answer could not be determined'


#print(welcome_assignment_answers("Are encoding and encryption the same? - Yes/No"))
#print(welcome_assignment_answers("Is it possible to decrypt a message without a key? - Yes/No"))
#print(welcome_assignment_answers("Is it possible to decode a message without a key? - Yes/No"))
#print(welcome_assignment_answers("In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"))
#print(welcome_assignment_answers("Is a hashed message supposed to be un-hashed? - Yes/No"))
#print(welcome_assignment_answers("What is the SHA256 hashing value to the following message: 'NYU Computer Networking' - Use SHA256 hash generator and use the answer in your code"))
#print(welcome_assignment_answers("Is MD5 a secured hashing algorithm? - Yes/No"))
#print(welcome_assignment_answers("What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"))
#print(welcome_assignment_answers("What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"))

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print (welcome_assignment_answers("Are encoding and encryption the same? - Yes/No"))
