"""
Directory Forms API client
"""
from setuptools import find_packages, setup

setup(
    name='directory_forms_api_client',
    version='7.5.5',
    url='https://github.com/uktrade/directory-forms-api-client',
    license='MIT',
    author='Department for International Trade',
    description='Python API client for Directory forms .',
    packages=find_packages(exclude=['tests.*', 'tests']),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'directory_client_core>=7.2.12,<8.0.0',
    ],
    extras_require={
        'test': [
            'django>=4.2.10,<5.0',
            'flake8',
            'pytest-codecov',
            'pytest-cov',
            'GitPython',
            'pytest-django==3.10.0',
            'pytest',
            'requests>=2.22.0,<3.0.0',
            'requests_mock==1.8.0',
            'setuptools',
            'twine',
            'wheel>=0.34.2,<1.0.0',
            'psycopg2',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
