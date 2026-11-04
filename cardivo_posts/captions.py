"""Caption builder.

Rules:
- English, written around what US users search on TikTok
  ("iphone hacks", "iphone tips and tricks", "hidden iphone features", ...).
- Always explains how to download Cardivo.
- Always lists a few hidden iPhone tricks in plain text.
- Never mentions anything health-related (checked by BANNED_WORDS).
"""
import random
import re

HOOKS = [
    "iPhone hacks you'll actually use every day 👀",
    "Hidden iPhone features nobody talks about 🤫",
    "iPhone tips and tricks I wish I knew sooner 📱",
    "Things your iPhone can do that you didn't know about ✨",
    "iPhone settings you need to change right now ⚙️",
    "The iPhone tricks Apple doesn't tell you about 👀",
    "Save this before you forget these iPhone hacks 📌",
    "Your iPhone is way smarter than you think 🧠",
    "iPhone features you've been sleeping on 😳",
    "If you have an iPhone, you need to know these 👇",
    "POV: you finally learn the hidden iPhone features 😮",
    "Best iPhone tricks of 2026 — part {n} 🔥",
    "iPhone hacks that feel illegal to know 😅",
    "Stop scrolling — these iPhone tips are worth it 🛑",
    "iOS tips every iPhone user should know 📲",
    "Underrated iPhone features you'll use daily 💡",
    "Little-known iPhone tricks that save you time ⏱️",
    "Turn these on and thank me later 🙌",
    "iPhone tips your friends don't know yet 🤭",
    "How to use your iPhone like a pro 😎",
    "Cool iPhone tricks to try tonight 🌙",
    "Secret iPhone features hiding in Settings 🔍",
]

SUB_HOOKS = [
    "Save this and try them today.",
    "Send this to someone who still doesn't know.",
    "Which one did you not know? Tell me below 👇",
    "Follow for a new iPhone trick every day.",
    "Swipe through and save it for later.",
    "Tag a friend who needs this.",
    "Comment the number you're turning on first.",
    "Part {n} of our daily iPhone tips series.",
]

TRICK_INTROS = [
    "More hidden iPhone tricks:",
    "Bonus iPhone hacks:",
    "A few more iPhone tips:",
    "Extra tricks to try:",
    "More things your iPhone can do:",
]

# Plain-text tricks for the caption. Must stay health-free.
CAPTION_TRICKS = [
    "Back Tap: double-tap the back of your iPhone to take a screenshot",
    "Hold the space bar to turn your keyboard into a trackpad",
    "Swipe on the Calculator display to delete the last digit",
    "Tap the top of the screen to jump back to the top",
    "Hold a photo's subject to lift it off the background",
    "Swipe down on the Home Screen to search anything",
    "Shake your iPhone to undo typing",
    "Swipe left with three fingers to undo, right to redo",
    "Hold the period key in Safari for .com, .net and .org",
    "Schedule a text with Send Later in Messages",
    "Edit or unsend an iMessage by holding it",
    "Press volume up to take a photo, hold it for video",
    "Point your camera at text and copy it with Live Text",
    "Scan documents straight into Notes",
    "Type an equation with = in Notes for instant answers",
    "Convert currency right inside the Calculator",
    "Lock any app with Face ID by holding its icon",
    "Pin your favorite chats at the top of Messages",
    "Share your Wi-Fi password by holding iPhones close",
    "Swap contacts with NameDrop by holding two iPhones together",
    "Show your battery percentage in the status bar",
    "Download offline maps before a trip",
    "Use Text Replacement to type your email in two keystrokes",
    "Silence calls from unknown numbers",
    "Make the camera flash blink for notifications",
    "Turn on a camera grid and level for straighter photos",
    "Merge duplicate photos to free up storage",
    "Have Safari read any article out loud",
    "Move many apps at once by tapping them while dragging",
    "Recover deleted photos from Recently Deleted",
]

CTA_TITLES = [
    "How to get Cardivo 📲",
    "Want Cardivo? Here's how 👇",
    "Get Cardivo in 3 steps:",
    "Download Cardivo:",
    "How to download Cardivo on iPhone:",
]

CTA_STEPS = [
    ["Open the App Store on your iPhone", 'Search "Cardivo"', "Tap Get — it's free to download"],
    ['Open the App Store', 'Type "Cardivo" in the search bar', "Tap Get and open the app"],
    ['Go to the App Store', 'Search for "Cardivo"', "Hit Get — free download"],
    ["Open App Store", 'Search "Cardivo app"', "Tap the blue Get button"],
]

CORE_TAGS = ["#iphonetricks", "#iphonetips", "#iphonehacks"]
ROTATING_TAGS = [
    "#ios", "#iphone", "#techtok", "#apple", "#iphonefeatures", "#iphonesettings",
    "#techtips", "#lifehacks", "#appletips", "#iphonetipsandtricks", "#hiddenfeatures",
    "#iphone17", "#iphone16", "#iphone15", "#ios26", "#techhacks", "#smartphonetips",
    "#fyp", "#foryou", "#learnontiktok",
]

BANNED_WORDS = [
    "health", "heart", "pulse", "bpm", "medical", "medication", "meds", "sleep",
    "hearing", "fitness", "wellness", "workout", "blood", "doctor", "symptom",
    "stress", "anxiety", "calorie", "cardio", "ecg", "breath",
]


def _check(text: str) -> None:
    low = text.lower()
    for w in BANNED_WORDS:
        if re.search(rf"\b{re.escape(w)}\b", low):
            raise ValueError(f"caption contains banned word: {w}")


def build_caption(rng: random.Random, part_no: int) -> str:
    hook = rng.choice(HOOKS).format(n=part_no)
    sub = rng.choice(SUB_HOOKS).format(n=part_no)
    tricks = rng.sample(CAPTION_TRICKS, rng.randint(4, 6))
    cta_title = rng.choice(CTA_TITLES)
    steps = rng.choice(CTA_STEPS)
    tags = CORE_TAGS + rng.sample(ROTATING_TAGS, rng.randint(3, 5)) + ["#cardivo"]
    rng.shuffle(tags)

    lines = [hook, sub, "", rng.choice(TRICK_INTROS)]
    lines += [f"• {t}" for t in tricks]
    lines += ["", cta_title]
    lines += [f"{i}. {s}" for i, s in enumerate(steps, 1)]
    lines += ["", " ".join(tags)]
    text = "\n".join(lines)
    _check(text)
    return text
