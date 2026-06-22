import requests
from pathlib import Path

USERNAME = "kauanmezavila"

events = requests.get(
    f"https://api.github.com/users/{USERNAME}/events/public"
).json()

last_push = next(
    event for event in events
    if event["type"] == "PushEvent"
)

repo = last_push["repo"]["name"]

content = f"""
Atualmente estou trabalhando em:

### 🚀 [{repo}](https://github.com/{repo})
"""

readme = Path("README.md").read_text(encoding="utf-8")

start = "<!-- LAST_REPO_START -->"
end = "<!-- LAST_REPO_END -->"

before = readme.split(start)[0]
after = readme.split(end)[1]

new_readme = (
    before
    + start
    + "\n"
    + content
    + "\n"
    + end
    + after
)

Path("README.md").write_text(
    new_readme,
    encoding="utf-8"
)
