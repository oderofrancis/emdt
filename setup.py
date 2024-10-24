from setuptools import setup, find_packages

setup(
    name='edmt',  # Replace with your package name
    version='1.0',          # Initial version
    author='Odero & Kuloba',
    author_email='francisodero10@gmail.com',
    description='Environmental Data Management Toolbox',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oderofrancis/emdt.git',  # Replace with your repo URL
    packages=find_packages(),  # Automatically find packages in your repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust as needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python versions supported
    install_requires=[
        'certifi==2024.8.30',
        'geopandas==1.0.1',
        'numpy==2.1.2',
        'packaging==24.1',
        'pandas==2.2.3',
        'pyogrio==0.10.0',
        'pyproj==3.7.0',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.2',
        'shapely==2.0.6',
        'six==1.16.0',
        'tqdm==4.66.5',
        'tzdata==2024.2',
    ],
)
