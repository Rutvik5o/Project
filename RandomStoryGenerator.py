import random

#defining a list of python for sentence making


topic=['DSA','Python','Java','Computer Networks','C++','Web Development']

adj=['an important','an essential','very important','an interesting']


to=['Developers','student','professional','Freshers']

supportive= ['learn it','master it','read it ','see it']

where = ['Coding ninjas','Code Studio','Code studio library','CN Guided Path','Geek for geeks','Javatpoint']

#generating our output 

print(random.choice(topic) + ' is ' + random.choice(adj) + ' topic for '+ random.choice(to) + ',  you can '+ random.choice(supportive) + ' from ' + random.choice(where))


#explonation

'''
it is one of the exciting beginner python projects with source code. Every 
time a user runs a code . the random story generator project tries to produce a different and random story.
'''