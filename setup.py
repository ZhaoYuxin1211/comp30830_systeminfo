from setuptools import setup, find_packages

setup(
    name='sysinfo',
    version='0.1.0',
    packages=find_packages(include=['comp30830_systeminfo', 'comp30830_systeminfo.*']),
    entry_points={
        'console_scripts': ['sysinfo=systeminfo.systeminfo:main'],
    }
)
