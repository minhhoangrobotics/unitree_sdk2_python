from setuptools import setup, find_packages

setup(
    name='unitree_sdk2py',
    version='1.0.0',
    description='Unitree SDK2 python interface',
    long_description='',
    author='Unitree',
    author_email='support@unitree.com',
    url='https://github.com/unitreerobotics/unitree_sdk2_python',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
