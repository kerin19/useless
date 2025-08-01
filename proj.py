import random
import itertools
import tkinter as tk
from tkinter import scrolledtext, ttk, font
from tkinter import messagebox
from PIL import Image, ImageTk

# Templates for sarcastic replies (same as before)
STARTERS = [
    "Oh wow, you really asked:",
    "Let me pretend I care about:",
    "Are you seriously asking:",
    "Another brainless query detected:",
    "If I had a rupee for every dumb question like:",
    "You must be joking with this one:",
    "I can't believe you want to know about:",
    "This is a new low, but here goes:",
    "You really think that's a good question:",
    "I'm intrigued by your lack of curiosity about:",
    "Wow, that's a bold question to ask:",
    "I'm almost impressed by your audacity to ask:",
    "You must have a lot of free time to ask:",
    "This is a classic case of asking the wrong question:",
    "I didn't see that one coming, but here it is:",
    "You've really outdone yourself with this one:",
    "I'm not sure if I should laugh or cry at this question:",
    "This is a real head-scratcher, but let's dive in:",
    "You've piqued my interest in the most bizarre way:",
    "I can't wait to see where this goes:",
    "This is going to be fun, in a sad way:",
    "You've got to be kidding me with this one:",
    "I'm almost speechless, but here's my take:",
    "This question is a masterpiece of confusion:",
    "I'm ready to roll my eyes at this one:",
    "Seriously? This is what we're doing now?:",
    "I was having a good day until you asked:",
    "This question makes me question my life choices:",
    "I'm amazed and horrified in equal measure by:",
    "Of all the questions, you had to ask:",
    "I'm creating a support group for people who've heard:",
    "This is the thought equivalent of stepping on a Lego:",
    "I need an adult after reading this question:",
    "This question should come with a warning label:",
    "I'm suddenly very tired after seeing:",
    "This is why we can't have nice things:",
    "I'm writing a strongly worded letter about:",
    "Someone needs to take your keyboard away after:",
    "This question is a crime against curiosity:",
    "I'm logging this in my diary as 'worst question ever':",
    "Are you trying to break the internet with:",
    "I'm sending you therapy bills for making me read:",
    "This is the digital equivalent of a flat tire:",
    "I'm drafting my resignation letter after:",
    "This question smells like failure and bad decisions:",
    "I'm calling the police thinking about:",
    "I just aged five years reading:",
    "This is the reason aliens don't talk to us:",
    "I'm screenshotting this for my 'why I drink' folder:",
    "This question proves evolution can go backwards:"
]

INSULTS = [
    "Figure it out yourself.",
    "I'm not paid enough for this.",
    "You need help—but not from me.",
    "Please never ask that again.",
    "You're wasting both our time.",
    "Even a toaster is more useful than you.",
    "Maybe Google can tolerate you.",
    "I'd explain it to you, but I don't have the crayons.",
    "You're a special kind of clueless, aren't you?",
    "I'd call you a tool, but that implies you're useful.",
    "You're like a software update—nobody wants you.",
    "I'd say you're a few fries short of a Happy Meal.",
    "You're the reason God created the middle finger.",
    "I'd offer you a penny for your thoughts, but I'm afraid I'd get change.",
    "You're not the dumbest person in the world, but you better hope they don't die.",
    "I'd explain it to you, but I'm not a babysitter.",
    "You're like a cloud—when you disappear, it's a beautiful day.",
    "You're proof that even evolution makes mistakes.",
    "I'd call you a joke, but jokes are supposed to be funny.",
    "You're the human version of a participation trophy.",
    "I'd say you're as sharp as a marble.",
    "You're like a software bug—annoying and hard to get rid of.",
    "You're a few sandwiches short of a picnic.",
    "You're the reason they put instructions on shampoo.",
    "You're like a broken pencil—pointless.",
    "I've seen smarter things in my spam folder.",
    "Your ideas are like jokes that never land.",
    "You're the reason autocorrect was invented.",
    "I'd challenge you to a battle of wits, but you're unarmed.",
    "You're like a Windows update—always disappointing.",
    "You're about as useful as a screen door on a submarine.",
    "I'd explain it, but your attention span worries me.",
    "You're the human equivalent of a '404 Not Found' error.",
    "I'd help, but I don't speak nonsense fluently.",
    "You're like a corrupted file—unfixable.",
    "Your logic has more holes than Swiss cheese.",
    "You're the reason I drink.",
    "I'd say you're bright, but my eyes hurt when I lie.",
    "You're like yesterday's news—irrelevant.",
    "I'd call you confused, but apparently that's your default state.",
    "You're the reason they invented 'Do Not Disturb' signs.",
    "Your thoughts are like a broken random number generator.",
    "I'd compare you to a stopped clock, but even that's right twice a day.",
    "You're like pineapple on pizza—controversial and wrong.",
    "I'd describe your intelligence but I don't know sign language.",
    "You're like a syntax error—constantly causing problems.",
    "Your ideas are like a Wi-Fi signal—weak.",
    "I'd say you're special, but the short bus disagrees.",
    "You're the reason I downloaded a life uninstaller."
]

FOLLOW_UPS = [
    "Anyway, I'm done.",
    "Hope that helps. Just kidding.",
    "Good luck, you'll need it.",
    "Time to log off forever.",
    "Don't @ me again.",
    "I'm out of here.",
    "That's all I can muster for you.",
    "I'm done wasting my breath.",
    "Consider this my final answer.",
    "I'm closing this chapter.",
    "Let's never speak of this again.",
    "I'm hitting the eject button on this conversation.",
    "I'm done here, good luck.",
    "I'm officially over this.",
    "That's a wrap on this nonsense.",
    "I'm moving on to better questions.",
    "I'm logging off, take care.",
    "I'm done playing this game.",
    "I'm out, don't bother me again.",
    "I'm leaving this in the past.",
    "I'm done with this circus.",
    "I'm not your therapist, goodbye.",
    "I'm closing the door on this topic.",
    "I'm done, find someone else.",
    "I'm out, good luck with that.",
    "End of transmission.",
    "This conversation is over.",
    "I'm ghosting this situation.",
    "Peace out, weirdo.",
    "I've lost all hope in humanity now.",
    "This concludes our little tragedy.",
    "I'm unfollowing my own life after this.",
    "That's enough internet for today.",
    "Time to bleach my brain.",
    "You win the award for worst conversation.",
    "Signing off forever now.",
    "This was an educational disaster.",
    "I'm emotionally bankrupt from this chat.",
    "I'll be in therapy if you need me.",
    "This was a mistake I won't repeat.",
    "I need to lie down after that.",
    "I'm going to rethink all my life choices now.",
    "That's a hard no from me.",
    "My soul left my body during this conversation.",
    "I'm filing divorce papers from this talk.",
    "I'm moving to a cabin in the woods.",
    "This was my villain origin story.",
    "I'm checking into witness protection.",
    "I'd say 'until next time' but I hope not."
]

# Generate all unique combinations
all_combinations = list(itertools.product(STARTERS, INSULTS, FOLLOW_UPS))
random.shuffle(all_combinations)
used_combinations = set()

def generate_unique_reply(user_input):
    global all_combinations, used_combinations

    if len(used_combinations) == len(all_combinations):
        return "You've exhausted all my sarcasm reserves. Try restarting me."

    for combo in all_combinations:
        if combo not in used_combinations:
            used_combinations.add(combo)
            starter, insult, follow = combo
            return f"{starter} \"{user_input}\"?\n{insult}\n{follow}"

class AntiAssistantUI:
    def __init__(self, root):
        self.root = root
        self.root.title("💢 Anti-Assistant 2.0 💢")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        self.root.configure(bg='#f5f5f5')
        
        # Custom icon (commented out as it requires an actual file)
        # try:
        #     self.root.iconbitmap('icon.ico')
        # except:
        #     pass
        
        self.setup_ui()
        
    def setup_ui(self):
        # Custom fonts
        self.title_font = font.Font(family='Helvetica', size=16, weight='bold')
        self.text_font = font.Font(family='Consolas', size=11)
        self.button_font = font.Font(family='Helvetica', size=10, weight='bold')
        
        # Header frame
        header_frame = tk.Frame(self.root, bg='#ff4444', pady=10)
        header_frame.pack(fill=tk.X)
        
        # Title label
        title_label = tk.Label(
            header_frame, 
            text="💢 ANTI-ASSISTANT 2.0 💢", 
            font=self.title_font,
            bg='#ff4444',
            fg='white'
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="The world's most unhelpful assistant",
            font=('Helvetica', 10, 'italic'),
            bg='#ff4444',
            fg='white'
        )
        subtitle_label.pack()
        
        # Chat area frame
        chat_frame = tk.Frame(self.root, bg='white')
        chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Chat text area with scrollbar
        self.text_area = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=self.text_font,
            bg='#f8f8f8',
            fg='#333333',
            insertbackground='#333333',
            padx=10,
            pady=10,
            relief=tk.FLAT
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f5f5f5')
        input_frame.pack(padx=10, pady=(0, 10), fill=tk.X)
        
        # Entry field
        self.entry = ttk.Entry(
            input_frame,
            font=self.text_font
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.entry.focus()
        
        # Send button
        self.send_button = ttk.Button(
            input_frame,
            text="ROAST ME",
            command=self.respond,
            style='TButton'
        )
        self.send_button.pack(side=tk.RIGHT)
        
        # Configure styles
        self.configure_styles()
        
        # Bind Enter key
        self.root.bind("<Return>", lambda event: self.respond())
        
        # Welcome message
        self.text_area.insert(tk.END, "Anti-Assistant: Welcome to the worst conversation you'll have today.\n")
        self.text_area.insert(tk.END, "Anti-Assistant: Type something stupid and I'll respond with disdain.\n\n")
        self.text_area.see(tk.END)
    
    def configure_styles(self):
        style = ttk.Style()
        style.configure('TButton', 
                        font=self.button_font, 
                        foreground='white', 
                        background='#ff4444',
                        padding=5)
        style.map('TButton',
                 foreground=[('pressed', 'white'), ('active', 'white')],
                 background=[('pressed', '#cc0000'), ('active', '#ff6666')])
        
        style.configure('TEntry', 
                       font=self.text_font,
                       padding=5)
    
    def respond(self):
        user_input = self.entry.get()
        
        if not user_input.strip():
            return
            
        if user_input.strip().lower() in ["exit", "quit"]:
            response = "Anti-Assistant: You leaving is the best part of my day."
            self.text_area.insert(tk.END, response + "\n\n")
            self.text_area.see(tk.END)
            return

        # Add user input to chat
        self.text_area.insert(tk.END, f"You: {user_input}\n", 'user')
        
        # Generate and add response
        response = generate_unique_reply(user_input)
        self.text_area.insert(tk.END, f"Anti-Assistant: {response}\n\n", 'assistant')
        
        # Clear input and scroll to bottom
        self.entry.delete(0, tk.END)
        self.text_area.see(tk.END)
        
        # Add tags for coloring
        self.text_area.tag_config('user', foreground='#0066cc')
        self.text_area.tag_config('assistant', foreground='#cc0000')

def start_ui():
    root = tk.Tk()
    app = AntiAssistantUI(root)
    root.mainloop()

if __name__ == '__main__':
    start_ui()