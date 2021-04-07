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
  ['High', ['Bought In High']],
  ['Low', ['Bought In Low']],
  ['Neutral', ['Bought In Neutral']],
]

drink = [
  ['(.*)', ['%1']],
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
