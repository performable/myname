import re

COMMON_LOCALS = ('support', 'info', 'sales', 'marketing', 'admin', 'webmaster', 'help',)
COMMON_DOMAINS = ('hotmail','msn','live','yahoo','yahoo.co.uk','ymail','rocketmail','gmail','googlemail','aol',
'fastmail.fm','web','mail.ru','rediff','indiatimes','lycos','libero.it','rambler.ru','mac',
'paracalls','linkedin','mynet','interia.pl','yandex.ru','sina','126','lycos','bol','in','me',
'voila.fr','mail','comcast','netcom','roadrunner','verizon','1and1','att','adelphia',
'bigpond','bluebottle','blueyonder','btopenworld','charter','cox','earthlink','sbc','telus',
'mailinator','charter','rogers','sympatico','tiscali', re.compile(r'\.edu$'))

class MyName(object):

  def __init__(self, email):
    if email:
      self.email = email.lower()
      self.local, self.domain = self.email.split('@')
    else:
      self.email = ''
      self.local = ''
      self.domain = ''

  @staticmethod
  def convert(cls, email):
    return cls(email).name

  def nameize(self, str):
    if str:
      name = str.lower()
      name = re.sub(r'[^a-z0-9]+', '-', name)
      name = re.sub(r'\-$', '', name)
      name = re.sub(r'^\-', '', name)
      return name
    else:
      return ''

  def names(self):
    if self.is_common_domain:
      yield self.local_name
    else:
      yield self.domain_name

    yield self.local_name + '-at-' + self.domain_name

  def name(self):
    if self.is_common_local and self.is_common_domain:
      return self.local_name + '-at-' + self.domain_name
    elif self.is_common_local:
      return self.domain_name
    elif self.is_common_domain:
      return self.local_name
    else:
      return self.domain_name

  @property
  def domain_name(self):
    hosts = self.domain.split('.')
    just_the_host = hosts[0] if hosts else ''
    return self.nameize(just_the_host)
    
  @property
  def local_name(self):
    local_sans_alias = re.sub(r'\+.*$', '', self.local)
    return self.nameize(local_sans_alias)

  @property
  def is_common_domain(self):
    for domain in COMMON_DOMAINS:
      if hasattr(domain, 'match'):
        if domain.search(self.domain):
          return True
      else:
        if re.match(r'^%s\.' % domain, self.domain):
          return True

  @property
  def is_common_local(self):
    for local in COMMON_LOCALS:
      if hasattr(local, 'match'):
        if local.search(self.local):
          return True
      else:
        if local == self.local:
          return True
