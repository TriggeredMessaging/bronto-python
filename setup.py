import os
from setuptools import find_packages, setup

import bronto


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

VERSION = bronto.__version__
github_url = 'https://github.com/TriggeredMessaging/bronto-python'
requires = ['suds==0.4',
            'six']

setup(name='bronto-python',
      version=VERSION,
      author='Fresh Relevance',
      author_email='joshua.yeomans-gladwin@freshrelevance.com',
      license='Apache',
      url=github_url,
      download_url='%sarchive/%s.tar.gz' % (github_url, VERSION),
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      tests_require=requires + ['mock'],
      description='A python wrapper around Bronto\'s SOAP API',
      long_description=open('README.rst').read(),
      keywords=['bronto', 'soap', 'marketing'],
      classifiers=[
           'Development Status :: 4 - Beta',
           'Environment :: Web Environment',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: Apache Software License',
           'Natural Language :: English',
           'Operating System :: OS Independent',
           'Programming Language :: Python',
           'Programming Language :: Python :: 2.7',
      ]
)
