"""Bank of iPhone features used on slides.

Each tip: id, theme, title, body, path.
Keep bodies short (one or two lines on a 1080px slide) and paths exact.
"""

THEMES = {
    "camera": "camera",
    "keyboard": "keyboard",
    "settings": "settings",
    "battery": "battery",
    "privacy": "privacy",
    "messages": "Messages & Photos",
    "productivity": "productivity",
    "safety": "safety",
    "health": "health",
    "accessibility": "accessibility",
}

TIPS = [
    # camera
    ("quicktake", "camera", "Lock video without holding", "In Photo mode, hold the shutter and slide it right to keep recording hands-free.", "Camera › Photo › Hold shutter › Slide right"),
    ("grid-level", "camera", "Camera grid & level", "Turn on the grid and level to keep every shot straight.", "Settings › Camera › Grid / Level"),
    ("volume-shutter", "camera", "Volume button shutter", "Press volume up to snap a photo. Hold it to start a video.", "Camera › Press volume up"),
    ("burst", "camera", "Burst mode", "Slide the shutter to the left to shoot a fast burst of photos.", "Camera › Photo › Slide shutter left"),
    ("mirror-front", "camera", "Mirror your selfies", "Save front-camera photos exactly as you see them in the preview.", "Settings › Camera › Mirror Front Camera"),
    ("preserve-settings", "camera", "Preserve camera settings", "Stop the camera from resetting your mode, filter and exposure every time.", "Settings › Camera › Preserve Settings"),
    ("live-text", "camera", "Copy text from the real world", "Point your camera at any text and tap the Live Text button to copy it.", "Camera › Tap the Live Text icon"),
    ("scan-docs", "camera", "Built-in document scanner", "Scan paper documents into clean PDFs right inside Notes.", "Notes › New note › Paperclip › Scan Documents"),
    ("magnifier", "camera", "Magnifier app", "Turn your iPhone into a magnifying glass with zoom and a flashlight.", "App Library › Magnifier"),
    ("measure", "camera", "Measure anything", "Use your camera as a tape measure for objects, spaces and even people.", "App Library › Measure"),
    ("visual-lookup", "camera", "Identify plants & pets", "Open a photo and tap the sparkle icon to identify plants, pets and landmarks.", "Photos › Open photo › Info (sparkle) icon"),
    # keyboard
    ("trackpad", "keyboard", "Keyboard trackpad", "Hold the space bar to turn your keyboard into a trackpad and move the cursor.", "Any text field › Hold space bar"),
    ("text-replacement", "keyboard", "Text replacement", "Type a short code like \"@@\" and your iPhone expands it into your full email.", "Settings › General › Keyboard › Text Replacement"),
    ("shake-undo", "keyboard", "Shake to undo", "Made a typo or deleted text? Shake your iPhone to undo it.", "Settings › Accessibility › Touch › Shake to Undo"),
    ("one-hand-keyboard", "keyboard", "One-handed keyboard", "Shrink the keyboard to one side for easy one-handed typing.", "Hold the emoji / globe key › Pick left or right"),
    ("calc-delete", "keyboard", "Delete a digit in Calculator", "Swipe left or right on the number to delete the last digit.", "Calculator › Swipe on the display"),
    ("three-finger-undo", "keyboard", "Three-finger undo", "Swipe left with three fingers to undo, right to redo.", "Any app › Three-finger swipe"),
    ("dot-com", "keyboard", "Instant .com", "Hold the period key in a web address field to pick .com, .net, .org and more.", "Safari address bar › Hold the . key"),
    ("double-space", "keyboard", "Double-space period", "Tap the space bar twice to add a period and a space.", "Settings › General › Keyboard › \".\" Shortcut"),
    ("haptic-keyboard", "keyboard", "Haptic keyboard", "Feel a subtle tap on every key press for faster, more confident typing.", "Settings › Sounds & Haptics › Keyboard Feedback"),
    # settings
    ("back-tap", "settings", "Back Tap", "Double- or triple-tap the back of your iPhone to screenshot, open an app and more.", "Settings › Accessibility › Touch › Back Tap"),
    ("tap-top", "settings", "Jump to the top", "Tap the very top of the screen to scroll back to the top of any list.", "Any app › Tap the status bar"),
    ("reduce-white-point", "settings", "Dimmer than minimum", "Make your screen darker than the lowest brightness setting allows.", "Settings › Accessibility › Display & Text Size › Reduce White Point"),
    ("led-flash", "settings", "Flash for alerts", "Make the camera flash blink when you get a call or notification.", "Settings › Accessibility › Audio & Visual › LED Flash for Alerts"),
    ("control-center", "settings", "Custom Control Center", "Add, remove and resize controls exactly the way you like.", "Control Center › Hold empty space › Edit"),
    ("action-button", "settings", "Action button", "Set the Action button to a flashlight, camera, shortcut and more.", "Settings › Action Button"),
    ("lock-screen", "settings", "Lock Screen widgets", "Add weather, battery, calendar and more widgets to your Lock Screen.", "Hold the Lock Screen › Customize"),
    ("lock-apps", "settings", "Lock any app", "Require Face ID to open private apps — or hide them completely.", "Hold an app icon › Require Face ID"),
    ("app-library", "settings", "App Library", "Swipe past your last Home Screen page to find every app sorted for you.", "Home Screen › Swipe left to the end"),
    ("drag-apps", "settings", "Move many apps at once", "Hold one app, start dragging, then tap other apps to stack and move them together.", "Home Screen › Hold app › Tap others"),
    ("home-search", "settings", "Search from anywhere", "Swipe down on any Home Screen to search apps, messages, settings and the web.", "Home Screen › Swipe down"),
    ("dark-icons", "settings", "Dark & tinted app icons", "Switch your app icons to dark or tinted to match your wallpaper.", "Hold Home Screen › Edit › Customize"),
    # battery
    ("charge-limit", "battery", "80% charge limit", "Cap charging at 80% to help your battery age more slowly.", "Settings › Battery › Charging"),
    ("battery-percent", "battery", "Battery percentage", "Show the exact battery percentage right in the status bar.", "Settings › Battery › Battery Percentage"),
    ("low-power", "battery", "Low Power Mode", "Cut background activity and stretch your battery when it's running low.", "Settings › Battery › Low Power Mode"),
    ("battery-health", "battery", "Battery health check", "See your battery's maximum capacity and cycle count in seconds.", "Settings › Battery › Battery Health"),
    ("bg-refresh", "battery", "Background App Refresh", "Stop apps you rarely use from refreshing in the background.", "Settings › General › Background App Refresh"),
    ("auto-lock", "battery", "Shorter Auto-Lock", "Lock your screen sooner to save battery when you put your phone down.", "Settings › Display & Brightness › Auto-Lock"),
    # privacy
    ("stolen-device", "privacy", "Stolen Device Protection", "Adds a Face ID check and a delay before anyone can change key settings.", "Settings › Face ID & Passcode › Stolen Device Protection"),
    ("safety-check", "privacy", "Safety Check", "See and instantly reset who and what has access to your data.", "Settings › Privacy & Security › Safety Check"),
    ("privacy-report", "privacy", "App Privacy Report", "See which apps used your camera, mic and location — and when.", "Settings › Privacy & Security › App Privacy Report"),
    ("hide-my-email", "privacy", "Hide My Email", "Create random email addresses that forward to your real inbox.", "Settings › Your name › iCloud › Hide My Email"),
    ("silence-callers", "privacy", "Silence Unknown Callers", "Send calls from numbers you don't know straight to voicemail.", "Settings › Apps › Phone › Silence Unknown Callers"),
    ("hidden-album", "privacy", "Lock the Hidden album", "Keep your Hidden and Recently Deleted albums behind Face ID.", "Settings › Apps › Photos › Use Face ID"),
    ("passwords-app", "privacy", "Passwords app", "All your saved passwords, passkeys and Wi-Fi codes in one place.", "App Library › Passwords"),
    ("precise-location", "privacy", "Approximate location", "Give apps your general area instead of your exact spot.", "Settings › Privacy & Security › Location Services › App"),
    ("share-wifi", "privacy", "Share Wi-Fi in one tap", "Bring your unlocked iPhone near a friend's to share the Wi-Fi password.", "Unlock iPhone › Hold near friend's iPhone"),
    # messages & photos
    ("send-later", "messages", "Schedule a text", "Write a message now and have it send automatically later.", "Messages › + › Send Later"),
    ("undo-send", "messages", "Edit or unsend texts", "Fix a typo or pull back a message you just sent.", "Messages › Hold message › Edit / Undo Send"),
    ("pin-chats", "messages", "Pin your top chats", "Keep your favorite conversations at the top of Messages.", "Messages › Swipe right on a chat › Pin"),
    ("lift-subject", "messages", "Cut out any subject", "Hold the subject of a photo to lift it off the background and paste it anywhere.", "Photos › Hold the subject"),
    ("duplicates", "messages", "Merge duplicate photos", "Find duplicate photos and merge them to free up storage.", "Photos › Utilities › Duplicates"),
    ("recently-deleted", "messages", "Recover deleted photos", "Deleted photos stay in Recently Deleted for 30 days.", "Photos › Utilities › Recently Deleted"),
    ("namedrop", "messages", "NameDrop", "Hold the top of two iPhones together to swap contact info.", "Unlock iPhone › Hold near another iPhone"),
    ("check-in", "messages", "Check In", "Let a friend know automatically when you've arrived home.", "Messages › + › Check In"),
    # productivity
    ("listen-page", "productivity", "Listen to any web page", "Have Safari read an article out loud while you do something else.", "Safari › Page menu › Listen to Page"),
    ("hide-distracting", "productivity", "Hide distracting items", "Remove pop-ups and clutter from a web page in Safari.", "Safari › Page menu › Hide Distracting Items"),
    ("focus-modes", "productivity", "Focus modes", "Choose which people and apps can reach you while you work, drive or rest.", "Settings › Focus"),
    ("shortcuts-automation", "productivity", "Personal automations", "Make your iPhone do things automatically when you arrive, leave or connect.", "Shortcuts › Automation › New Automation"),
    ("universal-clipboard", "productivity", "Copy on iPhone, paste on Mac", "Copy anything on your iPhone and paste it straight on your Mac or iPad.", "Settings › General › AirPlay & Continuity › Handoff"),
    ("translate", "productivity", "Live conversation translate", "Talk with someone in another language and see both sides translated.", "Translate › Conversation"),
    ("math-notes", "productivity", "Math in Notes", "Type an equation with \"=\" in Notes and get the answer instantly.", "Notes › Type 24*18="),
    ("unit-convert", "productivity", "Calculator converter", "Convert currency, length, weight and more right in Calculator.", "Calculator › Calculator icon › Convert"),
    ("live-voicemail", "productivity", "Live Voicemail", "Read a live transcript while someone leaves you a voicemail.", "Settings › Apps › Phone › Live Voicemail"),
    ("offline-maps", "productivity", "Offline maps", "Download a map area and get directions without signal.", "Maps › Profile › Offline Maps"),
    # safety
    ("emergency-sos", "safety", "Emergency SOS", "Hold the side button and a volume button to call emergency services fast.", "Settings › Emergency SOS"),
    ("crash-detection", "safety", "Crash Detection", "Your iPhone can detect a severe car crash and call for help.", "Settings › Emergency SOS › Call After Severe Crash"),
    ("find-my-offline", "safety", "Find My, even offline", "Find your iPhone even when it's off or offline.", "Settings › Your name › Find My › Find My iPhone"),
    ("medical-id", "safety", "Medical ID on Lock Screen", "First responders can see your allergies and emergency contacts without unlocking your phone.", "Health › Profile › Medical ID › Show When Locked"),
    # health
    ("screen-distance", "health", "Screen Distance", "Your iPhone can warn you when you hold it closer than 12 in (30 cm) to your eyes.", "Settings › Screen Time › Screen Distance"),
    ("walking-steadiness", "health", "Walking Steadiness", "Just by carrying your iPhone, it can track how steady you walk.", "Health › Browse › Mobility › Walking Steadiness"),
    ("loud-audio", "health", "Reduce Loud Audio", "Automatically lowers headphone volume above a level you choose.", "Settings › Sounds & Haptics › Headphone Safety"),
    ("motion-cues", "health", "Vehicle Motion Cues", "Moving dots on screen reduce motion sickness when you use your phone in a car.", "Settings › Accessibility › Motion › Vehicle Motion Cues"),
    ("background-sounds", "health", "Background Sounds", "Built-in rain, ocean and stream sounds to help you focus or relax.", "Settings › Accessibility › Audio & Visual › Background Sounds"),
    ("medications", "health", "Medication reminders", "Log your meds and vitamins and get reminders in the Health app.", "Health › Browse › Medications"),
    ("sleep-schedule", "health", "Sleep schedule", "Set a bedtime and wake-up time and let your iPhone wind down with you.", "Health › Browse › Sleep › Full Schedule"),
    ("night-shift", "health", "Night Shift", "Shift your screen to warmer colors after sunset automatically.", "Settings › Display & Brightness › Night Shift"),
    # accessibility
    ("sound-recognition", "accessibility", "Sound Recognition", "Get alerts when your iPhone hears a doorbell, a baby crying or a fire alarm.", "Settings › Accessibility › Sound Recognition"),
    ("eye-tracking", "accessibility", "Control with your eyes", "Navigate your iPhone using just your eyes and the front camera.", "Settings › Accessibility › Eye Tracking"),
    ("live-listen", "accessibility", "Live Listen", "Use your iPhone as a remote mic that streams sound to your AirPods.", "Control Center › Hearing › Live Listen"),
    ("bold-text", "accessibility", "Bigger, bolder text", "Make text easier to read across every app.", "Settings › Display & Brightness › Text Size / Bold Text"),
    ("assistive-access", "accessibility", "Simplified iPhone", "Give your parents a simpler iPhone with big buttons and only the apps they need.", "Settings › Accessibility › Assistive Access"),
    ("voice-isolation", "accessibility", "Voice Isolation", "Block background noise on calls so people hear only your voice.", "Control Center (during a call) › Mic Mode"),
]

TIP_BY_ID = {t[0]: t for t in TIPS}
