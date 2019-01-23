from setuptools import setup
setup(
    name='ose',
    version='0.6.0',
    description='Download Options DATA(NK255) from JPX',
    url='https://github.com/zaq9/ose',
    author='zaq',
    author_email='zaq_9@yahoo.co.jp',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
    ],
    keywords=['options','market-data','python','finance'],
    install_requires=['pandas'],
)
