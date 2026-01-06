# Task 5.1: The Spy Message Decoder
# Scenario: You intercepted a scrambled message from a rival
# spy agency. You need to decode it.
# Instructions:
# 1. Variable scrambled = ##gnimmargorP nohtyP evoL
# I##;.
# 2. Clean: Remove the
# hashtags # using .strip() or .replace().
# 3. Reverse: Flip the string so it reads correctly (Hint:
# slicing [::-1]).
# 4. Analyze: Count how many times the letter &quot;o&quot; appears in the
# decoded text.
# 5. Print the final clean message and the count.

scrambled = "##gnimmargorP nohtyP evoL I##"
cleaned = scrambled.replace("#", "")
reversed_message = cleaned[::-1]
o_count = reversed_message.lower().count("o")
print(f"Decoded Message: {reversed_message}")
print(f"Number of 'o's: {o_count}")

