import csv

with open('tablas_norma_tecnica.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    tabla = ""
    campo = ""
    descripcion = ""
    tipo = ""
    obligatorio = ""
    tamano = ""
    n = 0
    
    for row in csv_reader:
        tabla = row[0].lower().replace('\t',' ')
        campo = row[1].lower().replace('\t',' ')
        descripcion = row[2].replace('\t',' ')
        tipo = row[4].lower()
        obligatorio = row[6].lower()
        tamano = row[7]

        print(tabla, campo, descripcion, tipo, obligatorio, tamano)
        n += 1

        if n == 4:
            exit()
