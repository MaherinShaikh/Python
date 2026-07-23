
def create_character(characterName, strength, intelligence, charisma):
    if not isinstance(characterName, str):
        return 'The character name should be a string'
    if characterName == "":
        return 'The character should have a name'
    if len(characterName) > 10:
        return 'The character name is too long'
    if " " in characterName:
        return 'The character name should not contain spaces'
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return "All stats should be integers"
    if strength<1 or intelligence<1 or charisma<1:
        return 'All stats should be no less than 1'
    if strength>4 or intelligence>4 or charisma>4:
        return 'All stats should be no more than 4'
    if (strength+intelligence+charisma) !=7:
        return 'The character should start with 7 points'

    full_dot = '●'
    empty_dot = '○'

    str_bar = (full_dot * strength) + (empty_dot * (10 - strength))
    int_bar = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_bar = (full_dot * charisma) + (empty_dot * (10 - charisma))

    return f"{characterName}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"


result = create_character('ren', 4, 2, 1)
print(result)

# create_character('ren', 4, 2, 1) should return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.