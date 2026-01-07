# Task 7.1: The Library Book Organizer
# Scenario: You have a pile of returned books (some duplicates)
# and need to update the library catalog.
# Instructions:
# 1. returned_books = [&quot;1984&quot;, &quot;Hobbit&quot;, &quot;1984&quot;,
# &quot;Dune&quot;, &quot;Hobbit&quot;].
# 2. Unique: Convert the list to a Set to remove duplicates.
# 3. Catalog: Create a dictionary library = {&#39;1984&#39;: 5,
# &#39;Hobbit&#39;: 2}.
# 4. Update: Loop through the unique set. If the book is
# in library, add +1 to its count. If not, add it with count 1.
# 5. Print the final library dictionary.

returned_books = ["1984", "Hobbit", "1984", "Dune", "Hobbit"]
unique_books=set(returned_books)
library={"1984":5,"Hobbit":2}

for book in unique_books:
    if book in library:
        library[book] += 1
    else:
        library[book] = 1
print("Updated Library Catalog:", library)
