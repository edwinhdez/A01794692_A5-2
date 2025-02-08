import unittest
import subprocess
import os

class TestMain(unittest.TestCase):
    def setUp(self):
        # Ruta al archivo de prueba
        self.test_file = 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/ComputeStatistics/data/test_file.txt'
        
        # Crear el archivo de prueba si no existe
        if not os.path.exists(self.test_file):
            with open(self.test_file, 'w') as f:
                f.write('1\n2\n3\n4\n5\n')

    def tearDown(self):
        # Eliminar el archivo de prueba si es necesario
        # Comentado para evitar la eliminación del archivo de prueba
        # if os.path.exists(self.test_file):
        #     os.remove(self.test_file)
        pass

    def test_main(self):
        # Ejecutar el script computeStatistics.py con el archivo de prueba
        result = subprocess.run(['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/ComputeStatistics/src/compute_statistics.py', self.test_file], capture_output=True, text=True)
        output = result.stdout.strip()
        expected_output = (
            "Descriptive Statistics:\n"
            "Mean: 514.84\n"
            "Median: 504.0\n"
            "Mode: 59.0\n"
            "Variance: 81704.22440000014\n"
            "Standard Deviation: 285.8395081160058\n"
        )
        self.assertIn(expected_output, output)

    def test_file_not_found(self):
        # Ejecutar el script computeStatistics.py con un archivo inexistente
        result = subprocess.run(['python', 'C:/git/TecMonterrrey/QualitySoftware/A01794692_A4-2/ComputeStatistics/src/compute_statistics.py', 'non_existent_file.txt'], capture_output=True, text=True)
        output = result.stdout.strip()
        self.assertIn("Error: The file 'non_existent_file.txt' was not found.", output)

if __name__ == '__main__':
    unittest.main()