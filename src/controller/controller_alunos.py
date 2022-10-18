from model.alunos import Alunos
from conexion.oracle_queries import OracleQueries


class Controller_Alunos:
    def __init__(self):
        pass

    def cadastrar_aluno(self) -> Alunos:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cursor = oracle.connect()

        cpf = input("CPF(Novo): ")

        data = dict(nome_aluno=nome, cpf=cpf)
        cursor.execute("""
        begin
            :codigo := ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL;
            insert into alunos values(:nome_aluno, :cpf);
        end;
        """, data)

        if self.verifica_existencia_aluno(oracle, cpf):
            nome = input("Nome (Novo): ")
            oracle.write(f"inset into alunos values ('{cpf}', '{nome}')")

            df_aluno = oracle.sqlToDataFrame(
                f"select cpf, nome_aluno from alunos where cpf = '{cpf}'")
            novo_aluno = Alunos(df_aluno.cpf.values[0],df_aluno.nome.values[0])
            print(novo_aluno.to_string())
            return novo_aluno
        else:
            print(f"O CPF {cpf} não existe.")
            return None
    



    def excluir_aluno(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_alunos(oracle, need_connect=True)
        cpf = int(input("CPF do aluno a ser excluído: "))

        if not self.verifica_existencia_aluno(oracle, cpf):
            df_aluno = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
            oracle.write(f"delete from alunos where cpf = {cpf}")
            aluno_excluido = Alunos(df_aluno.cpf.values[0], df_aluno.nome.values[0])
            print("Aluno removido com sucesso!")
            print(aluno_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_aluno(self,oracle: OracleQueries,cpf: str = None) -> bool:
        df_aluno = oracle.sqlToDataFrame(f"select cpf, nome_aluno from alunos where cpf = {cpf} f")
        return df_aluno.empty


    def listar_alunos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select a.cpf
                    , a.nome_aluno 
                from alunos a
                order by a.nome_aluno
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))