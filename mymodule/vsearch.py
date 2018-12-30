def search4vowel(phrase:str)->set:
    '''Return any vowels found in a supplied phrase.'''
    return set(phrase).intersection({'a','e','i','o','u'})

def search4letter(phrase:str,letters:str='aeiou')->set:
    '''Return a set of letters found in a supplied phrase.'''
    return set(phrase).intersection(set(letters))
