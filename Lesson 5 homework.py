#make something like Rock, Paper, Scissors, but give it more options.
#Give it at least two more options, like Fire, Water, Earth, Air, Wind.
#extra effects for extra points!
from random import randint
import time 
from gtts import gTTS 

computer_senpai = randint(0,4)
print('Welcome to the Muppets Dating App! \n Are you \'Kermit\', \'Miss Piggy\', \'Fozzie\', \'Beaker\', or \'Janice\'?')
def main():
    player_character = input('Who are you? ')
    if player_character == 'Kermit' or player_character == 'kermit' or player_character == 'green frog' or player_character == 'Kermie':
        #This is the Kermit Option
        print('Welcome Kermit. How\'s the rainbow?')
        time.sleep(2)
        print('We have hot singles in your area!')
        time.sleep(1)
        date = input('Would you like to date \'Miss Piggy\' or do you want to give \'Janice\' a spin? \n')
        if date == 'Miss Piggy' or date == 'pig' or date == 'miss piggy' or date == 'piggy':
            print('Calling \'Miss Piggy\'. Please wait.')
            time.sleep(3)
            response = randint(0,2)
            if response == 0 or response == 1:
                print('Piggy: You better beat it, mister, before my pork hock slams into your puny face!')
                time.sleep(2.5)
                print('Oh well. You tried.')
            else:
                print('Piggy: Oh hi Kermie! How are you? XOXOXO')
                time.sleep(2.5)
                print('That\'s digusting. At least you got the skills.')
        elif date == 'Janice' or date == 'janice':
            print('Calling \'Janice\'')
            time.sleep(3)
            janice_decision = randint(0,2)
            if janice_decision == 0 or janice_decision == 1:
                print('Janice: Hi there! You\'ve reached my mailbox. I\'m probably with the band or making a movie. Have a nice day!')
                time.sleep(2.5)
                print('I suppose she\'s hard to get. Tough luck, man.')
            if janice_decision == 2:
                print('Hhellloo there. What do we have here? I suppose I can give you a try.')
                time.sleep(2.5)
                print('Wowee mate. You got them skills.')
        else:
            print('I regret I do not have ' + date + ' in my contact lists.')
            time.sleep(1.5)
            print('Have a nice day!')
    elif player_character == 'Miss Piggy' or player_character == 'pig' or player_character == 'miss piggy' or player_character == 'piggy':
        #Miss Piggy option
        print('Hello Piggy. Ya cheatin\' on Kermie, or you hungry for more?')
        time.sleep(2)
        print('We have hot singles in your area!')
        time.sleep(1)
        pig = input('Would you like to date \'Fozzie Bear\', \'Kermit\', or do you want to give \'Beaker\' a spin? \n')
        if pig == 'Kermit' or pig == 'Kermie' or pig == 'frog' or pig == 'kermit':
            print('Calling \'Kermit\'. Please wait.')
            time.sleep(3)
            response = randint(0,2)
            if response == 0 or response == 1:
                print('Kermit: Uh, hey Piggy. Um. I\'m kinda busy right now. Um. Bye.')
                time.sleep(2.5)
                print('Oh well. Guys are weird sometimes. Go easy on him, will ya?')
            else:
                print('Kermit: Uh, hey Piggy. You wanna get together? Um. *gulp* Sure.')
                time.sleep(2.5)
                print('Smooth. You got your guy back. But don\'t throw him away again.')
        elif pig == 'Fozzie' or pig == 'Fozzie Bear' or pig == 'fozzie bear' or pig == 'fozzie' or pig == 'bear':
            print('Calling \'Fozzie Bear\'')
            time.sleep(3)
            fozz_decision = randint(0,2)
            if fozz_decision == 0 or fozz_decision == 1:
                print('Fozzie: Hey there, ho there! Unfortunately, you landed in my mailbox!')
                time.sleep(1.5)
                print('Fozzie: Perhaps I put you in spam. Oh well. Back to intensive cliff-jumping!')
                time.sleep(2.5)
                print('That\'s awkward. I guess he didn\'t want complications with Kermit.')
            if fozz_decision == 2:
                print('Fozzie: Oho there. Does Kermit know about this?')
                time.sleep(1.5)
                print('I suppose it doesn\' matter.')
                time.sleep(2.5)
                print('If computers had emotions, I\'d be crying alongside Kermit right now.')
        elif pig == 'Beaker' or pig == 'beaker' or pig == 'stupid':
            print('Calling \'Beaker\'')
            time.sleep(3)
            beaker_response = randint(1,2)
            if beaker_response == 1:
                print('Beaker: MMEEEEEEEEEEEPPPPPPPPPPPPPP!!!!!')
                time.sleep(2.5)
                print('That will be an unforgettable response. I think he said, \'NNOOOOOOOOO!\'')
            if beaker_response == 2:
                print('Beaker: meep.')
                time.sleep(2.5)
                print('Nice job getting hooked up to a mad scientist.')
        else:
            print('I regret I do not have ' + pig + ' in my contact lists.')
            time.sleep(1.5)
            print('Have a nice day!')
    elif player_character == 'Fozzie' or player_character == 'Fozzie Bear' or player_character == 'fozzie' or player_character == 'fozzie bear' or player_character == 'bear':
        print('Hey ho Fozzie! Nice to see you, old chum.')
        time.sleep(2)
        print('Hot singles in your area!')
        time.sleep(1)
        fozz_b = input('\'Miss Piggy\' and \'Janice\' are single, and ready to mingle! Take your pick!\n')
        if fozz_b == 'Miss Piggy' or fozz_b == 'pig' or fozz_b == 'miss piggy' or fozz_b == 'piggy':
            print('Calling \'Miss Piggy\'. Please wait.')
            time.sleep(3)
            response = randint(0,2)
            if response == 0 or response == 1:
                print('Piggy: You\'re not worth my time, bear. Get out of here.')
                time.sleep(2.5)
                print('Oh well. You tried.')
            else:
                print('Piggy: Rawr. You look tempting')
                time.sleep(2.5)
                print('That\'s digusting. My job here is done.')
        elif fozz_b == 'Janice' or fozz_b == 'janice':
            print('Calling \'Janice\'')
            time.sleep(3)
            janice_decision = randint(0,2)
            if janice_decision == 0 or janice_decision == 1:
                print('Janice: Hi there! You\'ve reached my mailbox. I\'m probably with the band or making a movie. Have a nice day!')
                time.sleep(2.5)
                print('Tough luck, man.')
            if janice_decision == 2:
                print('Mhm. Not bad, not bad. I guess I can try you.')
                time.sleep(2.5)
                print('Hey there, ho there, indeed. Nice work.')
        else:
            print('I regret I do not have ' + fozz_b + ' in my contact lists.')
            time.sleep(1.5)
            print('Have a nice day!')
    elif player_character == 'Beaker' or player_character == 'beaker' or player_character == 'scientist':
        print('Welcome Beaker. Nice to see that your head hasn\'t been blown off by the doctor.')
        time.sleep(2)
        print('We found some hot singles in your area!')
        time.sleep(1)
        beak = input('We found \'Miss Piggy\' and \'Janice\'! Take your pick.\n')
        if beak == 'Miss Piggy' or beak == 'pig' or beak == 'miss piggy' or beak == 'piggy':
            print('Calling \'Miss Piggy\'. Please wait.')
            time.sleep(3)
            response = randint(0,3)
            if response == 0 or response == 1 or response == 3:
                print('Piggy:')
                time.sleep(4)
                print('Poor guy. Don\'t worry about it. There are always more fish in the sea.')
            else:
                print('Piggy: Oh boy. I\'d rather date a twig.')
                time.sleep(2.5)
                print('Ouch. Maybe a workout or two would help.')
        elif beak == 'Janice' or beak == 'janice':
            print('Calling \'Janice\'')
            time.sleep(3)
            janice_decision = randint(0,2)
            if janice_decision == 0 or janice_decision == 1:
                print('Janice: Hi there! You\'ve reached my mailbox. I\'m probably with the band or making a movie. Have a nice day!')
                time.sleep(2.5)
                print('Tough luck, man.')
            if janice_decision == 2:
                print('Janice:')
                time.sleep(2.5)
                print('Poor guy. Don\'t worry about it. There are always more fish in the sea.')
        else:
            print('I regret I do not have ' + beak + ' in my contact lists.')
            time.sleep(1.5)
            print('Have a nice day!')
    elif player_character == 'Janice' or player_character == 'janice':
        print('Welcome Janice. How\'s the band going?')
        time.sleep(2)
        print('We have hot singles in your area!')
        time.sleep(1)
        jan = input('Would you like to date \'Fozzie Bear\', \'Kermit\', or do you want to give \'Beaker\' a spin? \n')
        if jan == 'Kermit' or jan == 'Kermie' or jan == 'frog' or jan == 'kermit':
            print('Calling \'Kermit\'. Please wait.')
            time.sleep(3)
            response = randint(0,2)
            if response == 0 or response == 1:
                print('Kermit: Oh hey there, Janice. Sorry, can\'t do this to Piggy.')
                time.sleep(2.5)
                print('It takes real maturity to say that type of stuff. Kudos to him.')
            else:
                print('Kermit: What\'s up? You want a raise?')
                time.sleep(2)
                print('Kermit: Oh. Sorry, can\'t do that to Piggy. Seeya around.')
                time.sleep(2.5)
                print('Well. That cancels him out.')
        elif jan == 'Fozzie' or jan == 'Fozzie Bear' or jan == 'fozzie bear' or jan == 'fozzie' or jan == 'bear':
            print('Calling \'Fozzie Bear\'')
            time.sleep(3)
            fozz_decision = randint(0,2)
            if fozz_decision == 0 or fozz_decision == 1:
                print('Fozzie: Hey there, ho there! Unfortunately, you landed in my mailbox!')
                time.sleep(1.5)
                print('Fozzie: Perhaps I put you in spam. Oh well. Back to intensive cliff-jumping!')
                time.sleep(2.5)
                print('You gotta like a guy for that.')
            if fozz_decision == 2:
                print('Fozzie: Oho there. Anything for you, mi\'lady.')
                time.sleep(2.5)
                print('Very gentleman-like. Smooth.')
        elif jan == 'Beaker' or jan == 'beaker' or jan == 'stupid':
            print('Calling \'Beaker\'')
            time.sleep(3)
            beaker_response = randint(1,2)
            if beaker_response == 1:
                print('Beaker: MMEEEEEEEEEEEPPPPPPPPPPPPPP!!!!!')
                time.sleep(2.5)
                print('That will be an unforgettable response. I think he said, \'NNOOOOOOOOO!\'')
            if beaker_response == 2:
                print('Beaker: meep.')
                time.sleep(2.5)
                print('Nice job getting hooked up to a mad scientist.')
        else:
            print('I regret I do not have ' + jan + ' in my contact lists.')
            time.sleep(1.5)
            print('Have a nice day!')
    else: 
        print('Sorry ' + player_character + ', try another website.')
while True:
    main()
    time.sleep(2)
    choice = input('Try again? Type \'yes\' or \'no\'.\n')
    if choice == 'no' or choice == 'No' or choice == 'NO':
        time.sleep(1)
        print('I hope you had fun.\nGood bye!')
        time.sleep(4)
        exit()
    else:
        time.sleep(1)
        print('Good luck!\n')
        time.sleep(3)