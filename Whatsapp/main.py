from openai import OpenAI
import pyautogui
import time
import pyperclip
client = OpenAI()  # reads key from environment

def is_last_message_from_sender(chat_log, sender_name = "Aayush College"):
    # Split the chat log into individual message
    msg = chat_log.strip().split("/2026] ")[-1]
    
    if sender_name in msg:
        return True
    return False
    

# Click the Whatsapp icon
pyautogui.click(323, 760)
time.sleep(1)
try: 
    while True:
        # Drag from and to position
        pyautogui.moveTo(380, 95)
        pyautogui.dragTo(442, 811, duration=1.0, button='left')

        # Copy the Clipboard
        pyautogui.hotkey('command', 'c')
        time.sleep(2)

        # Deselect the chat in Whatsapp
        pyautogui.click(807, 493)

        #Paste the clipboard
        chat_history = pyperclip.paste()
        print(chat_history)

        if is_last_message_from_sender(chat_history):
            completion = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "system", "content": "You are a person named Ajoy who speaks hindi as well as english. You are from India and you are a coder. You analyze the chat history and respond like Ajoy. Output should be the next chat response (text message only)"},
                {"role": "user", "content": chat_history}
            ]
            )

            response = completion.choices[0].message.content 
            pyperclip.copy(response)

            # Click chat box in whatsapp
            pyautogui.click(866, 805)
            time.sleep(2)

            # Paste the text
            pyautogui.hotkey('command', 'v')
            time.sleep(2)

            # Send the text
            # pyautogui.press('return')
except KeyboardInterrupt:
    print("\nProgram exited using Ctrl + C")
    


            

        