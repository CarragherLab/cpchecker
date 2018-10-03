from setuptools import setup

setup(name="cpchecker",
      version=0.1,
      packages=["cpchecker"],
      entry_points={
          "console_scripts": ["cpchecker = cpchecker.__main__:main"]
      },
      install_requires=["pyyaml"])
