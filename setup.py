from distutils.core import setup

setup(
    name='duo-web-python',
    version='1.2.0',
    description='Duo Web SDK for two-factor authentication',
    author='Duo Security, Inc.',
    author_email='support@duosecurity.com',
    url='https://github.com/duosecurity/duo_python',
    packages=['duo_web'],
    package_data={
        'duo_web': ['js/*.js'],
    },
    data_files=[
        ('share/javascript/duo', [
	    'js/Duo-Web-v2.js',
            'js/Duo-Web-v2.min.js',
        ]),
       ('/etc/httpd/conf.d',['conf/duo-js.conf']),
       ('/etc/duo',['conf/duo_web.conf']),
    ],
    license='BSD',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ],
)
