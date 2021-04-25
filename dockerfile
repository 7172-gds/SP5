FROM debian 
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install python3
COPY sp5_2.py .
CMD python3 sp5_2.py
