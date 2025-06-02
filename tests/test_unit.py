import unittest
from app.usuarios import validar_email, cadastrar_usuario

class TestUnitario(unittest.TestCase):
    def test_validar_email_valido(self):
        self.assertTrue(validar_email("teste@exemplo.com"))

    def test_validar_email_invalido(self):
        self.assertFalse(validar_email("testeexemplo.com"))

    def test_cadastrar_usuario_valido(self):
        usuario = cadastrar_usuario("João", "joao@email.com")
        self.assertEqual(usuario["nome"], "João")

    