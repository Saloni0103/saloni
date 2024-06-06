#!/usr/bin/env python
# coding: utf-8
# 1 answer
in python escape characters are special character that are used to represent other characters or to perform specific functions.
Here are some escape characters in python.

\n=new line character
\t=tab character ,used to create a horizontal space
\r=carriage return , used to return to the begining of the line
\b=backspace, used to remove the previous character of space
\f=form feed character, used to advance to the next page or form
\\=backslash character
\'=single quote, used to represent a single character
\"=double quote, used to represent a double character
\a=alert, used to sound an alarm (ascii bell character,used to produce a sound bell).
\v=vertical tab, used to create a vertical space
\xhh=hexadecimal character
\\ooo=octal character
\N{name}=unicode character
\uxxxx=unicode character ,used by hexadecimal point code xxxx
\Uxxxxxxxx=unicode character ,used by hexadecimal point code xxxxxxxx
# In[2]:


print("Hello\nWorld")
print("Hello\tWorld")
print("Hello \r World")
print("Hello\\World")
print('Hello \'World\'')
print("Hello \"World\"")
print("\u2665")  # heart symbol
print("\x41")  # ASCII character 'A'
print("\101")  # ASCII character 'A'
print(r"Hello\nWorld")


# In[12]:


#2.
# \n is a new line character
#\t is a tab
print("MY\nlife") #\n
print("MY\tlife") #\t


# In[3]:


#3. Single quotes with escaping
single_quotes_escaped = 'Howl\'s Moving Castle'
print(single_quotes_escaped)  # Output: Howl's Moving Castle


# In[4]:


#4.
import os

newlines = os.linesep * 5
print(newlines)

print(*[""] * 5, sep="")


# In[8]:


#4.

import os
newlies =os.linesep*1
print(newlies)

newlines = "s"
for i in range(1):
    newlines += ""
print(newlines)


# In[9]:


#5.
print("Hello world!"[1])
print("Hello world!"[0:5])
print("Hello world!"[:5])
print("Hello world!"[3:])


# In[25]:


#7.
print("Hello".upper())
print("Hello".upper().isupper())
print("Hello".upper().lower())


# In[26]:


#8.
print("Remember, remember, the fifth of July.".split())  
print("-".join("There can only one.".split())) 


# In[30]:


#9.methods for right-justifying, left-justifying, and centering a string.

print("Hello".rjust(20))  # right-justified
print("Hello".ljust(20))  # left-justified
print("Hello".center(20)) # center-justified


# In[43]:


#10.
s = '  Hello  World   From DigitalOcean \t\n\r\tHi There  '
result = s.strip()
print(result)


# In[ ]:





# In[ ]:




