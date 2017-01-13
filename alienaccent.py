def convert(st):
  
    for i in st:
      if i == 'o':
        st = st.replace('o', 'u')
      elif i == 'a':
        st = st.replace('a', 'o')
 
    return st
