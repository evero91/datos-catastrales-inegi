import csv

def nombre_sql(texto):
    return texto.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('.','').replace(',','')

with open('tablas_norma_tecnica.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    tabla = ''
    _tabla = ''
    campo = ''
    descripcion = ''
    tipo = ''
    obligatorio = ''
    tamano = ''
    create_table = ''
    comentario = ''
    _comentario_tabla = ''
    
    for row in csv_reader:
        tabla = '_'.join(nombre_sql(row[0].lower().strip().replace('\t',' ')).split())
        campo = row[1].lower().replace('\t',' ').strip()
        descripcion = row[2].replace('\t',' ').strip()
        tipo = row[4].lower().strip()
        obligatorio = row[6].lower().strip()
        tamano = row[7].strip()

        if tabla != '':
            if create_table != '':
                create_table = create_table[:-2] + '\n);\n\n' + comentario + '\n'
            
            create_table += f'CREATE TABLE {tabla} (\n'

            if row[8].strip() != '':
                _comentario_tabla = row[8].strip()

            comentario = f"COMMENT ON TABLE {tabla} IS '{_comentario_tabla}';\n"
            _tabla = tabla

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
        comentario += f"COMMENT ON COLUMN {_tabla}.{campo} IS '{descripcion}';\n"

    create_table = create_table[:-2] + '\n);\n\n' + comentario + '\n'

with open('create_table.sql', 'w', newline='', encoding='utf-8') as archivo:
    archivo.write(create_table)
    archivo.close()
    print('Archivo create_table.sql creado')

# print(create_table)