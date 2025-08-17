# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform left:
    xalign 0.25
    yalign 0.0

transform right:
    xalign 0.75
    yalign 0.0

transform centre:
    xalign 0.5
    yalign 0

define j = Character("January")
define f = Character("Finn")
define t = Character("Teacher")

label start:

    scene special scene 1

    j "{i}I was just sitting in class doing my work, when a friend of mine I hadn’t seen in a while came and sat on the desk beside me.{/i}"

    scene special scene 2

    j "{i}It was weird, to say the least. It had been about 2 weeks since I last heard from him, and here he was all of a sudden, sitting beside me quite rudely on a desk, not even acknowledging my presence.{/i}"
    j "Oh, you’re back. Hi."

    scene special scene 3

    j "{i}He looked at me, a distant look in his eyes, like he heard me but couldn’t quite recognize his own name.{/i}"
    j "Were you sick? It’s been so long."
    j "{i}He blinked at me like I was the one acting weird and whipped his head around as if it wasn’t me that was talking to him.{/i}"
    f "Me? What?"
    j "{i}He almost looked horrified… or shocked? I thought maybe I said something wrong.{/i}"
    f "Are you talking to me? Wait. Wh… Huh?"
    j "{i}I guessed something happened when he was gone, more than just being sick. The look on his face and his change in mannerisms since I last saw him was weird, even for him.{/i}"

    scene classroom dialogue background

    show january worried

    j "Finn, are you feeling okay–"

    show january worried at left
    show finn shocked at right

    f "Can you see me? You’re talking to me?"

    hide finn shocked
    show january neutral at centre

    j "{i}I thought maybe he had a fever. I couldn’t think of any other explanation for a question so out there after having disappeared from school for a couple weeks. Fevers do weird things to people right?{/i}"

    show january worried at centre
    
    j "Of course. Are you feeling alright?"

    show january worried at left
    show finn desparate at right

    f "What the hell? Is this some kind of joke?"

    show january concerned at left

    j "Sorry, I’m just worried about you, I mean–"

    hide january concerned
    hide finn desparate
    show teacher stern

    t "January!"

    hide teacher stern
    show january awkward

    j "{i}The teacher interrupted me before I could continue; scolding me for talking during class.{/i}"
    j "{i}I looked around the room and found most of the class staring at me, whispering to one another.{/i}"

    show january worried

    j "Sorry."

    j "{i}This was too weird to ignore. I spoke to Finn in a whisper instead, hoping the teacher wouldn’t hear.{/i}"

    show january worried at left
    show finn neutral at right

    j "Is it okay if I check your temperature? Just with the back of my hand..."

    hide finn neutral

    j "{i}I forgot what I was saying when I watched him hop off the desk. I thought he was finally just going to sit down normally.{/i}"
    j "{i}Not even close.{/i}"
    
    show january shocked

    j "What… What are you doing? Finn?"
    j "{i}I watched as he climbed… really clumsily… on top of the desk.{/i}"

    show january shocked at left
    show finn clapping his hands at right

    j "{i}Nothing made any sense at the time. I asked him what was wrong, and he got angry… Or confused?... Angrily confused?{/i}"
    j "{i}And then next thing I knew he was up on the desk clapping his hands like there were no consequences to his actions.{/i}"

    hide finn clapping his hands
    show january shocked at centre

    j "What are you doing?!"

    hide january shocked
    show teacher stern

    t "January, do you need to step outside?"

    hide teacher stern
    show january stern

    j "{i}I don’t even know. I looked up at him, the best way to describe how I felt was also just angrily confused.{/i}"
    j "{i}Finn knew how much I enjoy this class, knew I hated getting into any kind of conflict. Yet, he was being disruptive and I was the one in trouble for it.{/i}"

    hide january stern
    show finn stern

    f "You do. I want you to tell me what the hell is going on, come outside."

    show finn stern at right
    show january stern at left

    j "I don’t know ‘what the hell is going on’. What are you doing?"

    hide january stern
    hide finn stern
    show teacher neutral

    t "January."

    hide teacher neutral
    show january awkward

    j "Yeah. Um. Please excuse us. I’m sorry."

    scene outside classroom dialogue background
    hide january awkward
    show january concerned

    j "I’m confused."

    show january concerned at left
    show finn awkward at right

    f "Sorry… Yeah… This all sounds insane, doesn’t it? Also sorry for getting you in trouble, I just really needed to like… confirm this is happening? I still can’t believe it."
    f "That you could see me, that is…"
    f "I’m not really thinking right now, it’s been like 2 weeks or something since… I just– God"
    f "I really don’t know what’s going on."
    j "{i}I don’t think I’ve ever seen Finn like this before, so… emotional? We haven't known each other for long, but he never seemed like the type to just break down in front of people like this. Respectfully.{/i}"
    j "{i}This is really all unbelievable. Something happened, he doesn’t know what, and now he’s like… invisible? But I can see him.{/i}"
    j "{i}That stuff’s not even physically possible, right? Nothing makes sense. Maybe I’m seeing things.{/i}"
    j "{i}Maybe I’m imagining all this. Maybe I’m the one with the fever or something.{/i}"
    j "{i}Or maybe I’m still sleeping.{/i}"
    j "{i}That would make more sense.{/i}"

    hide finn awkward
    show finn concerned at right

    f "January? You good? Look, I’m sorry. This is a lot. I wish I could tell you what’s going on."

    hide january concerned
    show january awkward at left

    j "I think I need to go to the sick bay."

    hide finn concerned
    show finn desparate at right

    f "January! I’m real, I’m here! I’m sorry, I know it’s confusing, I’m confused too. I’m really here though, please, I don’t want to be alone again."
    j "{i}Alone again…{/i}"
    j "{i}I know how that feels.{/i}"

    hide january awkward
    show january worried at left

    j "Are you, uh, sure you’re invisible?"

    show finn stern at right

    f "January, I’m pretty sure I’m invisible. Pretty sure I have been for the past however long it’s been."

    show january awkward at left

    j "..."

    show finn awkward at right

    f "Alright yeah that’s understandable, I’d probably look at you the exact same way if you told me all this crap after disappearing for ages."

    show finn concerned at right

    f "Do you believe I’m really here?"

    show january neutral at left

    j "{i}I do. It’d be hard to believe that he’s not really standing here right in front of me. This is really scarily real.{/i}"
    j "Can you do that again? Clap or… Try and draw some attention to yourself, I mean."

    show finn neutral at right

    f "Yeah, whatever, if that helps. Open the door for me."

    hide finn neutral
    hide january neutral

    "I reached for the door knob but before I could grab a hold of it the door flung open… Hitting Finn in the face…"

    show january shocked

    j "Oh my God!"

    show january shocked at left
    show teacher neutral at right

    t "January, is everything alright? You should come back in soon, the bell will go off in a couple minutes."
    j "I’m fine, but what about Finn!?"
    t "What about Finn?"

    hide teacher neutral
    hide january shocked
    show finn awkward

    f "I'm good..."

    hide finn awkward
    show teacher neutral

    t "Oh. Right, yes. I apologise, I know you were good friends, but at this time we’ve been asked to keep everything confidential. He’ll be okay though."
    j "{i}Yeah, he sure sounds 'okay'{/i}"
    j "{i}Wait, what?{/i}"
    "Finn and I shared a terrified look."

    show teacher neutral at right
    show january worried at left

    j "I'll be there in a minute..."
    "I waited until the teacher left and was fully out of view before I turned back to Finn."

    hide teacher neutral
    show january awkward

    j "Um."

    show january awkward at left
    show finn stern at right

    f "Concerning, yeah. Just grab your stuff, we’ll talk soon."

    show january worried at left

    j "Wait, where are you doing?"
    f "Nowhere. It’s not like I can open doors anymore. I’ll wait outside for you."

    show finn neutral at right

    f "See you soon."

    # This ends the game.

    return
