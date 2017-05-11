def whoseMove(lastPlayer, win):
      if win == True:
        if lastPlayer == 'black':
          return 'black'
        else:
          return 'white'
      else:
        if lastPlayer == 'white':
          return 'black'
        else:
          return 'white'
		  
		  