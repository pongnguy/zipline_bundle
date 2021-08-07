FROM ubuntu:20.10

ENV DEBIAN_FRONTEND=noninteractive

RUN --mount=type=cache,target=/var/cache/apt \
    apt update && \
    apt upgrade -y
#RUN --mount=type=cache,target=/var/cache/apt \
#    apt install -y python3-pip

#ENV LOCAL=/home/alfred

COPY ../download/Miniconda3-latest-Linux-x86_64.sh '/root/Downloads/'
RUN chmod +x /root/Downloads/Miniconda3-latest-Linux-x86_64.sh && \
    /root/Downloads/Miniconda3-latest-Linux-x86_64.sh -b -p /root/miniconda

RUN /root/miniconda/bin/conda create -n condaenv python=3.6 -y

RUN --mount=type=cache,target=/root/.cache/pip \
    /root/miniconda/envs/condaenv/bin/pip3 install pandas pyfolio
#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install backtrader

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install pandas numpy

RUN --mount=type=cache,target=/root/.cache/pip \
    /root/miniconda/envs/condaenv/bin/pip3 install "requests>2,<3" "urllib3>1.24,<2" "websocket-client>=0.56.0,<1" "websockets>=8.0,<9"

RUN --mount=type=cache,target=/root/.cache/pip \
    /root/miniconda/envs/condaenv/bin/pip3 install torch torchvision torchaudio

RUN --mount=type=cache,target=/root/.cache/pip \
    /root/miniconda/envs/condaenv/bin/pip3 install jupyterlab

RUN --mount=type=cache,target=/root/.cache/pip \
    /root/miniconda/envs/condaenv/bin/pip3 install flake8 pytest-runner

# This works, but relies on an experimental "run" command in conda
RUN --mount=type=cache,target=/root/miniconda/pkgs \
    --mount=type=cache,target=/root/.conda/pkgs \
    /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda install -c conda-forge bcolz -y"

RUN --mount=type=cache,target=/root/miniconda/pkgs \
    --mount=type=cache,target=/root/.conda/pkgs \
    /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda install -c quantopian zipline"



#RUN --mount=type=cache,target=/var/cache/apt \
#    apt-get install -y build-essential

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install bottleneck

#RUN /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda install -y pandas numpy"

#RUN /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda install -c quantopian ta-lib"

#RUN /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda install -c quantopian logbook"

#RUN --mount=type=cache,target=/root/miniconda/pkgs \
#    --mount=type=cache,target=/root/.conda/pkgs \
#    /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda uninstall pandas numpy scipy " \

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install --force-reinstall numpy==1.19.4

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install pandas==1.1.5 scipy==1.5.4

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install alpaca-trade-api

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install --upgrade pip setuptools wheel

#RUN --mount=type=cache,target=/var/cache/apt \
#    apt install -y git

#RUN git clone https://github.com/quantopian/zipline /root/Downloads/zipline

#RUN /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda install conda-build"

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install ta-lib

#RUN cd /root/Downloads/zipline/conda && \
#    /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda build ta-lib"

#RUN cd /root/Downloads/zipline/conda && \
#    /root/miniconda/bin/conda run -n condaenv /bin/bash -c "conda build logbook zipline"

#RUN --mount=type=cache,target=/root/.cache/pip \
#    /root/miniconda/envs/condaenv/bin/pip3 install zipline
