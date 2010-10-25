import unittest
from myname import MyName

class TestMyName(unittest.TestCase):
  def assert_convert_name(self, from_email, to):
    self.assertEquals(MyName(from_email).name(), to)

  def assert_convert_names(self, from_email, result):
    values = MyName(from_email).names()
    for value in values:
      assert value in result

  def test_myname(self):
    self.assert_convert_name('fernando@performable.com', 'performable')
    self.assert_convert_name('fernando.takai@gmail.com', 'fernando-takai')
    self.assert_convert_name('support@gmail.com', 'support-at-gmail')
    self.assert_convert_name('fernando....takai@gmail.com', 'fernando-takai')
    self.assert_convert_name('bts@alumni.brown.edu', 'bts')
    self.assert_convert_name('claire@megacorp.co.uk', 'megacorp')
    self.assert_convert_name('fernando19@aol.com', 'fernando19')
    self.assert_convert_name('fernando.@aol.com', 'fernando')
    self.assert_convert_name('.fernando@aol.com', 'fernando')
    self.assert_convert_name('FERNANDO@aol.com', 'fernando')
    self.assert_convert_name('fernando@PERFORMABLE.COM', 'performable')

    self.assert_convert_names('fernando@performable.com', ['performable', 'fernando-at-performable'])
    self.assert_convert_names('fernando.takai@gmail.com', ['fernando-takai', 'fernando-takai-at-gmail'])
    self.assert_convert_names('support@gmail.com', ['support', 'support-at-gmail'])
