import re

demo_text = 'I have applied for German Job-Seeker Visa. I am already looking for companies located in Germany offering roles similar to mine.'

country_re = r'\bG\w+'
x = re.findall(country_re, demo_text)

print(x)