from nltk.chat.util import Chat, reflections
from .models import barMenu
import decimal

# pairs = [
#   ['Deal', ['Deal Done']],
#   ['No Deal', ['Deal Not Done']],
#   ['My name is (.*)', ['Hi %1']],
#   ['(hi|hello|hey|holla|hola)', ['Hey There', 'Hi There', 'Hayyy']],
#   ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
#   # ['(.*)(location|city)', 'Tokoyo', 'Japan'],
#   ['(.*) created you ?', ['Vrushit Created Me Using NLTK']],
#   ['How is the weather in (.*)', ['The weather in %1 is amazing like always']],
#   ['(.*)help(.*)', ['I can help you !']],
#   ['(.*) your name ?', ['My name is Sam']]
# ]

# Answers From Chatbot Be Like :-
# Your drink says you're about to get prettier, funnier and become a great dancer! DEAL?
# Shhh. don't worry, I won't tell anyone you made such an offer.
# 

price = [
  ['High', ['Just got your salary?', 'Are you sure you want to overpay?', "Finally got your Mom's Credit Card?"]],
  ['Low', ['You caught me at the right time. You sure you wanna go ahead?', 'Hit YES for an instant one-up', 'Are you from Wall Street?']],
  ['Neutral', ['Are you sure you wanna buy this drink?']],
]

drink = [
  ['Beer', ['The best beer is an open beer.', 'Beer doesn’t have many vitamins. That’s why you need to drink lots of it.', 'Save the earth, its the only planet with beer.', 'May you always have love in your heart and beer in your belly.', 'Every loaf of bread is a tragic story of a group of grains that could have become beer but didn’t.', 'In wine there is wisdom, in beer there is freedom, in water there is bacteria.', 'Beer is proof that God loves us and wants us to be happy.']],

  ['Whiskey', ['Dear Whiskey, we had a deal that you would make me prettier, funnier and a better dancer. I saw the video, we need to talk.', 'Whiskey is not the answer. Alcohol is the question. Yes is the answer.']],

  ['Cocktail', ['When you accidentally pour too much alcohol into your mixed drink and you have to just deal with it because your mother didn’t raise a quitter.', 'I know I should give up drinking but I am not a quitter.']],

  ['(.*) Wine', ['Always buy a bigger bottle than you think you’ll need. Better to be safe than sober.', 'Alcohol may be man’s worst enemy, but the bible says love your enemy.', 'Home is where the wine is.', 'Of course size matters. No one wants a small glass of wine.', 'In wine there is wisdom, in beer there is freedom, in water there is bacteria.']],

  ['Vodka', ['Vodka is not the answer, it just makes you forget the question.', 'Vodka – Because no great story ever started with someone eating a salad.', 'Vodka may not be the answer but it’s worth a shot.', 'I used to think drinking Vodka was bad for me… so I gave up thinking.']],

  ['(Gin|Cocktail)', ['To me "Drink Responsibly" means dont spill it.', 'You say alcoholism, I say liver crossfit.', 'Not to get technical but according to chemistry alcohol is a solution.', 'I said no to alcohol, but it just doesn’t listen.', 'Alcohol may not solve your problems, but neither will water or milk.', 'A party without alcohol is just a meeting.', 'I read an article that said if you drink every day you might be an alcoholic… thank God I only drink every night.']],

]


def bargaing( name, quantity ):
  ordered = barMenu.objects.all().filter(name=name)
  if len(ordered) > 0:
    drinktype = ordered[0].drinktype
    ordered[0].old_price = ordered[0].current_price

    all_drinks = barMenu.objects.all().filter(drinktype=drinktype).exclude(name=name)

    ordered[0].current_price = ordered[0].current_price + (ordered[0].actual_price * decimal.Decimal(quantity/100))
    ordered[0].tot_qty = ordered[0].tot_qty + quantity
    ordered[0].savings = ordered[0].actual_price - ordered[0].current_price
    
    if ordered[0].high < ordered[0].current_price:
      ordered[0].high = ordered[0].current_price

    if ordered[0].savings > 0:
      ordered[0].className = "green"
    else:
      ordered[0].className = "red"


    ordered[0].save()

    for i in all_drinks:
      i.old_price = i.current_price
      i.current_price = i.current_price - decimal.Decimal((ordered[0].actual_price * decimal.Decimal(quantity/100)/2))
      i.savings = i.actual_price - i.current_price

      if i.savings > 0:
        i.className = "green"
      else:
        i.className = "red"

      if i.low > i.current_price:
        i.low = i.current_price

      i.save()


    # ordered[0].name
    return 1
  else:
    return 0
  
def send_reply_price( user_msg ):
  chat = Chat(price, reflections) 
  reply = chat.respond(user_msg)
  return reply

def send_reply_drink( user_msg ):
  chat = Chat(drink, reflections) 
  reply = chat.respond(user_msg)
  return reply
