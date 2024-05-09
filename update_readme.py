import random
import re

# Read the README file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Define the old and new image URLs
old_image_url = 'https://github-readme-streak-stats.herokuapp.com?user=garvit-exe&theme=transparent&date_format=j%20M%5B%20Y%5D&hide_border=true'
new_image_url = 'https://github-readme-streak-stats.herokuapp.com?user=garvit-exe&theme=react&date_format=j%20M%5B%20Y%5D&hide_border=true'

# Replace the old image URL with the new one
readme_content = readme_content.replace(old_image_url, new_image_url)

# Write the updated README content back to the file
with open('README.md', 'w') as file:
    file.write(readme_content)

