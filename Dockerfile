# Käytetään Python 3.10 -pohjakuvaa
FROM python:3.10

# Työhakemisto kontissa
WORKDIR /app

# Kopioidaan riippuvuudet
COPY requirements.txt .

# Asennetaan riippuvuudet
RUN pip install --no-cache-dir -r requirements.txt

# Kopioidaan ohjelma konttiin
COPY ./src/ .
COPY entrypoint.sh .
COPY .pylintrc .

# Tehdään datadirectory tietokannalle
#RUN mkdir -p data

# Tehdään testiraporteille directory
#RUN mkdir -p reports

# Tehdään entrypointin valintaskriptistä ajettava
RUN chmod +x entrypoint.sh

# Määritellään käynnistyskomento
ENTRYPOINT ["./entrypoint.sh"]