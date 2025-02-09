import unittest
import subprocess
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        # Rutas a los archivos de prueba
        self.catalogue_file = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A5-2/ComputeSales/data/catalogue.json'
        self.sales_file = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A5-2/ComputeSales/data/sales_records.json'
        self.results_file = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A5-2/ComputeSales/data/SalesResults.txt'

        # Crear los archivos de prueba si no existen
        if not os.path.exists(self.catalogue_file):
            with open(self.catalogue_file, 'w') as f:
                f.write('{"product1": 10.0, "product2": 20.0, "product3": 30.0}')

        if not os.path.exists(self.sales_file):
            with open(self.sales_file, 'w') as f:
                f.write('[{"product": "product1", "quantity": 2}, '
                        '{"product": "product2", "quantity": 1}, '
                        '{"product": "product3", "quantity": 3}]')

    def tearDown(self):
        # Eliminar el archivo de resultados si es necesario
        if os.path.exists(self.results_file):
            os.remove(self.results_file)

    def test_main(self):
        # Ejecutar el script compute_sales.py con los archivos de prueba
        result = subprocess.run(
            ['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A5-2/ComputeSales/src/computeSales.py',
             self.catalogue_file, self.sales_file],
            capture_output=True, text=True
        )
        output = result.stdout.strip()

        # Ignorar las líneas de carga de archivos
        output_lines = output.split('\n')
        relevant_output = '\n'.join(output_lines[2:])

        expected_output = (
            "Sales Summary Report\n"
            "====================\n"
            "Total Sales: $130.00\n\n"
            "Details:\n"
            "Product: product1\n"
            "  Quantity: 2\n"
            "  Unit Price: $10.00\n"
            "  Total Price: $20.00\n\n"
            "Product: product2\n"
            "  Quantity: 1\n"
            "  Unit Price: $20.00\n"
            "  Total Price: $20.00\n\n"
            "Product: product3\n"
            "  Quantity: 3\n"
            "  Unit Price: $30.00\n"
            "  Total Price: $90.00\n\n"
            "Time elapsed: 0.00 seconds\n\n"
        )

        # Comparar las líneas individuales de la salida esperada y la salida real
        expected_lines = expected_output.strip().split('\n')
        relevant_lines = relevant_output.strip().split('\n')
        self.assertEqual(expected_lines, relevant_lines)

    def test_file_not_found(self):
        # Ejecutar el script compute_sales.py con un archivo inexistente
        result = subprocess.run(
            ['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A5-2/ComputeSales/src/computeSales.py',
             'non_existent_catalogue.json', 'non_existent_sales.json'],
            capture_output=True, text=True
        )
        output = result.stdout.strip()
        self.assertIn("Error loading catalogue", output)


if __name__ == '__main__':
    unittest.main()
