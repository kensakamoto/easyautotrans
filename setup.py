from setuptools import setup, find_packages

setup(
    name="easyautotrans",
    packages=find_packages(),
    install_requires=[
        "pyperclip",
        "googletrans"
    ],
    entry_points={
        "console_scripts": [
            "easy-auto-trans = easyautotrans.easyautotrans:main"
        ]
    }
)