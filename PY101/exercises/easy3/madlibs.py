
def get_noun():
    noun = input('Enter a noun: ')
    return noun

def get_verb():
    verb = input('Enter a verb: ')
    return verb

def get_adjective():
    adjective = input('Enter an adjective: ')
    return adjective

def get_adverb():
    adverb = input('Enter an adverb: ')
    return adverb

def display_output():
    noun = get_noun()
    verb = get_verb()
    adjective = get_adjective()
    adverb = get_adverb()
    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
    print(f'The {adjective} {noun} {verb}s {adverb} over the lazy dog.')
    print(f"The {noun} {adverb} {verb}s up to Joe's blue turtle")

display_output()

    