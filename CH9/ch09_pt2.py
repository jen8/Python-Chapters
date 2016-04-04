def replace(s, old, new):
        """
          >>> replace('Mississippi', 'i', 'I')
          'MIssIssIppI'
          >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
          >>> replace(s, 'om', 'am')
          'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
          >>> replace(s, 'o', 'a')
          'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
        """
        s.split(s,old)
        s.join(s,new)
        return s           



if __name__ == '__main__':
    import doctest
    doctest.testmod()