from colorama import Fore, Style, init
from textblob import TextBlob
init(autoreset=True)
print(Fore.CYAN+"Welcome to sentiment spy")
name=input(Fore.MAGENTA+"Enter your name: ").strip()or "Friendly Agent"
print(Fore.CYAN+f"Hello Agent {name}!(exit | reset | history)")
history=[]
while True:
    text=input(Fore.GREEN+"You:").strip()
    if not text:
       print(Fore.RED+"Please enter valid text");continue
    cmd=text.lower()
    if cmd=="exit":
        print(Fore.BLUE+f"Goodbye Agent {name}!");break
    if cmd =="reset":
        history.clear();print(Fore.CYAN+"History cleared");continue
    if cmd=="history":
        if not history:print(Fore.YELLOW+"No history yet.")
        else:
            print (Fore.CYAN+"Conversation History")
            for i, (t, p, s )in enumerate(history,1):
               col={"Positive":Fore.GREEN,  "Negative":Fore.RED , "Neutral":Fore.YELLOW}[s]
               print(f"[{i}] {col}{t} ({p:.2f}), {s})")
        continue
    polarity= TextBlob(text).sentiment.polarity
    sentiment, color=(
        ("Positive",Fore.GREEN) if polarity >0.05 else
        ("Negative",Fore.RED) if polarity <-0.05 else
        ("Neutral",Fore.YELLOW)
    )
    history.append((text, polarity, sentiment))
    print(f"{color}sentiment: {sentiment} ({polarity:.2f})")   

