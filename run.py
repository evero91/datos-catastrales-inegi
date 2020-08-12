import csv

def nombre_sql(texto):
    return texto.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('.','').replace(',','').replace('\t',' ')

with open('tablas_norma_tecnica.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    tabla = ""
    campo = ""
    descripcion = ""
    tipo = ""
    obligatorio = ""
    tamano = ""
    create_table = ""
    n = 0
    
    for row in csv_reader:
        tabla = '_'.join(nombre_sql(row[0].lower().strip()).split())
        campo = row[1].lower().replace('\t',' ').strip()
        descripcion = row[2].replace('\t',' ').strip()
        tipo = row[4].lower().strip()
        obligatorio = row[6].lower().strip()
        tamano = row[7].strip()

        if tabla != '':
            # QUITAR ULTIMA \n Y COMA
            # CERRAR CREATE TABLE ) Y PONER ; \n
            # ESCRIBIR CREATE TABLE EN ARCHIVO
            print(create_table)
            create_table = f'CREATE TABLE {tabla} (\n'

        # AGREGAR COLUMNA A CREATE TABLE
        if tipo.startswith('alfa'):
            create_table += f'{campo} VARCHAR({tamano})'
        elif tipo.startswith('num'):
            if ',' in tamano:
                create_table += f'{campo} DECIMAL({tamano})'
            else:
                create_table += f'{campo} INTEGER'
        else:
            create_table += f'{campo} DATE'

        if obligatorio.startswith('obli'):
            create_table += ' NOT NULL'
            
        create_table += ',\n'
        n += 1

        if n == 80:
            exit()
