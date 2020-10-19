print("Welcome to MattLib!")
print("Please gimme the following...")
print()

adj_1 = input("Adjective: ")
noun_1 = input("Noun: ")
past_tense_verb_1 = input("Verb (past tense): ")
adverb_1 = input("Adverb: ")
adj_2 = input("Another adjective: ")
noun_2 = input("Another noun: ")
noun_3 = input("A noun again: ")
adj_3 = input("And another adjective: ")
verb = input("Verb: ")
adverb_2 = input("Another adverb: ")
past_tense_verb_2 = input("Verb (past tense): ")
adj_4 = input("Finally, an adjective: ")

template =f"Today I went to the zoo. I saw a(n) {adj_1} {noun_1} jumping up and\ndown in its tree. He {past_tense_verb_1} {adverb_1} through the large tunnel\nthat led to its {adj_2} {noun_2}. I got some peanuts and passed them through\nthe cage to a gigantic gray {noun_3} towering above my head. Feeding that\nanimal made me hungry. I went to get a {adj_3} scoop of ice cream. It filled my\nstomach. Afterwards I had to {verb} {adverb_2} to catch our bus. When I got home\nI {past_tense_verb_2} my mom for a {adj_4} day at the zoo."

print()
print(template)
