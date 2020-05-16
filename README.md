### Creating New Python Environment

I highly recommend using Homebrew and pyenv and following this article
for setting up your local environment:

    https://jacobian.org/2019/nov/11/python-environment-2020/


### Installing cyvcf2

Here are the steps for installing cyvcf2:

    $ python --version
    Python 3.7.5

    $ python -m venv .venv
    $ source .venv/bin/activate

    $ export LDFLAGS="-L/usr/local/opt/openssl/lib"
    $ export CPPFLAGS="-I/usr/local/opt/openssl/include"
    $ pip install cyvcf2

    $ pip freeze
    click==7.1.2
    coloredlogs==14.0
    cyvcf2==0.20.0
    humanfriendly==8.2
    numpy==1.18.4
    
    
### Installing tabulate

Here are the steps for installing tabulate:

    $ pip install tabulate
    
### Running code

Now you can run the code:

    $ python run_me.py

