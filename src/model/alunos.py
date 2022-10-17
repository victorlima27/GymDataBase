from model.exercicios import Exercicios


class Alunos:
    def __init__(
        self,
        codigo_aluno: int = None,
        nome_aluno: str = None,
        cpf: str = None,
        pagamento: int = None,
        vencimento_mensalidade: str = None,
        telefone: str = None,
        codigo_exercicio: Exercicios = None,
    ):
        self.set_codigo_aluno(codigo_aluno)
        self.set_codigo_exercicio(codigo_exercicio)
        self.set_nome_aluno(nome_aluno)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_pagamento(pagamento)
        self.set_vencimento_mensalidade(vencimento_mensalidade)

    def set_codigo_aluno(self, codigo_aluno: int):
        self.set_codigo_aluno = codigo_aluno

    def set_nome_aluno(self, nome_aluno: str):
        self.set_nome_aluno = nome_aluno

    def set_cpf(self, cpf: str):
        self.set_cpf = cpf

    def set_telefone(self, telefone: str):
        self.set_telefone = telefone

    def set_pagamento(self, pagamento: int):
        self.pagamento = pagamento

    def set_vencimento_mensalidade(self, vencimento_mensalidade: str):
        self.set_vencimento_mensalidade = vencimento_mensalidade

    def set_codigo_exercicio(self, codigo_exercicio: Exercicios):
        self.set_codigo_exercicio = codigo_exercicio

    def get_codigo_aluno(self) -> int:
        return self.codigo_aluno

    def get_nome_aluno(self) -> str:
        return self.nome_aluno

    def get_cpf(self) -> str:
        return self.set_cpf

    def get_telefone(self) -> str:
        return self.telefone

    def get_pagamento(self) -> int:
        return self.pagamento

    def get_vencimento_mensalidade(self) -> str:
        return self.vencimento_mensalidade

    def get_codigo_exercicio(self) -> Exercicios:
        self.codigo_exercicio

    def to_string(self):
        return f"cod.aluno:{self.get_codigo_aluno()} | nome.aluno: {self.get_nome_aluno()} | cpf: {self.get_cpf()}| telefone:{self.get_telefone()} | pagamento:{self.get_pagamento()} | vencimento: {self.get_vencimento_mensalidade()} | cod.exercicio: {self.get_codigo_exercicio()}"
