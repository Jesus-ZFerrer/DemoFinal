FROM alpine:3.10   #this is which linux I will be using

RUN apk add --no-cache python3-dev \     # here I declare to install python
    && pip3 install --upgrade pip        # and also pip/update

WORKDIR /app      #here I create the folder /app

COPY .  /app      # Here copy all in actual directory in /app folder

RUN pip3 --no-cache-dir install -r requirements.txt  #Install all the modules required

CMD ["python3", "Testprueba.py"] #Correr el script de palindriome
 
    
