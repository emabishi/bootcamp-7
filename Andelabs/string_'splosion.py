'''
Study the pattern below and write your program to pass the tests

 phone  => pphphophonphone
 ab     => aab
 like   => lliliklike


 tests

 class TestStringSplosion(TestCase):

    """
        TestCases for String splosion lab
    """

    def test_string_splosion1(self):
        string_splosion = StringSplosion('Code')
        self.assertEqual(
            string_splosion.manipulate(),
            'CCoCodCode',
            msg='should manipulate the string'
        )

    def test_string_splosion2(self):
        string_splosion = StringSplosion('abc')
        self.assertEqual(
            string_splosion.manipulate(),
            'aababc',
            msg='should manipulate a second time'
        )

    def test_string_splosion3(self):
        string_splosion = StringSplosion('andela')
        self.assertEqual(
            string_splosion.manipulate(),
            'aanandandeandelandela',
            msg='should manipulate a third time'
        )

'''
class StringSplosion(str):
  
    def manipulate(str):
      result = ''
      for n in range(0,len(str)+1):
        result += str[:n]
      return result