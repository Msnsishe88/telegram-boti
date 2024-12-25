import telebot
from datetime import datetime
import time
import random
import os

# تعديل مهم: استخدام متغير البيئة للتوكن
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    welcome_msg = f"""هلا وغلا {name} 🌹
أنا حمد، بوت عراقي سوري جاهز لخدمتك 🇮🇶 🇸🇾

شوف هاي الأوامر يا غالي:
/start - القائمة الرئيسية
/help - المساعدة
/time - الوقت
/joke - نكتة
/games - الألعاب
/hello - دردشة
/music - موسيقى
/share - مشاركة البوت"""
    bot.reply_to(message, welcome_msg)

@bot.message_handler(commands=['help'])
def help(message):
    help_text = """شو في عندك حبيبي؟ 🌹

• سولف معي عادي
• اكتب "حمد" وأنا جاهز
• العب معي ألعاب /games 
• اسمع موسيقى /music
• اضحك مع نكتة /joke

وإذا بدك شي بس احكي 💚"""
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['games'])
def games(message):
    games_text = """يلا نلعب! اختار لعبة:

🎲 /dice - زهر
🎯 /target - تصويب
⚽️ /football - كرة قدم
🎳 /bowling - بولينغ
🎰 /slots - سلوتس
🎮 /guess - خمن الرقم"""
    bot.reply_to(message, games_text)

@bot.message_handler(commands=['guess'])
def guess_game(message):
    number = random.randint(1, 10)
    msg = bot.reply_to(message, "خمن رقم من 1 لـ 10 🤔")
    bot.register_next_step_handler(msg, check_number, number)

def check_number(message, correct_number):
    try:
        guess = int(message.text)
        if guess == correct_number:
            bot.reply_to(message, "صح عليك! 🎉")
        else:
            bot.reply_to(message, f"للأسف غلط، الرقم كان {correct_number} 😅")
    except:
        bot.reply_to(message, "لازم تدخل رقم! جرب مرة ثانية /guess")

@bot.message_handler(commands=['dice', 'target', 'football', 'bowling', 'slots'])
def send_game(message):
    game_dict = {
        'dice': '🎲',
        'target': '🎯',
        'football': '⚽️',
        'bowling': '🎳',
        'slots': '🎰'
    }
    command = message.text[1:]
    if command in game_dict:
        bot.send_dice(message.chat.id, emoji=game_dict[command])

@bot.message_handler(commands=['music'])
def music(message):
    music_text = """شو بتحب تسمع؟ 🎵

🎸 /pop - بوب
🎺 /classical - كلاسيك
🪘 /arabic - طرب
🎼 /modern - حديث"""
    bot.reply_to(message, music_text)

@bot.message_handler(commands=['joke'])
def tell_joke(message):
    jokes = [
        "واحد سوري سأل عراقي: شو اسم أمك؟ قله: يمه 😂",
        "ليش العراقي حط ساعته بالفريزر؟ يريد يجمد الوقت 🕐",
        "واحد سوري راح للدكتور قله: عم اسمع أصوات براسي، قله: بكرا بنركبلك ويندوز جديد 💻",
        "ليش القطار زعلان؟ لأنه ما عندو صحاب، كل ما يشوف واحد يمشي 🚂",
        "مرة أسد عم يركض ورا أرنب، ليش؟ بدو يعمل ستوري 📸",
        "ليش البطريق دايماً مبسوط؟ لأنه عايش في سلام مع نفسه 🐧"
    ]
    bot.reply_to(message, f"خوش نكتة:\n{random.choice(jokes)}")

@bot.message_handler(commands=['time'])
def show_time(message):
    current_time = datetime.now().strftime("%I:%M %p")
    bot.reply_to(message, f"هسه الساعة {current_time} 🕐")

@bot.message_handler(commands=['share'])
def share(message):
    share_text = """شارك البوت مع أصدقائك 💚
t.me/[اسم_البوت_الخاص_بك]

خليهم يستمتعون معنا! 🌟"""
    bot.reply_to(message, share_text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg_text = message.text.lower()
    
    if "حمد" in msg_text:
        responses = [
            "لبيه عيوني 💚",
            "موجود حبيبي 🌹",
            "تدلل يا غالي ✨",
            "تحت أمرك 🌺"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif any(word in msg_text for word in ["شلونك", "كيفك", "شخبارك"]):
        responses = [
            "الحمدلله تمام، انت شلونك عيوني؟ 🌹",
            "بخير دام انت بخير، شو أخبارك؟ 💚",
            "منيح والله، كيفك انت يا قمر؟ ✨"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif "احبك" in msg_text:
        responses = [
            "وأنا أكثر والله 💚",
            "تسلملي يا غالي 🌹",
            "وأنا كمان بحبك كتير 💕"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif any(word in msg_text for word in ["باي", "مع السلامة"]):
        responses = [
            "الله معك حبيبي 🌹",
            "مع السلامة يا قمر 💚",
            "تعال بكرا نشوفك 🌺"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif "صباح" in msg_text:
        responses = [
            "صباح النور والسرور 🌞",
            "صباح الورد يا عسل 🌹",
            "يا صباح الخير والبركة ✨"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif "مساء" in msg_text:
        responses = [
            "مساء الخير والسعادة 🌙",
            "مساء النور يا نور 💫",
            "مساء الورد حبيبي 🌹"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif any(word in msg_text for word in ["شكرا", "تسلم"]):
        responses = [
            "العفو حبيبي 🌹",
            "من ذوقك يا غالي 💚",
            "تدلل عيوني ✨"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif "السلام عليكم" in msg_text:
        responses = [
            "وعليكم السلام والرحمة 🌹",
            "هلا وغلا بالغالي 💚",
            "وعليكم السلام، نورتنا ✨"
        ]
        bot.reply_to(message, random.choice(responses))
    
    else:
        responses = [
            "آمر حبيبي، شو بدك؟ 🌹",
            "موجود للخدمة 💚",
            "تفضل عيوني ✨",
            "احكيلي شو في؟ 🌺"
        ]
        bot.reply_to(message, random.choice(responses))

bot.infinity_polling(timeout=20, long_polling_timeout=20)
