class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assunto, corpo):
        for usuarios in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                usuarios.email,
                assunto,
                corpo,

)