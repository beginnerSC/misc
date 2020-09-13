# hash:sha256:15bd804473628c9b209de89e052215c71c31bd37c0fd5a87e279721fbb2551f0
FROM registry.codeocean.com/codeocean/miniconda3:4.8.2-python3.8-ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN conda install -y \
        jupyterlab==2.2.6 \
        numpy==1.19.1 \
        pandas==1.1.1 \
        scipy==1.5.2 \
    && conda clean -ya
