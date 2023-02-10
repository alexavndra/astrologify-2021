# setup.py file provided by Jason Goodison
# https://github.com/JasonLeviGoodison/SpotifyToYoutubeMP3/commit/0d658a24f8d2887d0e771fe4e8045607a08cff2d

"""allows setup for app"""

from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]

setup(
    name='SpotifyToYoutubeMP3',
    version='1.0',
    description='An application that gets your Spotify songs and downloads the YoutubeMP3 version',
    author='Jason Goodison',
    author_email='jasongoodisondevelopment@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)