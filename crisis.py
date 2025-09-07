from typing import List

CRISIS_KEYWORDS: List[str] = [ 
    "suicidal","suicide", "kill myself", "want to die", "hopeless", "worthless",
    "can't go on", "give up", "ending it all", "no reason to live"
]

SAFETY_MESSAGE = (
    "I'm really sorry to hear this it sounds like you're going through a really tough time. "
    "You're not alone, and there are people who are in the same situation who have overcome this crisis with help of re-assurance and support."
    "Please consider reaching out to a mental health professional or contact a helpline:\n\n"
    "**India:** +91 7893078930 (AASRA), 022 2754 6669 (One Life)\n"
)

def contains_crisis_keywords(text:str) ->bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)