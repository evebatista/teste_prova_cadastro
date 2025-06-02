import unittest
from app.usuarios import cadastrar_usuario

class TestIntegracao(unittest.TestCase):
    def test_cadastro_com_email_valido(self):
        usuario = cadastrar_usuario("Maria", "maria@exemplo.com")
        self.assertEqual(usuario["email"], "maria@exemplo.com")
