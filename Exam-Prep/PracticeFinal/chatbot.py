"""Functions for simple chatbot project."""
import random

def get_input():
    """ask user for an input message"""
    
    # get input from user on execution
    # for chatbot to respond to
    msg = input('INPUT :\t')
    out_msg = None
    
    return msg, out_msg


def is_question(input_msg):
    """determine if input from user contains a question

    Parameters
    ----------
    input_msg : str
        string containing input from user

    Returns
    -------
    out_msg : bool
        Boolean indicating True if input is a question; False otherwise

    """
    if '?' in input_msg:
        out_msg = True
    else:
        out_msg = False
    return out_msg


def end_chat(input_msg):
    """determine if 'quit' included in message; if yes, end the chat

    Parameters
    ----------
    input_msg : str
        input from user to be evaluated

    Returns
    -------
    out_msg : str or None
        Returns 'Bye' if 'quit' in input; otherwise, None
    chat : bool
        True if chat is to continue; False if chat is to end
    """

    if 'quit' in input_msg:
        out_msg = 'Bye' 
        chat = False
    else:
        out_msg = None
        chat = True      
    return out_msg, chat

def about_ucsd(input_string):
    
    to_check = ['UCSD', 
                'ucsd', 
                'UC San Diego', 
                'University of California, San Diego']
    # if at least one in to_check matches
    # input string, return True
    out = any(val in input_string for val in to_check) 
    
    return out


def return_message(out_msg, question, ucsd):
    
    """
    Parameters
    ----------
    out_msg : str
        message to be returned from chatbot

    question : bool
        Boolean indicating if the uer asked a question (True if yes; False otherwise)

    ucsd : bool
        Boolean indicating if the user mentioned UCSD (True if yes; False otherwise)
    """

    ucsd_facts = ['UCSD sits on the ancestral homelands of the Kumeyaay Nation.',
                  'UCSD has more than 220,000 Eucalyptus trees on its campus.',
                  'UCSD was founded in 1960.',
                  'UCSD receives more than $1B in research funding annually.',
                  'UCSD has more than 130 different majors and more than 40,000 students.'
                  ]

    if not out_msg:
        if question:
            out_msg = "I'm too shy to answer questions. What do you want to talk about?"
        else:
            # only return a ucsd_fact if NOT a question and IF UCSD mentioned
            if ucsd: 
                out_msg = random.choice(ucsd_facts)
            else:
                out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])
        
    return out_msg


def have_a_chat():
    """Main function to run our chatbot."""
  
    chat = True
    # chatbot will continue to execute until end_chat()
    # returns False, as indicated by 'quit' in chatbot input
    while chat:
        msg, out_msg = get_input()
        question = is_question(msg) 
        out_msg, chat = end_chat(msg)
        out_msg = return_message(out_msg=out_msg, question=question)
        
        print('OUTPUT:', out_msg)