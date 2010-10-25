from distutils.core import setup

setup(name='myname',
      version='0.1',
      description='Transforms emails into names',
      author='Fernando Takai',
      author_email='fernando@performable.com',
      maintainer='Performable',
      maintainer_email='fernando@performable.com',
      url='http://github.com/performable/python-myname',
      long_description='Easily transform an email into a user friendly name. A port of on myna-bird (http://github.com/wistia/myna_bird)',
      license="Public domain",
      packages=['myname'],
      package_dir = {'myname': 'myname'},
      platforms=['any'],
)
