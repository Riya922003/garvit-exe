import random
import re

# List of available themes
themes = ['react']

# Generate a random theme
new_theme = random.choice(themes)

# Read the README file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Update the GitHub Stats image URLs with the new theme
readme_content = re.sub(r'(https://github-readme-stats-garvit-exe\.vercel\.app/api\?username=garvit-exe&theme=)[^\s]+', rf'\1{new_theme}', readme_content)

# Update the Top Languages image URLs with the new theme
readme_content = re.sub(r'(https://github-readme-stats-garvit-exe\.vercel\.app/api/top-langs/\?username=garvit-exe&theme=)[^\s]+', rf'\1{new_theme}', readme_content)

# Update the GitHub Streak image URLs with the new theme
readme_content = re.sub(r'(https://github-readme-streak-stats\.herokuapp\.com\?user=garvit-exe&theme=)[^\s]+', rf'\1{new_theme}', readme_content)

# Write the updated README content back to the file
with open('README.md', 'w') as file:
    file.write(readme_content)
