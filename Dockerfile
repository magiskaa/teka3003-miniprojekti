# Käytetään Python 3.10 -pohjakuvaa
FROM python:3.10

# Työhakemisto kontissa
WORKDIR /app

# Kopioidaan riippuvuudet
COPY requirements.txt .

# Asennetaan riippuvuudet
RUN pip install --no-cache-dir -r requirements.txt

# Kopioidaan ohjelma konttiin
COPY main.py .

# Määritellään käynnistyskomento
CMD ["python", "main.py"]