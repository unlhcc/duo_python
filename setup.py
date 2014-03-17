from distutils.core import setup

setup(
    name='duo_web_python',
    version='1.1',
    description='Duo Web SDK for two-factor authentication',
    author='Duo Security, Inc.',
    author_email='support@duosecurity.com',
    url='https://github.com/duosecurity/duo_python',
    packages=['duo_web'],
    package_data={
        'duo_web': ['js/*.js'],
    },
    data_files=[
        ('js', [
                'js/Duo-Web-v1.bundled.js',
                'js/Duo-Web-v1.bundled.min.js',
                'js/Duo-Web-v1.js',
                'js/Duo-Web-v1.min.js',
        ]),
    ],
    license='BSD',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ],
)
