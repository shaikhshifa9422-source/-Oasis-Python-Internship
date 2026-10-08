# Oasis Infobyte - Task 3 - Basic Voice Assistant
# ID: OIB/O2/IP3914 - Shifa Shaikh

import datetime

print("Hello! I am your Voice Assistant")
print("Commands: time, date, hello, bye")

while True:
    command = input("You: ").lower()
    
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Assistant: Current time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"Assistant: Today's date is {date}")
    elif "hello" in command:
        print("Assistant: Hello Shifa! How can I help you?")
    elif "bye" in command:
        print("Assistant: Goodbye! Have a great day!")
        break
    else:
        print("Assistant: Sorry, I didn't understand. Try time/date/hello/bye")