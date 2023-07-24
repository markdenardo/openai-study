

import openai
import sys
sys.path
sys.path.append('/usr/local/lib/python3.9/site-packages')

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                          {"role": "user", "content": "write a short story about capybara making friends"}])

print(completion.choices[0].message.content)
