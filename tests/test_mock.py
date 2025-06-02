import unittest
from unittest.mock import patch
from app import usuarios

class TestMock(unittest.TestCase):
    @patch("app.usuarios.validar_email")
    def test_cadastro_com_mock(self, mock_validar_email):
        mock_validar_email.return_value = True
        resultado = usuarios.cadastrar_usuario("Ana", "ana@teste.com")
        self.assertEqual(resultado["nome"], "Ana")
        mock_validar_email.assert_called_once()
