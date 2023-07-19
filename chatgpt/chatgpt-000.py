import openai
import sys
sys.path
sys.path.append('/usr/local/lib/python3.9/site-packages')

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                          {"role": "user", "content": "write a short story about capybara making friends"}])

print(completion.choices[0].message.content)

# output

# One sunny morning, as Charlie strolled along the riverbank, he noticed a group of nervous monkeys chattering among themselves. Curiosity piqued, Charlie approached them cautiously, sensing their unease. The eldest monkey, Winston, explained that they were searching for a new home since their original habitat had been disturbed by humans. They were anxious because they couldn't find a suitable place to settle.

# Charlie, ever empathetic, knew he couldn't stand by and do nothing. With a reassuring smile, he suggested, "Why don't you come and stay with me? I'm sure my forest friends wouldn't mind sharing their homes with you."

# The monkeys exchanged glances, unsure of Charlie's offer. Winston, intrigued by the capybara's kindness, proposed they give it a try. With newfound hope, they followed Charlie through the forest, catching curious glances from other animals along the way.

# As they arrived at Charlie's dwelling—a cozy burrow nestled near the river—the capybara introduced the monkeys to his friends. They met Miranda, the wise old owl, who shared her hollow tree for the monkeys to roost in. Benjamin, a slow-moving sloth, offered them shelter on his tree branches, assuring the monkeys that his home was vast enough to accommodate their group. Enthusiastic chatter filled the air as everyone embraced the spirit of friendship and unity.

# Days turned into weeks, and the bond between Charlie and his newfound friends grew stronger every passing moment. The monkeys, grateful for the capybara's selflessness, worked tirelessly each day, gathering fruits and nuts to help sustain their hosts. They became an inseparable family, sharing stories, laughter, and even shedding tears together.

# News of the capybara's compassion spread throughout the rainforest, capturing the hearts of more creatures. A family of colorful macaws sought refuge with Charlie, offering mesmerizing melodies in return. A group of tiny frogs hopped alongside the monkeys, proclaiming their support for their new companions. The rainforest transformation was a testament to the power of kinship.

# Before long, the humans who had disrupted the monkeys' original home approached Charlie, moved by the harmony he had created. They realized the importance of preserving the rainforest and its diverse inhabitants. With their newfound understanding, they dedicated themselves to conserving the environment, ensuring a safe home for everyone who called the forest their own.

# And so, the rainforest flourished, filled with the laughter and joy of animals big and small. All thanks to the remarkable friendship of one capybara, whose kindness and compassion brought an entire community together, forever etching his legacy in the hearts of all who knew him.
