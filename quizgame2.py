import random

def quiz():
    
    score = 0

    q1 = raw_input('What type of animal is Bambi?: ')
    if q1 == ('deer'):
        score += 10
        print 'correct'
    else:
        print 'incorrect'
    q2 = raw_input('Which country features a maple leaf on its flag?: ')
    if q2 == ('canada'):
        score += 10
        print 'correct'
    q3 = raw_input('Who wrote the Harry Potter series?: ')
    if q3 == ('jk rowling'):
        score += 10 
        print 'correct'
    else: 
        print 'incorrect'
    q4 = raw_input('What is the official language of Brazil?: ')
    if q4 == ('portuguese'):
        score += 10 
        print 'correct'
    else: 
        print 'incorrect'
    q5 = raw_input('What superhero has been played by Michael Keaton, Val Kilmer, George Clooney and Christian Bale?: ')
    if q5 == ('batman'):
        score += 10 
        print 'correct'
    else: 
        print 'incorrect'
    q6 = raw_input('Which month is Black History Month in USA?: ')
    if q6 == ('february'):
        score += 10 
        print 'correct'
    else: 
        print 'incorrect'
    q7 = raw_input('The Everglades are in what state?: ')
    if q7 == ('florida'):
        score += 10 
        print 'correct'
    else: 
        print 'incorrect'    

    game_over = raw_input ('You scored' ,score,'%. Type Y to play again: ')
        
        
    
    
    
    