
def pig_latin_v2(str):
    
    diferent_vogal_count = 0
    double_different_vogal_word = False
    previews_vogal = ''

    
    for letter in str:
        if(letter in 'aeiou' and previews_vogal != letter):
            diferent_vogal_count += 1
            previews_vogal = letter
        if(diferent_vogal_count == 2):
            double_different_vogal_word = True
            break
        

    if(double_different_vogal_word == True):
        return f"{str[0:]}way"
    else:
        return f"{str[1:]}{str[0]}ay"

print(pig_latin_v2("wind"))
print(pig_latin_v2("wine"))


