full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(strength(string)):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return 'All stats should be integers'
#My code below during July 11th 2026
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
#AI Assistance(Read the READ.ME File)
    str_bar = (full_dot * strength) + (empty_dot * (10 - strength))

    int_bar = (full_dot * intelligence) + (empty_dot * (10 - intelligence))

    cha_bar = (full_dot * charisma ) + (empty_dot * (10 - charisma))
    return f'{name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}'

create_character('ren', 4, 2, 1)
#When create_character is called, this is an example test code to know that it is fully functional
