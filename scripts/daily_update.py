
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

# =====================================================
# CONFIGURATION
# =====================================================

TIMEZONE = ZoneInfo("Africa/Nairobi")
README_PATH = Path("README.md")

START_MARKER = "<!-- DAILY-START -->"
END_MARKER = "<!-- DAILY-END -->"

# =====================================================
# DAILY THEMES AND QUOTES
# Original quotes written for this profile.
# Multiple quotes per day allow weekly rotation.
# =====================================================

DAILY_DATA = {
    0: {
        "theme": "FOCUS",
        "mood": "STRATEGIC EXECUTION",
        "quotes": [
            "The week does not reward those who announce their intentions, but those who quietly turn them into systems.",
            "A thousand possibilities mean nothing without the discipline to pursue one.",
            "Clarity is the architecture of execution. Know the objective before making the move.",
            "The strongest beginnings are often quiet. Let the results introduce the ambition.",
        ],
    },

    1: {
        "theme": "DISCIPLINE",
        "mood": "CONSISTENCY OVER COMFORT",
        "quotes": [
            "Talent opens doors. Discipline determines how long you remain in the room.",
            "A system becomes powerful when consistency no longer requires motivation.",
            "The difference between intention and achievement is often an ordinary decision repeated.",
            "Do not negotiate with the standards you established when your vision was clear.",
        ],
    },

    2: {
        "theme": "PRECISION",
        "mood": "DEEP ENGINEERING",
        "quotes": [
            "Complexity is easy to create. Elegance requires understanding.",
            "The engineer who understands the smallest detail can influence the largest system.",
            "Precision is not doing more. It is removing everything that does not belong.",
            "Before optimizing the machine, understand what the machine is supposed to achieve.",
        ],
    },

    3: {
        "theme": "INNOVATION",
        "mood": "EXPERIMENTATION",
        "quotes": [
            "Every limitation is an invitation to question the architecture of possibility.",
            "Innovation begins when accepted assumptions become questions.",
            "The future is not discovered by waiting. It is engineered through deliberate experiments.",
            "A different perspective can solve what a thousand additional lines of code cannot.",
        ],
    },

    4: {
        "theme": "EXECUTION",
        "mood": "DELIVER RESULTS",
        "quotes": [
            "A beautiful architecture that never ships remains an unfinished argument.",
            "Measure progress by what works, not by what you intended to build.",
            "The final mile separates impressive plans from useful systems.",
            "Ideas earn attention. Execution earns trust.",
        ],
    },

    5: {
        "theme": "EXPLORATION",
        "mood": "LEARN AND BUILD",
        "quotes": [
            "Curiosity is the beginning of expertise; deliberate practice is its foundation.",
            "Explore beyond your stack. The next solution may live outside your comfort zone.",
            "Every experiment teaches something that documentation alone cannot.",
            "Build something unfamiliar. Discover what your current knowledge cannot yet explain.",
        ],
    },

    6: {
        "theme": "REFLECTION",
        "mood": "RESET AND RETHINK",
        "quotes": [
            "Reflection turns experience into intelligence and mistakes into architecture.",
            "A pause is not a retreat. Sometimes it is where the next strategy becomes visible.",
            "Review the system, question the assumptions, and prepare for a better iteration.",
            "The next chapter deserves a better version of the mind writing it.",
        ],
    },
}


# =====================================================
# GENERATE DAILY TRANSMISSION
# =====================================================

def generate_daily_content():

    now = datetime.now(TIMEZONE)

    weekday = now.weekday()
    day = DAILY_DATA[weekday]

    # Rotate quotes every ISO calendar week.
    quote_index = (now.isocalendar().week - 1) % len(day["quotes"])
    quote = day["quotes"][quote_index]

    day_name = now.strftime("%A").upper()
    formatted_date = now.strftime("%d %B %Y").upper()

    day_of_week = weekday + 1
    day_of_year = now.timetuple().tm_yday
    total_days = 366 if now.year % 4 == 0 and (
        now.year % 100 != 0 or now.year % 400 == 0
    ) else 365

    week_number = now.isocalendar().week

    content = f"""### {day_name} // ENGINEERING MODE

**{formatted_date}**

<sub>DAY {day_of_week:02d} OF THE WEEK · DAY {day_of_year} OF {total_days} · WEEK {week_number:02d}</sub>

<sub>{day["theme"]} MODE // {day["mood"]}</sub>

> *"{quote}"*

**OBSERVE. CALCULATE. ENGINEER. EXECUTE.**
"""

    return content


# =====================================================
# UPDATE README
# =====================================================

def update_readme():

    if not README_PATH.exists():
        raise FileNotFoundError("README.md was not found.")

    readme = README_PATH.read_text(encoding="utf-8")

    if readme.count(START_MARKER) != 1:
        raise ValueError("Expected exactly one DAILY-START marker.")

    if readme.count(END_MARKER) != 1:
        raise ValueError("Expected exactly one DAILY-END marker.")

    start = readme.index(START_MARKER) + len(START_MARKER)
    end = readme.index(END_MARKER)

    if start >= end:
        raise ValueError("Daily markers are incorrectly positioned.")

    daily_content = generate_daily_content()

    updated_readme = (
        readme[:start]
        + "\n"
        + daily_content
        + readme[end:]
    )

    README_PATH.write_text(updated_readme, encoding="utf-8")

    print("======================================")
    print(" DAILY ENGINEERING TRANSMISSION")
    print("======================================")
    print(daily_content)
    print("README successfully updated.")


# =====================================================
# ENTRY POINT
# =====================================================

if __name__ == "__main__":
    update_readme()
