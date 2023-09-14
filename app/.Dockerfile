FROM python:3.10.12-bookworm

RUN pip3 install ipykernel
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install scikit-learn
RUN pip3 install seaborn
RUN pip3 install ppscore
RUN pip3 install dash
RUN pip3 install dash_bootstrap_components
RUN pip3 install mlflow

WORKDIR /root/code

CMD tail -f /dev/null