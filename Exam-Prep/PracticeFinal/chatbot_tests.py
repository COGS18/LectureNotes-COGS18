from chatbot import is_question, end_chat, return_message

def test_is_question():
	assert callable(is_question)
	assert isinstance(is_question('?'), bool)
	assert is_question('?') == True
	assert is_question('cool?') == True
	assert is_question('cool') == False

def test_end_chat():
	assert callable(end_chat)
	assert isinstance(end_chat('quit'), tuple)
	assert end_chat('quit') == ('Bye', False)
	assert end_chat('hi') == (None, True)
	assert end_chat('this has quit in the middle') == ('Bye', False)

def test_return_message():
	ucsd_facts = ['UCSD sits on the ancestral homelands of the Kumeyaay Nation.',
	              'UCSD has more than 220,000 Eucalyptus trees on its campus.',
	              'UCSD was founded in 1960.',
	              'UCSD receives more than $1B in research funding annually.',
	              'UCSD has more than 130 different majors and more than 40,000 students.'
	             ]

	assert callable(test_return_message)
	assert isinstance(return_message(out_msg=None, question=True, ucsd=False), str)
	assert return_message(out_msg=None, question=True, ucsd=False) == "I'm too shy to answer questions. What do you want to talk about?"
	assert return_message(out_msg=None, question=True, ucsd=True) == "I'm too shy to answer questions. What do you want to talk about?"
	assert return_message(out_msg=None, question=False, ucsd=True) in ucsd_facts 
	assert return_message(out_msg=None, question=False, ucsd=False) in ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!']