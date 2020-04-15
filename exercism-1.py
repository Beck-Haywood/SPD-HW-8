# Bob is a lackadaisical teenager. In conversation, his responses are very limited.

# Bob answers 'Sure.' if you ask him a question, such as "How are you?".
# He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.

# Bob's conversational partner is a purist when it comes to written communication and always follows normal rules regarding sentence punctuation in English.
import string
def bob(response):
    if response == '':
        return 'Fine. Be that way!'
    elif response[len(response) - 1] == '?':
        if response.isupper() == True:
            return "Calm down, I know what I'm doing!"
        elif response.isupper() == False:
            return "Sure."
    elif response.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'

print('How are you?')
print(bob('How are you?'))
print('HEY WHAT!')
print(bob('HEY WHAT!'))
print('HEY WHAT ARE YOU DOING?')
print(bob('HEY WHAT ARE YOU DOING?'))
print('')
print(bob(''))
print('Bruh')
print(bob('Bruh'))

