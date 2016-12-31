def goodVsEvil(good, evil):
      good1 = good.split()
      evil1 = evil.split()
      
      #print good1
      #print evil1
      
      counter1 = 0
      for i in good1:
        counter1 = counter1 + int(i)
        
      #print counter1
      
      counter2 = 0
      for j in evil1:
        counter2 = counter2 + int(j)
        
      #print counter2
        
      if counter1 == counter2:
        print 'Should be a tie'
      elif counter1 > counter2:
        print 'Good should triumph'
      else:
        print 'Evil should win'
          
        
      return
    
    
goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')  # == 'Battle Result: Evil eradicates all trace of Good', 'Evil should win' );
goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') #  == 'Battle Result: Good triumphs over Evil', 'Good should win' );
goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') #== 'Battle Result: No victor on this battle field', 'Should be a tie' );   