#generate sentence from user

#split sentence into words

#loop through words and convert to pig latin

#stick words back together

#output the final string


sentence = input("please type a sentence: ").strip().lower()
words = sentence.split() #will generate a list of words from the sentence

new_words = []
for word in words:
  #code that converts each word into pig latin
  if word[0] in "aeiou":
    new_word = word + "yay"
    new_words.append(new_word)
  else:
    vowel_index = 0
    for letter in word:
      if letter not in "aeiou":
        vowel_index += 1
      else:
        break
    print(vowel_index)
    consonants = word[:vowel_index]
    the_rest = word[vowel_index:]
    new_word = the_rest + consonants + "ay"
    new_words.append(new_word)

print(new_words)

new_sentence = " ".join(new_words) #joining new_words list with a space
print(new_sentence)
