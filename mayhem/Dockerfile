FROM fuzzers/atheris:2.0.7-python3.9

RUN pip install parsy
COPY . /src
WORKDIR /src
RUN chmod +x /src/mayhem/fuzz_parsy.py
CMD ["/src/mayhem/fuzz_parsy.py"]
