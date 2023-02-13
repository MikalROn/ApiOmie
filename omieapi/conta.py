from omieapi.omie import Omie


class Conta(Omie):
    """ Classe que possui todos os metodos ralacionados a contas correntes no Omie """
    def _chamada_api_conta(self, call: str = '', param: dict | tuple | list = None) -> dict:
        """ Metodo feito para carregar o endpoint padrão da classe """
        return self._chamar_api(
            endpoint='geral/contacorrente/',
            call=call,
            param=param
        )

    def listar_contas_correntes(
            self, pagina: int, registros_por_pagina: int, apenas_importado_api: bool
    ) -> dict:
        """
        :param pagina:                          integer	Número da página que será listada.
        :param registros_por_pagina:            integer	Número de registros retornados
        :param apenas_importado_api:            Bool	Tipo de Cartão para Administradoras de Cartão.
        """
        apenas_importado_api = self._bool_para_sn(apenas_importado_api)
        return self._chamada_api_conta(
            call='ListarContasCorrentes',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api
            }
        )

    def incluir_conta_corrente(
            self, cCodCCInt: int, tipo_conta_corrente: str,
            codigo_banco: str, descricao: str, saldo_inicial: float
    ) -> dict:
        """
        :param cCodCCInt:                           integer	Código da conta corrente no Omie.
        :param tipo_conta_corrente:                 string2	Tipo da Conta Corrente.
        :param codigo_banco:                        string3	Código do banco
        :param descricao:                           string40	Descrição da conta corrente.
        :param saldo_inicial:                       decimal	Saldo Inicial da Conta Corrente
        """
        resposta = self._chamada_api_conta(
            call='IncluirContaCorrente',
            param={
                "cCodCCInt": cCodCCInt,
                "tipo_conta_corrente": tipo_conta_corrente,
                "codigo_banco": codigo_banco,
                "descricao": descricao,
                "saldo_inicial": saldo_inicial
            }
        )
        return resposta

    def excluir_conta_corrente(
            self, nCodCC: int, cCodCCInt: str
    ) -> dict:
        """
        :param nCodCC:          integer	Código da conta corrente no Omie.
        :param cCodCCInt:       string20	Código de Integração do Parceiro.
        """
        return self._chamada_api_conta(
            call='ExcluirContaCorrente',
            param={
                    "nCodCC": nCodCC,
                    "cCodCCInt": cCodCCInt
            }
        )

    def consultar_conta_corrente(
            self, nCodCC: int, cCodCCInt: str
    ) -> dict:
        """
        :param nCodCC:          integer	Código da conta corrente no Omie.
        :param cCodCCInt:       string20	Código de Integração do Parceiro.
        """
        return self._chamada_api_conta(
            call='ConsultarContaCorrente',
            param={
                "nCodCC": nCodCC,
                "cCodCCInt": cCodCCInt
            }
        )

    def lista_resumo_contas_correntes(
            self, pagina: int, registros_por_pagina: int, apenas_importado_api: bool
    ) -> dict:
        """
        :param pagina:                          integer	Número da página que será listada.
        :param registros_por_pagina:            integer	Número de registros retornados
        :param apenas_importado_api:            Bool	Tipo de Cartão para Administradoras de Cartão.
        """
        return self._chamada_api_conta(
            call='ListarResumoContasCorrentes',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api
            }
        )

    def alterar_conta_corrente(
            self, cCodCCInt: int, tipo_conta_corrente: str, codigo_banco: str, descricao: str, saldo_inicial: float
    ) -> dict:
        """
        :param cCodCCInt:                           integer	Código da conta corrente no Omie.
        :param tipo_conta_corrente:                 string2	Tipo da Conta Corrente.
        :param codigo_banco:                        string3	Código do banco
        :param descricao:                           string40	Descrição da conta corrente.
        :param saldo_inicial:                       decimal	Saldo Inicial da Conta Corrente
        """
        return self._chamada_api_conta(
            call='AlterarContaCorrente',
            param={
                "cCodCCInt": cCodCCInt,
                "tipo_conta_corrente": tipo_conta_corrente,
                "codigo_banco": codigo_banco,
                "descricao": descricao,
                "saldo_inicial": saldo_inicial
            }
        )

    def pesquisa_conta_corrente(
            self, pagina: int, registros_por_pagina: int, apenas_importado_api: bool
    ) -> dict:
        """
        :param pagina:                          integer	Número da página que será listada.
        :param registros_por_pagina:            integer	Número de registros retornados
        :param apenas_importado_api:            Bool	Tipo de Cartão para Administradoras de Cartão.
        """
        apenas_importado_api = self._bool_para_sn(apenas_importado_api)
        return self._chamada_api_conta(
            call='PesquisarContaCorrente',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api
            }
        )

    def lancamento_em_cc(
            self, metodo: str, cCodIntLanc: str, nCodCC: int, dDtLanc: str, nValorLanc: float,
            cCodCateg: str, cTipo: str,  nCodCliente: str, cObs: str
    ) -> dict:
        """
        :param metodo:        IncluirLancCC or AlterarLancCC    Um altera o outro inclui novas informações
        :param cCodIntLanc:                         string20	Código da categoria
        :param nCodCC:                              integer	    Código da conta corrente.
        :param dDtLanc:                             string10	Data do lançamento na conta corrente.
        :param nValorLanc:                          decimal	    Valor do lançamento
        :param cCodCateg:                           string20	Código da categoria
        :param cTipo:                               string5	    Tipo de documento.
        :param nCodCliente:                         integer	    Código de Cliente / Favorecido.
        :param cObs:                                text	    Observações.
        """
        self._gerencia_metodo(['IncluirLancCC', 'AlterarLancCC'], metodo)
        return self._chamar_api(
                call=metodo,
                endpoint='financias/contacorentelancamento',
                param={
                    "cCodIntLanc": cCodIntLanc,
                    "cabecalho": {
                        "nCodCC": nCodCC,
                        "dDtLanc": dDtLanc,
                        "nValorLanc": nValorLanc
                    }, "detalhes": {
                        "cCodCateg": cCodCateg,
                        "cTipo": cTipo,
                        "nCodCliente": nCodCliente,
                        "cObs": cObs}
                }
            )

    def consulta_e_exclui_lancamento(
            self, metodo: str,  nCodLanc: str, cCodIntLanc: int
    ) -> dict:
        """
        :param metodo:          ExcluirLancCC or ConsultaLancCC     Um cancela o outro exclui lançamentos
        :param nCodLanc:        string40	                        Identificação do lançamento do extrato importado
        :param cCodIntLanc:     string20	                        Código do lançamento da conta corrente
        """
        self._gerencia_metodo(['ExcluirLancCC' , 'ConsultaLancCC'], metodo)
        return self._chamar_api(
            call=metodo,
            endpoint='financas/contacorrentelancamentos',
            param={
                "nCodLanc": nCodLanc,
                "cCodIntLanc": cCodIntLanc
            }
        )
