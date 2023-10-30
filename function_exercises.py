#!/usr/bin/env python
# coding: utf-8

# ### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[187]:


def is_two(num):
    if num in (2, '2'):
        return True
    else:
        return False



# ### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[191]:


def is_vowel(character):
    vowels = 'a','e','i','o','u','A' ,'E', 'I', 'O', 'U'
    return character in vowels




# ### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[101]:


def is_consonant(character):
    return not is_vowel(character)





# ### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[165]:


def capitalize_if_consonant(word):
    if word and word[0].isalpha() and word[0].lower() not in 'a,e,i,o,u':
        return word[0].upper() + word[1:]
    else:
        return word
        



# ### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[201]:


def calculate_tip(tip_percentage, bill_total):
    if 0 <= tip_percentage <= 1:
        tip_amount = tip_percentage * bill_total
        return tip_amount
    else:
        return 'Not a valid tip amount. Please provide a number between 0 and 1'




# ### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[204]:


def apply_discount(original_price, discount_percentage):
    if 0 <= discount_percentage <= 100:
        discount = original_price * (discount_percentage / 100)
        discounted_price = original_price - discount
        return discounted_price
    else:
        return "Invalid discount percentage. Please provide a value between 0 and 100."




# ### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[161]:


def handle_commas(number_with_commas):
    if ',' in number_with_commas:
        return float(number_with_commas.replace(',', ''))
    else:
        return float(number_with_commas)




# ### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[172]:


def get_letter_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid input, score out of range'





# ### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[216]:


def remove_vowels(word):
    vowels = 'A, E, I, O, U, a, e, i, o, u'
    result = ''.join(char for char in word if char not in vowels)
    return result




# ### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# * anything that is not a valid python identifier should be removed
# * leading and trailing whitespace should be removed
# * everything should be lowercase
# * spaces should be replaced with underscores
# 

# In[218]:


def normalize_name(somestr):
    new_string = ''
    somestr = somestr.strip().lower()
    for char in somestr:
        if char.isalpha() or char == ' ':
            new_string += char
    return new_string.strip().replace(' ', '_')




# ### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[237]:


def cumulative_sum(oldlist):
    newlist=[]
    c_sum = 0
    for num in oldlist:
        c_sum += num
        print(f'cumulative: {c_sum}')
        newlist.append(c_sum)
    print(f'oldlistt: {oldlist}')
    print(f'newlist: {newlist}')
