#!/usr/bin/env python
# coding: utf-8

# # Name(s)
# Richa Gadgil

# **Instructions:** This is an individual assignment. Complete the following code and push to get your score.

# I am providing the autograder answers locally so you may test your code before pushing. I will be reviewing your submissions, and if I find you are circumventing the autograder in any manner, you will receive a 0 on this assignment and your case will be reported to the honor board for review. i.e., approach the assignment in a genuine manner and you have nothing to worry about.

# In[ ]:





# **Question 1.**
# When will new material be available each week?

# You can answer the question by defining an anonymous function. This creates a function that I can test using pytest. You don't have to worry about the details. You just need to answer the question by changing the string argument that is currently set to "D". I know this is a bit weird, but I want you to get used to submitting code as early as possible.

# In[1]:


# Nothing to modify in this cell
def question_1(answer):
    answers = {
        "A": "Monday morning",
        "B": "Sunday night",
        "C": "Monday evening",
        "D": "I don't know"
    }
    try:
        return answers[answer]
    except:
        return "Not a valid answer"


# In[2]:


# YOUR SOLUTION HERE
# Sample incorrect answer
answer_question_1 = lambda: question_1("C")


# **Question 2.**
# Do I need to buy the textbook?

# In[4]:


# Nothing to modify in this cell
def question_2(answer):
    answers = {
        "A": "No",
        "B": "Maybe",
        "C": "Yes. You will struggle with some of the chapters without the textbook",
    }
    try:
        return answers[answer]
    except:
        return "Not a valid answer"


# In[5]:


# YOUR SOLUTION HERE
# Sample incorrect answer
answer_question_2 = lambda: question_2("C")


# **Question 3.**
# Are these any required times that I be online?

# In[6]:


# Nothing to modify in this cell
def question_3(answer):
    answers = {
        "A": "Yes",
        "B": "No"
    }
    try:
        return answers[answer]
    except:
        return "Not a valid answer"


# In[3]:


# YOUR SOLUTION HERE
# Sample incorrect answer
answer_question_3 = lambda: question_3("A")


# **Question 4.**
# What software will I use to complete the assignments?

# In[8]:


# Nothing to modify in this cell
def question_4(answer):
    answers = {
        "A": "Java",
        "B": "Netbeans",
        "C": "Anaconda"
    }
    try:
        return answers[answer]
    except:
        return "Not a valid answer"


# In[4]:


# YOUR SOLUTION HERE
# Sample incorrect answer
answer_question_4 = lambda: question_4("C")


# **Question 5.**
# Do I need to participate in this class or can I just do the labs and assignments?

# In[10]:


# Nothing to modify in this cell
def question_5(answer):
    answers = {
        "A": "Yes. If you want to get anything higher than a C, you'll need to do more than the labs and assignments",
        "B": "No",
    }
    try:
        return answers[answer]
    except:
        return "Not a valid answer"


# In[5]:


# YOUR SOLUTION HERE
# Sample incorrect answer
answer_question_5 = lambda: question_5("A")


# In[6]:


# Don't forget to push!


# In[ ]:





# In[ ]:




