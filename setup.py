from setuptools import setup, find_packages

setup(
    name='planner',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'python-crontab',
    ],
    entry_points={
        'console_scripts': [
            'planner=planner.main:main',
        ],
    },
    data_files=[('config', ['planner.conf'])],
)