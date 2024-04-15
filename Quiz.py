

print("Welcome to the Quiz!\nRules:-\n1.The quiz consists of three levels\n2.Each level has 2 categories")
print("3.Each category consists of 10 questions\n4.to progress to the next level the player should score at least:-\n   30% in Level 1")
print("   40% in level 2\n   50%  in level3\n5.You can pass as many questions as you want by typing pass.\n6.You can only answer 3 questions incorrectly per level.\n7.Write all answers in small letters.\n\n")
print("LEVEL-1")
print("The categories are:-\n1.Mental Maths\n2.Indian History")
c1=input("Enter the serial number of category:- ")
w1=0
p1=0
a=0
b=0
p2=0
w2=0
w3=0
p3=0
if c1=="1":
    for q in range (1,11):
        if w1==4:
            break
        if q==1:
                
            q1=input("Q1.What is the square root of 144? ")
            if q1=="12":
                print("Correct answer")
                p1+=1
              
            elif q1=="pass":
                print("Question passed")
    
            else:
              print('Wrong answer')
              w1+=1

        if q==2:        
            q2=input("Q2.What is 6x8? ")
            if q2=="48":
                print("Correct answer")
                p1+=1
                
            elif q2=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==3:
            q3=input("Q3.What is the cube of 3? " )
            if q3=="27":
                print("Correct answer")
                p1+=1
            elif q3=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==4:        
            q4=input("Q4.What is 34523 raised to the power 0? ")
            if q4=="1":
                print("Correct answer")
                p1+=1
            elif q4=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==5:
            q5=input("Q5.How many sides does a decagon have? ")
            if q5=='10':
                print("Correct answer")
                p1+=1
            elif q5=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==6:
            q6=input("Q6.What is 234x574x0+34? ")
            if q6=="34":
                print("Correct answer")
                p1+=1
            elif q6=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==7:
            q7=input("Q7.If a Ram gives 30% of his marbles to Shyam,he has 14 marbles left,how many marbles did he have at the start? ")
            if q7=="20":
                print("Correct answer")
                p1+=1
            elif q7=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')
    
        if q==8:
            q8=input("Q8.How many vertices does cylinder have? ")
            if q8=="0":
                print("Correct answer")
                p1+=1
            elif q8=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==9:
            q9=input("Q9.If Q+4=5.What is the value of Q? ")
            if q9=="1":
                print("Correct answer")
                p1+=1
            elif q9=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')
    
        if q==10:
            q10=input("Q10.If 4 men can dig 4 wells in 4 hours.In how many hours will 400 men dig 400 wells? ")
            if q10=="4":
                print("Correct answer")
                p1+=1
            elif q10=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')
        if p1>=3:
            a=1
        if p1<3:
               a=2
elif c1=="2":
    for q in range (1,11):
        if w1==4:
            break
        if q==1:
                
            q1=input("Q1.Upnishads are books on? ")
            if q1=="philosophy":
                print("Correct answer")
                p1+=1
            elif q1=="pass":
                print("Question passed")
    
            else:
              print('Wrong answer')
              w1+=1

        if q==2:        
            q2=input("Q2.Who was the first Indian ruler who had territory outside India? ")
            if q2=="kanishka":
                print("Correct answer")
                p1+=1
            elif q2=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==3:
            q3=input("Q3.Where were the hymns of Rigveda composed? " )
            if q3=="punjab":
                print("Correct answer")
                p1+=1
            elif q3=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==4:        
            q4=input("Q4.Who was the ruler of the kingdom between the rivers Jhelum and Chenab? ")
            if q4=="porus":
                print("Correct answer")
                p1+=1
            elif q4=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==5:
            q5=input("Q5.Who was the last Hindu emperor of northern India? ")
            if q5=="harsha":
                print("Correct answer")
                p1+=1
            elif q5=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==6:
            q6=input("Q6.In which Year did India attain Independence? ")
            if q6=="1947":
                print("Correct answer")
                p1+=1
            elif q6=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==7:
            q7=input("Q7.Bimbisara was the founder of which one of the following dynasties? ")
            if q7=="shunga":
                print("Correct answer")
                p1+=1
            elif q7=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')
    
        if q==8:
            q8=input("Q8.A Janapadin was the ___ of a janapada. ")
            if q8=="ruler":
                print("Correct answer")
                p1+=1
            elif q8=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')

        if q==9:
            q9=input("Q9.Dholavira is situated at the bank of River? ")
            if q9=="luni":
                print("Correct answer")
                p1+=1
            elif q9=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')
    
        if q==10:
            q10=input("Q10.In the Vedic age, who was the head of “Grama”? ")
            if q10=="gramini":
                print("Correct answer")
                p1+=1
            elif q10=="pass":
                print("Question passed")
            else:
                w1+=1
                print('Wrong answer')
        if p1>=3:
            a=1
        if p1<3:
            a=2
else:
    print("Error:Invalid Serial Number")
if w1==4:
    a=2
if a==2:
   print("Game Over\nTry again??")
            
if a==1:
    print("Congratulations!You Proceeded to next Level.\n \n")
    print("\n\nLEVEL-2")
    print("The categories are:-\n1.Constitition\n2.Genral Knowledge")
    c2=input("Enter the serial number of category:- ")
    if c2=="1":
        for q12 in range(1,11):
            if w2==4:
                break
            if q12==1:
                
               q1=input("Q1.Before the independence of India, Dadra and nagar haveli were under the administrative control of ? ")
               if q1=="portuguese":
                  print("Correct answer")
                  p2+=1
               elif q1=="pass":
                    print("Question passed")
    
               else:
                 print('Wrong answer')
                 w2+=1

            if q12==2:        
                q2=input("Q2.Which Constitutional Article lays down the provision for a National Commission for SC and ST{write the number}? ")
                if q2=="338":
                    print("Correct answer")
                    p2+=1
                elif q2=="pass":
                    print("Question passed")
                else:
                    w2+=1
                    print('Wrong answer')
                 
            if q12==3:
               q3=input("Q3.Which community gets special provision for Central Services in Article 336? " )
               if q3=="anglo-indian":
                    print("Correct answer")
                    p2+=1
               elif q3=="pass":
                    print("Question passed")
               else:
                w2+=1
                print('Wrong answer')

            if q12==4:        
                q4=input("Q4. National Commission for SC and ST shall be made by which constitutional institution ? ")
                if q4=="parliament":
                    print("Correct answer")
                    p2+=1
                elif q4=="pass":
                    print("Question passed")
                else:
                    w2+=1
                    print('Wrong answer')

            if q12==5:
                q5=input("Q5.Which Constitutional Article defines the Panchayat Raj? ")
                if q5=="243":
                    print("Correct answer")
                    p2+=1
                elif q5=="pass":
                    print("Question passed")
                else:
                    w2+=1
                    print('Wrong answer')
    
            if q12==6:
                q6=input("Q6.The Constitution of India, was drafted and enacted in which language ? ")
                if q6=="english":
                    print("Correct answer")
                    p2+=1
                elif q6=="pass":
                    print("Question passed")
                else:
                    w1+=1
                    print('Wrong answer')

            if q12==7:
                q7=input("Q7. Total No. of Schedule in Constitution of India is? ")
                if q7=="12":
                    print("Correct answer")
                    p2+=1
                elif q7=="pass":
                    print("Question passed")
                else:
                    w2+=1
                    print('Wrong answer')
    
            if q12==8:
                q8=input("Q8. Total No. of fundamental rights in Constitution of India is  ")
                if q8=="6":
                    print("Correct answer")
                    p2+=1
                elif q8=="pass":
                    print("Question passed")
                else:
                    w2+=1
                    print('Wrong answer')

            if q12==9:
                q9=input("Q9. As per constitution of India, the Legislative assembly of a state consists of more than 500 and not less than 60 members, but which has 32 Members ? ")
                if q9=="sikkim":
                    print("Correct answer")
                    p2+=1
                elif q9=="pass":
                    print("Question passed")
                else:
                    w2+=1
                    print('Wrong answer')
    
            if q12==10:
                q10=input("Q10.How many members can be nominated to the rajya sabha by president of India ? ")
                if q10=="12":
                    print("Correct answer")
                    p2+=1
                elif q10=="pass":
                    print("Question passed")
                else:
                    w2+=1
                    print('Wrong answer')
            if p2>=4:
                b=1
            if p2<4:
                b=2
    elif c2=="2":
            for q12 in range (1,11):
                if w2==4:
                    if q12==1:
                        q1=input("Q1.Entomology is the science that studies ")
                    if q1=="insects":
                        print("Correct answer")
                        p2+=1
                    elif q1=="pass":
                         print("Question passed")
    
                    else:
                       print('Wrong answer')
                       w2+=1
    
                if q12==2:        
                    q2=input("Q2.Eritrea, which became the 182nd member of the UN in 1993, is in the continent of ")
                    if q2=="africa":
                        print("Correct answer")
                        p2+=1
                    elif q2=="pass":
                        print("Question passed")
                    else:
                        w2+=1
                        print('Wrong answer')

                if q12==3:
                    q3=input("Q3.Which community gets special provision for Central Services in Article 336? " )
                    if q3=="anglo-indian":
                        print("Correct answer")
                        p2+=1
                    elif q3=="pass":
                        print("Question passed")
                    else:
                        w2+=1
                        print('Wrong answer')

                if q12==4:        
                    q4=input("Q4.Golf player Vijay Singh belongs to which country?")
                    if q4=="fiji":
                       print("Correct answer")
                       p2+=1
                    elif q4=="pass":
                        print("Question passed")
                    else:
                       w2+=1
                       print('Wrong answer')

                if q12==5:
                    q5=input("Q5.First Afghan War took place in which year? ")
                    if q5=="1839":
                        print("Correct answer")
                        p2+=1
                    elif q5=="pass":
                        print("Question passed")
                    else:
                        w2+=1
                    print('Wrong answer')

                if q12==6:
                    q6=input("Q6.Federation Cup, World Cup, Allywyn International Trophy and Challenge Cup are awarded to winners of? ")
                    if q6=="volleyball":
                        print("Correct answer")
                        p2+=1
                    elif q6=="pass":
                        print("Question passed")
                    else:
                        w2+=1
                        print('Wrong answer')

                if q12==7:
                    q7=input("Q7.Film and TV institute of India is located at? ")
                    if q7=="pune":
                        print("Correct answer")
                        p2+=1
                    elif q7=="pass":
                        print("Question passed")
                    else:
                        w2+=1
                        print('Wrong answer')
    
                if q12==8:
                    q8=input("Q8.Georgia, Uzbekistan and Turkmenistan became the members of UNO in?  ")
                    if q8=="1992":
                        print("Correct answer")
                        p2+=1
                    elif q8=="pass": 
                        print("Question passed")
                    else:
                        w2+=1
                        print('Wrong answer')

                if q12==9:
                    q9=input("Q9.During World War II, when did Germany attack France? ")
                    if q9=="1940":
                        print("Correct answer")
                        p2+=1
                    elif q9=="pass":
                        print("Question passed")
                    else:
                        w2+=1
                        print('Wrong answer')
    
                if q12==10:
                    q10=input("Q10.During World War II, when did Germany attack France?? ")
                    if q10=="mosquito":
                        print("Correct answer")
                        p2+=1
                    elif q10=="pass":
                        print("Question passed")
                    else:
                        w2+=1
                        print('Wrong answer')
                if p2>=4:
                    b=1
                if p2<4:
                    b=2    
    else:
        print("Error:Invalid Serial Number")
    if w2==4:
        b==2
    if b==2:
       print("Game Over.\nTry again??")            
    if b==1:
        print("Congratulations!You Proceeded to next Level.\n \n")
        print("\n\nLEVEL-3") 
        print("The categories are:-\n1.Biology\n2.Chemistry")
        c3=input("Enter the serial number of category:- ")
        if c3=="1":
            for q13 in range(1,11):
                if w3==4:
                    break
                if q13==1:
                
                    q1=input("Q1. A baby blue whale drinks this many liters of milk per day ?")
                    if q1=="190":
                        print("Correct answer")
                        p3+=1
                    elif q1=="pass":
                        print("Question passed")
    
                    else:
                      print('Wrong answer')
                      w3+=1

                if q13==2:        
                    q2=input('Q2.Which blood group is called the "universal donor"? ')
                    if q2=="o":
                        print("Correct answer")
                        p3+=1
                    elif q2=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==3:
                    q3=input("Q3.How much blood is in the human body{in L}? " )
                    if q3=="7":
                        print("Correct answer")
                        p3+=1
                    elif q3=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==4:        
                    q4=input("Q4.How many basic tastes can humans sense? ")
                    if q4=="5":
                        print("Correct answer")
                        p3+=1
                    elif q4=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==5:
                    q5=input("Q5.What sensory function do the ears provide other than hearing? ")
                    if q5=="balance":
                        print("Correct answer")
                        p3+=1
                    elif q5=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==6:
                    q6=input("Q6.Which group of animals is Charles Darwin best known for studying? ")
                    if q6=="birds":
                        print("Correct answer")
                        p3+=1
                    elif q6=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==7:
                    q7=input("Q7. How many sets of legs does a shrimp have? ")
                    if q7=="5":
                        print("Correct answer")
                        p3+=1
                    elif q7=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
    
                if q13==8:
                    q8=input("Q8.Which is the most abundant gas in the earth's atmosphere?")
                    if q8=="nitrogen":
                        print("Correct answer")
                        p3+=1
                    elif q8=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
        
                if q13==9:
                    q9=input("Q9.Which gas evolved from  paddy fields and marshes? ")
                    if q9=="methane":
                        print("Correct answer")
                        p3+=1
                    elif q9=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
    
                if q13==10:
                    q10=input("Q1.0What is the toxicity caused by silicon called? ")
                    if q10=="silcosois":
                        print("Correct answer")
                        p3+=1
                    elif q10=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
                if p3>=5:
                    c=1
                if p3<5:
                    c=2
        elif c3=="2":
            for q13 in range(1,11):
                if w3==4:
                    break
                if q13==1:
                
                    q1=input("Q1.The number of moles of solute present in 1 kg of a solvent is called its? ")
                    if q1=="molality":
                          print("Correct answer")
                          p3+=1
                    elif q1=="pass":
                        print("Question passed")
    
                    else:
                      print('Wrong answer')
                      w3+=1

                if q13==2:        
                    q2=input("Q2 The metal used to recover copper from a solution of copper sulphate is ? ")
                    if q2=="Fe":
                       print("Correct answer")
                       p3+=1
                    elif q2=="pass":
                       print("Question passed")
                    else:
                      w3+=1
                      print('Wrong answer')

                if q13==3:
                    q3=input("Q3.the metallurgical process in which a metal is obtained in a fused state is called ?" )
                    if q3=="smelting":
                       print("Correct answer")
                       p3+=1
                    elif q3=="pass":
                          print("Question passed")
                    else:
                       w3+=1
                       print('Wrong answer')
                
                    if q13==4:        
                        q4=input("Q4.The most commonly used bleaching agent is? ")
                    if q4=="chlorine":
                        print("Correct answer")
                        p3+=1
                    elif q4=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==5:
                    q5=input("Q5.The heat required to raise the temperature of body by 1 K is called? ")
                    if q5=="thermal capacity":
                       print("Correct answer")
                       p3+=1
                    elif q5=="pass":
                         print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==6:
                    q6=input("Q6.The nuclear particles which are assumed to hold the nucleons together are? ")
                    if q6=="mesons":
                        print("Correct answer")
                        p3+=1
                    elif q6=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
                
                if q13==7:
                    q7=input("Q7 The metal that is used as a catalyst in the hydrogenation of oils is? ")
                    if q7=="nickel":
                        print("Correct answer")
                        p3+=1
                    elif q7=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
    
                    if q13==8:
                       q8=input("Q8.The most abundant rare gas in the atmosphere is")
                    if q8=="argon":
                        print("Correct answer")
                        p3+=1
                    elif q8=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')

                if q13==9:
                    q9=input("Q9.The heat energy produced when the human body metabolises 1 gram of fat is{in kj}? ")
                    if q9=="39":
                        print("Correct answer")
                        p3+=1
                    elif q9=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
    
                if q13==10:
                    q10=input("Q10.The most malleable metal is? ")
                    if q10=="gold":
                        print("Correct answer")
                        p3+=1
                    elif q10=="pass":
                        print("Question passed")
                    else:
                        w3+=1
                        print('Wrong answer')
                if p3>=5:
                    c=1
                if p3<5:
                    c=2
        else:
            print("Error:Invalid Serial Number")
        if c==2:
            print("Game Over.\nTry again??")
        if c==1:
            t=p1+p2+p3
            print("Congratulations!You passed the Quiz,\nwith",t,"points")
            
                
            
                
            
             
    
    
    
    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    