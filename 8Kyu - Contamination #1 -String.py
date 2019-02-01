def contamination(text, char):
  #Code here ;)
  if(text == '' or char == ''):
      return ''
  else:
      l = len(text)
      result = l*char
      return result
      
