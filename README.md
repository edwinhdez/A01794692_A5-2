# Compute Sales

Este proyecto es una herramienta para calcular las ventas totales y generar un informe detallado de las ventas a partir de un catálogo de productos y un registro de ventas.

## Requisitos

- Python 3.10
- Poetry

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/edwinhdez/A01794692_A5-2.git
    cd compute_sales
    ```

2. Instala las dependencias usando Poetry:

    ```sh
    poetry install
    ```

## Uso

### Ejecutar el programa

Para ejecutar el programa, puedes usar los paths por defecto o proporcionar tus propios paths para los archivos de catálogo y ventas:

```sh
python3 ComputeSales\src\computeSales.py
```

### O proporcionando los paths:
```sh 
python3 ComputeSales\src\computeSales.py path/to/catalogue.json path/to/sales_records.json
```
### Ejecutar las pruebas
Para ejecutar las pruebas unitarias, usa el siguiente comando:

```sh
python3 ComputeSales\test\test_compuet_sales.py
```

### Ejecutar flake8
Para verificar el cumplimiento con PEP8 usando flake8, ejecuta el siguiente comando:

``` sh
python3 ComputeSales\src\utils\run_flake8.py
``` 

## Conclusiones
Después de usar flake8 para validar el código, se encontraron y corrigieron varios problemas de estilo, incluyendo:

- Líneas demasiado largas.
- Líneas en blanco incorrectas.
- Comentarios de bloque que no comenzaban con # .
- Falta de nuevas líneas al final de los archivos.
- Todos estos problemas fueron corregidos para asegurar que el código cumple con las convenciones de estilo de PEP8. Ahora, flake8 no encuentra ningún problema en el código:

``` sh
No issues found by flake8.
``` 

## Estructura del Proyecto
``` sh
.
├── ComputeSales
│   ├── data
│   │   ├── catalogue.json
│   │   ├── sales_records.json
│   │   └── SalesResults.txt
│   ├── flake8_reports
│   │   └── flake8_issues_YYYYMMDD_HHMMSS.txt
│   ├── src
│   │   ├── computeSales.py
│   │   └── utils
│   │       └── run_flake8.py
│   └── tests
│       └── test_compute_sales.py
├── pyproject.toml
└── README.md
```
## Autor
Edwin Hernandez - A01794692@tec.mx