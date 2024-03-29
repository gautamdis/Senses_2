from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A simple python library to wish, listen and speak'

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
    name="Senses_2",
    version=VERSION,
    author="Gautam Yadav",
    author_email="gautamdiscoder@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/gautamdis/Senses_2",
    packages=find_packages(),
    install_requires=['pyttsx3','SpeechRecognition','datetime'],
    py_modules=['Senses_2'],
    python_requires='>=3.6',
    package_dir={'': 'src'},
    keywords=['Senses_2', 'senses_2', 'speaking', 'listening', 'wishing', 'python', 'python3', 'jarvis', 'siri', 'alexa', 'google assistant', 'voice', 'voice assistant', 'voice recognition', 'speech recognition', 'text to speech', 'speech to text', 'Gautam Yadav', 'Gautam', 'Yadav', 'gautamdiscoder'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
