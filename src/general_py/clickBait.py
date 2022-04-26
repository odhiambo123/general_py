import random

#constants:
obj_pronouns = ['Her', 'Him','Them']
possesive_pronouns = ['Her', 'His', 'Their']
personal_pronouns = ['She', 'He', 'They']
states = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania','Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
nouns = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent','Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado','Plastic Straw','Serial Killer', 'Telephone Psychic']
places = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement','Workplace', 'Donut Shop', 'Apocalypse Bunker']
When = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def main():
    print('Click Bait Headline Generator')

    while True:
        print('enter the number of headlines to generate: ')
        response = input('> ')
        if not response.isdecimal():
            print('please enter a number')
        else:
            numberOfHeadlines = int(response)
            break#exit the loop

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1,8)

        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()
        print(headline)
    print()

    website = random.choice(['website','blag', 'Facebuuk','Googles','Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(When).lower()
    print('Post these to our', website, when, 'or you\'re fired!')

def generateAreMillennialsKillingHeadline():
    noun = random.choice(nouns)
    return 'Are Millenials Killing the {} Industry'.format(noun)
def generateWhatYouDontKnowHeadline():
    noun = random.choice(nouns)
    pluralNoun = random.choice(nouns)
    when = random.choice(When)
    return 'without This {}, {} could Kill you {}'.format(noun, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(obj_pronouns)
    state = random.choice(states)
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    return 'Big Companies Hate {}! See How This {} {} Invented a cheaper {}'.format(pronoun, state, noun1, noun2)
def generateYouWontBelieveHeadline():
    state = random.choice(states)
    noun = random.choice(nouns)
    pronoun = random.choice(possesive_pronouns)
    place = random.choice(places)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun,pronoun, place)
def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(nouns) + 's'
    pluralNoun2 = random.choice(nouns) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)
def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(nouns)
    state = random.choice(states)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)
def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(nouns) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)
def generateJobAutomatedHeadline():
    state = random.choice(states)
    noun = random.choice(nouns)
    i = random.randint(0, 2)
    pronoun1 = possesive_pronouns[i]
    pronoun2 = personal_pronouns[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)
    # If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()