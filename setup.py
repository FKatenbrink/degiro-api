from setuptools import setup, find_packages

setup(name='degiro-api',
      version='0.10004',
      description='An unofficial DeGiro API wrapper for Python.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
      ],
      keywords='DeGiro API Wrapper',
      url='https://github.com/FKatenbrink/degiro-api',
      author='Florian Katenbrink',
      author_email='f.katenbrink@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'requests',
      ]
)
