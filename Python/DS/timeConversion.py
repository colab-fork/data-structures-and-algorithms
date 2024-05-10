def timeConversion(s):
    m = s[-2:]
    s = s[:-2]
    s =s.split(':')
    if m == 'PM':
        if s[0] != '12':
            s[0] = str(int(s[0]) + 12)
    else:
        if s[0] == '12':
            s[0] = '00'
        
    ret = ':'.join(s)
    return ret

  
  """
  >>> %Run -c $EDITOR_CONTENT
01:01:00
>>> 
  
  """
