from omieapi.core.omiebase import OmieBase

# Aviso -> antes de usar confira se n�o a oq vc precisa j� feito no codigo principal,
# o codigo autogerdo pode conter erros n�o detectados ainda
class CodigoAutogerado(OmieBase):
    """ Este côdigo foi gerado de forma automatica por um script de scrap """     
    def alterar_cliente(self, **kargs) -> dict:
                """ Altera os dados do cliente """
                return self._chamar_api(
                    call= 'AlterarCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def associar_cod_int_cliente(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AssociarCodIntCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def consultar_cliente(self, **kargs) -> dict:
                """ Consulta os dados de um cliente """
                return self._chamar_api(
                    call= 'ConsultarCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def excluir_cliente(self, **kargs) -> dict:
                """ Exclui um cliente da base de dados. """
                return self._chamar_api(
                    call= 'ExcluirCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def incluir_cliente(self, **kargs) -> dict:
                """ Inclui o cliente no Omie """
                return self._chamar_api(
                    call= 'IncluirCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def incluir_clientes_por_lote(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'IncluirClientesPorLote',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def listar_clientes(self, **kargs) -> dict:
                """ Lista os clientes cadastrados """
                return self._chamar_api(
                    call= 'ListarClientes',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def listar_clientes_resumido(self, **kargs) -> dict:
                """ Realiza pesquisa dos clientes """
                return self._chamar_api(
                    call= 'ListarClientesResumido',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def upsert_cliente(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'UpsertCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def upsert_cliente_cpf_cnpj(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'UpsertClienteCpfCnpj',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def upsert_clientes_por_lote(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'UpsertClientesPorLote',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def alterar_caract_cliente(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def consultar_caract_cliente(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def excluir_caract_cliente(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def excluir_todas_caract_cliente(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirTodasCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def incluir_caract_cliente(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def excluir_tags(self, **kargs) -> dict:
                """ Remove tags associadas a um cliente. """
                return self._chamar_api(
                    call= 'ExcluirTags',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def excluir_todas(self, **kargs) -> dict:
                """ Remove todas as tags associadas a um cliente. """
                return self._chamar_api(
                    call= 'ExcluirTodas',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def incluir_tags(self, **kargs) -> dict:
                """ Associa tags a um cliente. """
                return self._chamar_api(
                    call= 'IncluirTags',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def listar_tags(self, **kargs) -> dict:
                """ Lista as tags de um determinado cliente. """
                return self._chamar_api(
                    call= 'ListarTags',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def alterar_projeto(self, **kargs) -> dict:
                """ Altera um projeto """
                return self._chamar_api(
                    call= 'AlterarProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def consultar_projeto(self, **kargs) -> dict:
                """ Consulta um projeto """
                return self._chamar_api(
                    call= 'ConsultarProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def excluir_projeto(self, **kargs) -> dict:
                """ Exclui um projeto """
                return self._chamar_api(
                    call= 'ExcluirProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def incluir_projeto(self, **kargs) -> dict:
                """ Inclui um novo projeto """
                return self._chamar_api(
                    call= 'IncluirProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def listar_projetos(self, **kargs) -> dict:
                """ Lista os projetos cadastrados """
                return self._chamar_api(
                    call= 'ListarProjetos',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def upsert_projeto(self, **kargs) -> dict:
                """ Inclui / Altera um projeto. """
                return self._chamar_api(
                    call= 'UpsertProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def consultar_empresa(self, **kargs) -> dict:
                """ Realiza a consulta de um registro especifico """
                return self._chamar_api(
                    call= 'ConsultarEmpresa',
                    endpoint= 'geral/empresas/',
                    param = kargs
                )
            
    def listar_empresas(self, **kargs) -> dict:
                """ Lista as empresas cadastradas no Omie. """
                return self._chamar_api(
                    call= 'ListarEmpresas',
                    endpoint= 'geral/empresas/',
                    param = kargs
                )
            
    def consultar_departamento(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarDepartamento',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def listar_depatartamentos(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'ListarDepatartamentos',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def consultar_categoria(self, **kargs) -> dict:
                """ Consulta uma categoria """
                return self._chamar_api(
                    call= 'ConsultarCategoria',
                    endpoint= 'geral/categorias/',
                    param = kargs
                )
            
    def listar_categorias(self, **kargs) -> dict:
                """ Lista as categorias cadastradas """
                return self._chamar_api(
                    call= 'ListarCategorias',
                    endpoint= 'geral/categorias/',
                    param = kargs
                )
            
    def listar_parcelas(self, **kargs) -> dict:
                """ Lista de Parcelas cadastradas. """
                return self._chamar_api(
                    call= 'ListarParcelas',
                    endpoint= 'geral/parcelas/',
                    param = kargs
                )
            
    def listar_tipo_ativ(self, **kargs) -> dict:
                """ Listar Tipos de Atividade. """
                return self._chamar_api(
                    call= 'ListarTipoAtiv',
                    endpoint= 'geral/tpativ/',
                    param = kargs
                )
            
    def listar_c_n_a_e(self, **kargs) -> dict:
                """ Listar os CNAEs cadastrados """
                return self._chamar_api(
                    call= 'ListarCNAE',
                    endpoint= 'produtos/cnae/',
                    param = kargs
                )
            
    def pesquisar_cidades(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'PesquisarCidades',
                    endpoint= 'geral/cidades/',
                    param = kargs
                )
            
    def listar_paises(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarPaises',
                    endpoint= 'geral/paises/',
                    param = kargs
                )
            
    def listar_tipos_anexos(self, **kargs) -> dict:
                """ Listagem de tipos de anexos. """
                return self._chamar_api(
                    call= 'ListarTiposAnexos',
                    endpoint= 'geral/tiposanexo/',
                    param = kargs
                )
            
    def incluir_anexo(self, **kargs) -> dict:
                """ Inclui o anexo para um documento. """
                return self._chamar_api(
                    call= 'IncluirAnexo',
                    endpoint= 'geral/anexo/',
                    param = kargs
                )
            
    def alterar_tipo_entrega(self, **kargs) -> dict:
                """ Alterar tipo de entrega """
                return self._chamar_api(
                    call= 'AlterarTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def consultar_tipo_entrega(self, **kargs) -> dict:
                """ Consultar tipo de entrega """
                return self._chamar_api(
                    call= 'ConsultarTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def excluir_tipo_entrega(self, **kargs) -> dict:
                """ Excluir tipo de entrega """
                return self._chamar_api(
                    call= 'ExcluirTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def incluir_tipo_entrega(self, **kargs) -> dict:
                """ Incluir tipo de entrega """
                return self._chamar_api(
                    call= 'IncluirTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def listar_tipo_entrega(self, **kargs) -> dict:
                """ Listar tipo de entrega """
                return self._chamar_api(
                    call= 'ListarTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def listar_tipo_assinante(self, **kargs) -> dict:
                """ Lista os tipos de assinante """
                return self._chamar_api(
                    call= 'ListarTipoAssinante',
                    endpoint= 'geral/tipoassinante/',
                    param = kargs
                )
            
    def listar_contas(self, **kargs) -> dict:
                """ Lista as contas do CRM. """
                return self._chamar_api(
                    call= 'ListarContas',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def verificar_conta(self, **kargs) -> dict:
                """ Verifica se uma conta foi criada a partir do nome e e-mail. """
                return self._chamar_api(
                    call= 'VerificarConta',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def alterar_caract_conta(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def consultar_caract_conta(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def excluir_caract_conta(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def excluir_todas_caract_conta(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirTodasCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def incluir_caract_conta(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def consultar_contato(self, **kargs) -> dict:
                """ Consulta o Contato """
                return self._chamar_api(
                    call= 'ConsultarContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def incluir_contato(self, **kargs) -> dict:
                """ Inclui um novo Contato """
                return self._chamar_api(
                    call= 'IncluirContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def listar_contatos(self, **kargs) -> dict:
                """ Lista os contatos do CRM. """
                return self._chamar_api(
                    call= 'ListarContatos',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def upsert_contato(self, **kargs) -> dict:
                """ Upsert do contato """
                return self._chamar_api(
                    call= 'UpsertContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def verificar_contato(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'VerificarContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def alterar_oportunidade(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def consultar_oportunidade(self, **kargs) -> dict:
                """ Consulta de oportunidade. """
                return self._chamar_api(
                    call= 'ConsultarOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def excluir_oportunidade(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def incluir_oportunidade(self, **kargs) -> dict:
                """ Incluir uma oportunidade. """
                return self._chamar_api(
                    call= 'IncluirOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def listar_oportunidades(self, **kargs) -> dict:
                """ Lista de oportunidades. """
                return self._chamar_api(
                    call= 'ListarOportunidades',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def upsert_oportunidade(self, **kargs) -> dict:
                """ Upsert de oportunidade. """
                return self._chamar_api(
                    call= 'UpsertOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def obter_lista_op(self, **kargs) -> dict:
                """ Lista de Oportunidades. """
                return self._chamar_api(
                    call= 'ObterListaOp',
                    endpoint= 'crm/oportunidades-resumo/',
                    param = kargs
                )
            
    def alterar_tarefa(self, **kargs) -> dict:
                """ Altera uma tarefa. """
                return self._chamar_api(
                    call= 'AlterarTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def calendario_tarefas(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'CalendarioTarefas',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def consultar_tarefa(self, **kargs) -> dict:
                """ Consulta uma tarefa da oportunidade. """
                return self._chamar_api(
                    call= 'ConsultarTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def excluir_tarefa(self, **kargs) -> dict:
                """ Exclui um tarefa. """
                return self._chamar_api(
                    call= 'ExcluirTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def incluir_tarefa(self, **kargs) -> dict:
                """ Inclui uma tarefa na oportunidade. """
                return self._chamar_api(
                    call= 'IncluirTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def listar_emails_tarefas(self, **kargs) -> dict:
                """ Lista os  emails tarefas. """
                return self._chamar_api(
                    call= 'ListarEmailsTarefas',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def listar_tarefas(self, **kargs) -> dict:
                """ Tarefas da oportunidade. """
                return self._chamar_api(
                    call= 'ListarTarefas',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def upsert_tarefa(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'UpsertTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def obter_detalhes_tarefa(self, **kargs) -> dict:
                """ Consulta os detalhes de uma tafera. """
                return self._chamar_api(
                    call= 'ObterDetalhesTarefa',
                    endpoint= 'crm/tarefas-resumo/',
                    param = kargs
                )
            
    def obter_lista_tarefas(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterListaTarefas',
                    endpoint= 'crm/tarefas-resumo/',
                    param = kargs
                )
            
    def obter_resumo_tarefas(self, **kargs) -> dict:
                """ Resumos das tarefas do CRM. """
                return self._chamar_api(
                    call= 'ObterResumoTarefas',
                    endpoint= 'crm/tarefas-resumo/',
                    param = kargs
                )
            
    def listar_solucoes(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarSolucoes',
                    endpoint= 'crm/solucoes/',
                    param = kargs
                )
            
    def listar_fases(self, **kargs) -> dict:
                """ Fases da Oportunidade """
                return self._chamar_api(
                    call= 'ListarFases',
                    endpoint= 'crm/fases/',
                    param = kargs
                )
            
    def listar_usuarios(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarUsuarios',
                    endpoint= 'crm/usuarios/',
                    param = kargs
                )
            
    def obter_usuarios(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterUsuarios',
                    endpoint= 'crm/usuarios/',
                    param = kargs
                )
            
    def listar_status(self, **kargs) -> dict:
                """ Status da oportunidade. """
                return self._chamar_api(
                    call= 'ListarStatus',
                    endpoint= 'crm/status/',
                    param = kargs
                )
            
    def listar_motivos(self, **kargs) -> dict:
                """ Motivos da oportunidade. """
                return self._chamar_api(
                    call= 'ListarMotivos',
                    endpoint= 'crm/motivos/',
                    param = kargs
                )
            
    def listar_tipos(self, **kargs) -> dict:
                """ Tipos de oportunidades. """
                return self._chamar_api(
                    call= 'ListarTipos',
                    endpoint= 'crm/tipos/',
                    param = kargs
                )
            
    def listar_parceiros(self, **kargs) -> dict:
                """ Parceiros e equipes da oportunidade. """
                return self._chamar_api(
                    call= 'ListarParceiros',
                    endpoint= 'crm/parceiros/',
                    param = kargs
                )
            
    def listar_finders(self, **kargs) -> dict:
                """ Finders da oportunidade. """
                return self._chamar_api(
                    call= 'ListarFinders',
                    endpoint= 'crm/finders/',
                    param = kargs
                )
            
    def listar_origens(self, **kargs) -> dict:
                """ Origens da oportunidade. """
                return self._chamar_api(
                    call= 'ListarOrigens',
                    endpoint= 'crm/origens/',
                    param = kargs
                )
            
    def listar_concorrentes(self, **kargs) -> dict:
                """ Concorrentes da oportunidade. """
                return self._chamar_api(
                    call= 'ListarConcorrentes',
                    endpoint= 'crm/concorrentes/',
                    param = kargs
                )
            
    def listar_verticais(self, **kargs) -> dict:
                """ Lista as verticais cadastradas. """
                return self._chamar_api(
                    call= 'ListarVerticais',
                    endpoint= 'crm/verticais/',
                    param = kargs
                )
            
    def alterar_vendedor(self, **kargs) -> dict:
                """ Altera os dados de um vendedor """
                return self._chamar_api(
                    call= 'AlterarVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def consultar_vendedor(self, **kargs) -> dict:
                """ Consulta os dados de um vendedor """
                return self._chamar_api(
                    call= 'ConsultarVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def excluir_vendedor(self, **kargs) -> dict:
                """ Exclui um vendedor """
                return self._chamar_api(
                    call= 'ExcluirVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def incluir_vendedor(self, **kargs) -> dict:
                """ Inclui um vendedor """
                return self._chamar_api(
                    call= 'IncluirVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def listar_vendedores(self, **kargs) -> dict:
                """ Listagem de Vendedores """
                return self._chamar_api(
                    call= 'ListarVendedores',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def upsert_vendedor(self, **kargs) -> dict:
                """ Inclui / Altera um vendedor """
                return self._chamar_api(
                    call= 'UpsertVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def consultar_tipo_tarefa(self, **kargs) -> dict:
                """ Consulta tipo de tarefa """
                return self._chamar_api(
                    call= 'ConsultarTipoTarefa',
                    endpoint= 'crm/tipostarefa/',
                    param = kargs
                )
            
    def excluir_tipo_tarefa(self, **kargs) -> dict:
                """ Excluir tipo de tarefa """
                return self._chamar_api(
                    call= 'ExcluirTipoTarefa',
                    endpoint= 'crm/tipostarefa/',
                    param = kargs
                )
            
    def listar_tipos_tarefa(self, **kargs) -> dict:
                """ Lista tipos de tarefa """
                return self._chamar_api(
                    call= 'ListarTiposTarefa',
                    endpoint= 'crm/tipostarefa/',
                    param = kargs
                )
            
    def alterar_conta_corrente(self, **kargs) -> dict:
                """ Altera a Conta Corrente """
                return self._chamar_api(
                    call= 'AlterarContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def consultar_conta_corrente(self, **kargs) -> dict:
                """ Realiza a consulta de uma conta corrente """
                return self._chamar_api(
                    call= 'ConsultarContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def excluir_conta_corrente(self, **kargs) -> dict:
                """ Excluir a Conta Corrente """
                return self._chamar_api(
                    call= 'ExcluirContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def incluir_conta_corrente(self, **kargs) -> dict:
                """ Inclui uma conta corrente """
                return self._chamar_api(
                    call= 'IncluirContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def listar_contas_correntes(self, **kargs) -> dict:
                """ Listar Contas Correntes """
                return self._chamar_api(
                    call= 'ListarContasCorrentes',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def listar_resumo_contas_correntes(self, **kargs) -> dict:
                """ Listar resumida de Contas correntes. """
                return self._chamar_api(
                    call= 'ListarResumoContasCorrentes',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def pesquisar_conta_corrente(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'PesquisarContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def upsert_conta_corrente(self, **kargs) -> dict:
                """ Upsert da Conta Corrente """
                return self._chamar_api(
                    call= 'UpsertContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def upsert_conta_corrente_por_lote(self, **kargs) -> dict:
                """ Upsert por lote de Conta Corrente """
                return self._chamar_api(
                    call= 'UpsertContaCorrentePorLote',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def alterar_lanc_c_c(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def consulta_lanc_c_c(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultaLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def excluir_lanc_c_c(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def incluir_lanc_c_c(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def listar_lanc_c_c(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def alterar_conta_pagar(self, **kargs) -> dict:
                """ Altera uma conta a pagar """
                return self._chamar_api(
                    call= 'AlterarContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def cancelar_pagamento(self, **kargs) -> dict:
                """ Cancela um pagamento realizado no Contas a Pagar """
                return self._chamar_api(
                    call= 'CancelarPagamento',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def consultar_conta_pagar(self, **kargs) -> dict:
                """ Consulta uma conta a pagar """
                return self._chamar_api(
                    call= 'ConsultarContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def excluir_conta_pagar(self, **kargs) -> dict:
                """ Exclui uma conta a pagar """
                return self._chamar_api(
                    call= 'ExcluirContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def incluir_conta_pagar(self, **kargs) -> dict:
                """ Inclui uma conta a Pagar. """
                return self._chamar_api(
                    call= 'IncluirContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def incluir_conta_pagar_por_lote(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirContaPagarPorLote',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def lancar_pagamento(self, **kargs) -> dict:
                """ Efetua a baixa de um pagamento do contas a pagar. """
                return self._chamar_api(
                    call= 'LancarPagamento',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def listar_contas_pagar(self, **kargs) -> dict:
                """ Listar as Contas a Pagar """
                return self._chamar_api(
                    call= 'ListarContasPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def upsert_conta_pagar(self, **kargs) -> dict:
                """ Upsert do Contas a Pagar """
                return self._chamar_api(
                    call= 'UpsertContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def upsert_conta_pagar_por_lote(self, **kargs) -> dict:
                """ Efetua o UPSERT do Contas a Pagar por Lote """
                return self._chamar_api(
                    call= 'UpsertContaPagarPorLote',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def alterar_conta_receber(self, **kargs) -> dict:
                """ Altera um conta a receber """
                return self._chamar_api(
                    call= 'AlterarContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def cancelar_conta_receber(self, **kargs) -> dict:
                """ Cancelamento do boleto gerado de uma conta a receber """
                return self._chamar_api(
                    call= 'CancelarContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def cancelar_recebimento(self, **kargs) -> dict:
                """ Efetua o cancelamento de um recebimento de Contas a Receber. """
                return self._chamar_api(
                    call= 'CancelarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def conciliar_recebimento(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConciliarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def consultar_conta_receber(self, **kargs) -> dict:
                """ Consulta uma Conta a Receber """
                return self._chamar_api(
                    call= 'ConsultarContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def desconciliar_recebimento(self, **kargs) -> dict:
                """ Desconciliar o Recebimento """
                return self._chamar_api(
                    call= 'DesconciliarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def excluir_conta_receber(self, **kargs) -> dict:
                """ Exclui uma conta a receber """
                return self._chamar_api(
                    call= 'ExcluirContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def incluir_conta_receber(self, **kargs) -> dict:
                """ Inclui uma conta a Receber """
                return self._chamar_api(
                    call= 'IncluirContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def incluir_conta_receber_por_lote(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirContaReceberPorLote',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def lancar_recebimento(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'LancarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def listar_contas_receber(self, **kargs) -> dict:
                """ Lista as contas a receber cadastradas. """
                return self._chamar_api(
                    call= 'ListarContasReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def upsert_conta_receber(self, **kargs) -> dict:
                """ Executa o Upsert do Contas a receber """
                return self._chamar_api(
                    call= 'UpsertContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def upsert_conta_receber_por_lote(self, **kargs) -> dict:
                """ Efetua o UPSERT do Contas a Receber por Lote. """
                return self._chamar_api(
                    call= 'UpsertContaReceberPorLote',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def cancelar_boleto(self, **kargs) -> dict:
                """ Cancela o Boleto. """
                return self._chamar_api(
                    call= 'CancelarBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def gerar_boleto(self, **kargs) -> dict:
                """ Gera um Boleto referente a um Contas a Receber. """
                return self._chamar_api(
                    call= 'GerarBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def obter_boleto(self, **kargs) -> dict:
                """ Disponibiliza o link de Download do Boleto. """
                return self._chamar_api(
                    call= 'ObterBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def prorrogar_boleto(self, **kargs) -> dict:
                """ Prorroga o vencimento do Boleto. """
                return self._chamar_api(
                    call= 'ProrrogarBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def cancelar_pix(self, **kargs) -> dict:
                """ Efetua o cancelamento de um PIX """
                return self._chamar_api(
                    call= 'CancelarPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def gerar_pix(self, **kargs) -> dict:
                """ Gera o QrCode de um PIX. """
                return self._chamar_api(
                    call= 'GerarPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def gerar_qr_code_pix(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'GerarQrCodePix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def listar_pix(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def listar_status_pix(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarStatusPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def obter_pix(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def obter_status_pix(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterStatusPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def listar_extrato(self, **kargs) -> dict:
                """ Listagem do Extrato """
                return self._chamar_api(
                    call= 'ListarExtrato',
                    endpoint= 'financas/extrato/',
                    param = kargs
                )
            
    def listar_orcamentos(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarOrcamentos',
                    endpoint= 'financas/caixa/',
                    param = kargs
                )
            
    def obter_u_r_l_boleto(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'ObterURLBoleto',
                    endpoint= 'financas/pesquisartitulos/',
                    param = kargs
                )
            
    def pesquisar_excluidos(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'PesquisarExcluidos',
                    endpoint= 'financas/pesquisartitulos/',
                    param = kargs
                )
            
    def pesquisar_lancamentos(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'PesquisarLancamentos',
                    endpoint= 'financas/pesquisartitulos/',
                    param = kargs
                )
            
    def obter_resumo_contador(self, **kargs) -> dict:
                """ Obtem o resumo do painel do contador. """
                return self._chamar_api(
                    call= 'ObterResumoContador',
                    endpoint= 'contador/resumo/',
                    param = kargs
                )
            
    def consultar_banco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarBanco',
                    endpoint= 'geral/bancos/',
                    param = kargs
                )
            
    def listar_bancos(self, **kargs) -> dict:
                """ Exibe uma lista com os banco cadastrados. """
                return self._chamar_api(
                    call= 'ListarBancos',
                    endpoint= 'geral/bancos/',
                    param = kargs
                )
            
    def consultar_tipo_documento(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarTipoDocumento',
                    endpoint= 'geral/tiposdoc/',
                    param = kargs
                )
            
    def pesquisar_tipo_documento(self, **kargs) -> dict:
                """ Pesquisa o tipo de documento """
                return self._chamar_api(
                    call= 'PesquisarTipoDocumento',
                    endpoint= 'geral/tiposdoc/',
                    param = kargs
                )
            
    def listar_tipos_c_c(self, **kargs) -> dict:
                """ Listar os tipos de contas correntes. """
                return self._chamar_api(
                    call= 'ListarTiposCC',
                    endpoint= 'geral/tipocc/',
                    param = kargs
                )
            
    def listar_cadastro_d_r_e(self, **kargs) -> dict:
                """ Lista as contas do DRE """
                return self._chamar_api(
                    call= 'ListarCadastroDRE',
                    endpoint= 'geral/dre/',
                    param = kargs
                )
            
    def consultar_final_transf(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarFinalTransf',
                    endpoint= 'geral/finaltransf/',
                    param = kargs
                )
            
    def listar_final_transf(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarFinalTransf',
                    endpoint= 'geral/finaltransf/',
                    param = kargs
                )
            
    def listar_bandeiras(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarBandeiras',
                    endpoint= 'geral/bandeiracartao/',
                    param = kargs
                )
            
    def alterar_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def associar_cod_int_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AssociarCodIntProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def consultar_produto(self, **kargs) -> dict:
                """ Consulta um produto. """
                return self._chamar_api(
                    call= 'ConsultarProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def excluir_produto(self, **kargs) -> dict:
                """ Exclui um produto """
                return self._chamar_api(
                    call= 'ExcluirProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def incluir_produto(self, **kargs) -> dict:
                """ Incluir um produto. """
                return self._chamar_api(
                    call= 'IncluirProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def incluir_produtos_por_lote(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'IncluirProdutosPorLote',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def listar_produtos(self, **kargs) -> dict:
                """ Lista completa do cadastro de produtos """
                return self._chamar_api(
                    call= 'ListarProdutos',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def listar_produtos_resumido(self, **kargs) -> dict:
                """ Lista os produtos cadastrados """
                return self._chamar_api(
                    call= 'ListarProdutosResumido',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def upsert_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'UpsertProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def upsert_produtos_por_lote(self, **kargs) -> dict:
                """ DEPRECATED """
                return self._chamar_api(
                    call= 'UpsertProdutosPorLote',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def alterar_caract_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def consultar_caract_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def excluir_caract_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def incluir_caract_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def listar_caract_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def alterar_estrutura(self, **kargs) -> dict:
                """ Alterar a estrutura de um produto. """
                return self._chamar_api(
                    call= 'AlterarEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def consultar_estrutura(self, **kargs) -> dict:
                """ Consulta a estrutura do produto. """
                return self._chamar_api(
                    call= 'ConsultarEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def excluir_estrutura(self, **kargs) -> dict:
                """ Excluir item da estrutura de um produto. """
                return self._chamar_api(
                    call= 'ExcluirEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def incluir_estrutura(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def listar_estruturas(self, **kargs) -> dict:
                """ Lista as estruturas de produtos. """
                return self._chamar_api(
                    call= 'ListarEstruturas',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def alterar_componentes_kit(self, **kargs) -> dict:
                """ Inclui/Altera/Exclui os componentes do KIT. """
                return self._chamar_api(
                    call= 'AlterarComponentesKit',
                    endpoint= 'geral/produtoskit/',
                    param = kargs
                )
            
    def alterar_req(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def consultar_req(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def excluir_req(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def incluir_req(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def pesquisar_req(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'PesquisarReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def upsert_req(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'UpsertReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def altera_ped_compra(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlteraPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def consultar_ped_compra(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def excluir_ped_compra(self, **kargs) -> dict:
                """ Excluir um Pedido de Compra """
                return self._chamar_api(
                    call= 'ExcluirPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def incluir_ped_compra(self, **kargs) -> dict:
                """ Incluir um Pedido de Compra """
                return self._chamar_api(
                    call= 'IncluirPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def pesquisar_ped_compra(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'PesquisarPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def upsert_ped_compra(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'UpsertPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def alterar_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def concluir_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConcluirOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def consultar_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def excluir_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def incluir_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def listar_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def reverter_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ReverterOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def upsert_ordem_producao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'UpsertOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def alterar_nota_ent(self, **kargs) -> dict:
                """ Alterar nota de entrada """
                return self._chamar_api(
                    call= 'AlterarNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def consultar_nota_ent(self, **kargs) -> dict:
                """ Consultar nota de entrada """
                return self._chamar_api(
                    call= 'ConsultarNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def excluir_nota_ent(self, **kargs) -> dict:
                """ Excluir nota de entrada """
                return self._chamar_api(
                    call= 'ExcluirNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def incluir_nota_ent(self, **kargs) -> dict:
                """ Incluir nota de entrada """
                return self._chamar_api(
                    call= 'IncluirNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def listar_nota_ent(self, **kargs) -> dict:
                """ Listagem de nota de entrada """
                return self._chamar_api(
                    call= 'ListarNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def status_nota_ent(self, **kargs) -> dict:
                """ Status de nota de entrada """
                return self._chamar_api(
                    call= 'StatusNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def cancelar_nota_ent(self, **kargs) -> dict:
                """ Cancelar nota de entrada """
                return self._chamar_api(
                    call= 'CancelarNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def concluir_nota_ent(self, **kargs) -> dict:
                """ Concluir nota de entrada """
                return self._chamar_api(
                    call= 'ConcluirNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def conferir_nota_ent(self, **kargs) -> dict:
                """ Conferir nota de entrada """
                return self._chamar_api(
                    call= 'ConferirNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def duplicar_nota_ent(self, **kargs) -> dict:
                """ Duplicar nota de entrada """
                return self._chamar_api(
                    call= 'DuplicarNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def alterar_etapa_recebimento(self, **kargs) -> dict:
                """ Alterar etapa recebimento NFe """
                return self._chamar_api(
                    call= 'AlterarEtapaRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def alterar_recebimento(self, **kargs) -> dict:
                """ Alterar recebimento de NFe """
                return self._chamar_api(
                    call= 'AlterarRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def concluir_recebimento(self, **kargs) -> dict:
                """ Concluir recebimento de NFe """
                return self._chamar_api(
                    call= 'ConcluirRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def consultar_recebimento(self, **kargs) -> dict:
                """ Consultar recebimento de NFe """
                return self._chamar_api(
                    call= 'ConsultarRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def listar_recebimentos(self, **kargs) -> dict:
                """ Listar recebimento de NFe """
                return self._chamar_api(
                    call= 'ListarRecebimentos',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def reverter_recebimento(self, **kargs) -> dict:
                """ Reverter recebimento NFe """
                return self._chamar_api(
                    call= 'ReverterRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def alterar_familia(self, **kargs) -> dict:
                """ Altera uma familia de produto """
                return self._chamar_api(
                    call= 'AlterarFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def consultar_familia(self, **kargs) -> dict:
                """ Consulta uma familia de produto """
                return self._chamar_api(
                    call= 'ConsultarFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def excluir_familia(self, **kargs) -> dict:
                """ Exclui uma familia de produto """
                return self._chamar_api(
                    call= 'ExcluirFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def incluir_familia(self, **kargs) -> dict:
                """ Inclui uma familia de produto """
                return self._chamar_api(
                    call= 'IncluirFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def pesquisar_familias(self, **kargs) -> dict:
                """ Listagem de familias cadastradas """
                return self._chamar_api(
                    call= 'PesquisarFamilias',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def upsert_familia(self, **kargs) -> dict:
                """ Inclui / Altera uma familia de produto """
                return self._chamar_api(
                    call= 'UpsertFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def listar_unidades(self, **kargs) -> dict:
                """ Lista as unidades de medidas """
                return self._chamar_api(
                    call= 'ListarUnidades',
                    endpoint= 'geral/unidade/',
                    param = kargs
                )
            
    def listar_compradores(self, **kargs) -> dict:
                """ Lista os compradores cadastrados. """
                return self._chamar_api(
                    call= 'ListarCompradores',
                    endpoint= 'estoque/comprador/',
                    param = kargs
                )
            
    def listar_produto_fornecedor(self, **kargs) -> dict:
                """ Listar os produtos por fornecedores. """
                return self._chamar_api(
                    call= 'ListarProdutoFornecedor',
                    endpoint= 'estoque/produtofornecedor/',
                    param = kargs
                )
            
    def listar_formas_pag_vendas(self, **kargs) -> dict:
                """ Lista as formas de pagmento de vendas. """
                return self._chamar_api(
                    call= 'ListarFormasPagVendas',
                    endpoint= 'produtos/formaspagvendas/',
                    param = kargs
                )
            
    def consultar_n_c_m(self, **kargs) -> dict:
                """ Consulta um NCM """
                return self._chamar_api(
                    call= 'ConsultarNCM',
                    endpoint= 'produtos/ncm/',
                    param = kargs
                )
            
    def listar_n_c_m(self, **kargs) -> dict:
                """ Lista os NCMs cadastrados. """
                return self._chamar_api(
                    call= 'ListarNCM',
                    endpoint= 'produtos/ncm/',
                    param = kargs
                )
            
    def listar_cenarios(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarCenarios',
                    endpoint= 'geral/cenarios/',
                    param = kargs
                )
            
    def listar_impostos_cenario(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarImpostosCenario',
                    endpoint= 'geral/cenarios/',
                    param = kargs
                )
            
    def listar_c_f_o_p(self, **kargs) -> dict:
                """ Listar as CFOPs """
                return self._chamar_api(
                    call= 'ListarCFOP',
                    endpoint= 'produtos/cfop/',
                    param = kargs
                )
            
    def listar_c_s_t(self, **kargs) -> dict:
                """ Listar os CSTs do ICMS """
                return self._chamar_api(
                    call= 'ListarCST',
                    endpoint= 'produtos/icmscst/',
                    param = kargs
                )
            
    def listar_c_s_o_s_n(self, **kargs) -> dict:
                """ Listar os CSOSN do ICMS. """
                return self._chamar_api(
                    call= 'ListarCSOSN',
                    endpoint= 'produtos/icmscsosn/',
                    param = kargs
                )
            
    def listar_orig_merc(self, **kargs) -> dict:
                """ Listar a origem da mercadoria do ICMS. """
                return self._chamar_api(
                    call= 'ListarOrigMerc',
                    endpoint= 'produtos/icmsorigem/',
                    param = kargs
                )
            
    def listar_cst_pis(self, **kargs) -> dict:
                """ Listar o CST do PIS. """
                return self._chamar_api(
                    call= 'ListarCstPis',
                    endpoint= 'produtos/piscst/',
                    param = kargs
                )
            
    def listar_cst_cofins(self, **kargs) -> dict:
                """ Listar CST do COFINS. """
                return self._chamar_api(
                    call= 'ListarCstCofins',
                    endpoint= 'produtos/cofinscst/',
                    param = kargs
                )
            
    def listar_cst_ipi(self, **kargs) -> dict:
                """ Listar CST do IPI. """
                return self._chamar_api(
                    call= 'ListarCstIpi',
                    endpoint= 'produtos/ipicst/',
                    param = kargs
                )
            
    def listar_enq_ipi(self, **kargs) -> dict:
                """ Listar Enquadramento do IPI. """
                return self._chamar_api(
                    call= 'ListarEnqIpi',
                    endpoint= 'produtos/ipienq/',
                    param = kargs
                )
            
    def listar_tp_calc(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarTpCalc',
                    endpoint= 'produtos/tpcalc/',
                    param = kargs
                )
            
    def listar_c_e_s_t(self, **kargs) -> dict:
                """ Listar CEST. """
                return self._chamar_api(
                    call= 'ListarCEST',
                    endpoint= 'produtos/cest/',
                    param = kargs
                )
            
    def alterar_estoque_minimo(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarEstoqueMinimo',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def excluir_ajuste_estoque(self, **kargs) -> dict:
                """ Excluir um Movimento de Ajuste de Estoque """
                return self._chamar_api(
                    call= 'ExcluirAjusteEstoque',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def incluir_ajuste_estoque(self, **kargs) -> dict:
                """ Incluir um Ajuste de Estoque """
                return self._chamar_api(
                    call= 'IncluirAjusteEstoque',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def listar_ajuste_estoque(self, **kargs) -> dict:
                """ Listar os ajuste de estoque. """
                return self._chamar_api(
                    call= 'ListarAjusteEstoque',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def listar_movimento_estoque(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarMovimentoEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def listar_pos_estoque(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarPosEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def listar_saldo_pendente(self, **kargs) -> dict:
                """ Lista o saldo pendente de estoque. """
                return self._chamar_api(
                    call= 'ListarSaldoPendente',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def movimento_estoque(self, **kargs) -> dict:
                """ Consulta do Movimento de Estoque """
                return self._chamar_api(
                    call= 'MovimentoEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def posicao_estoque(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'PosicaoEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def consultar_previsao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarPrevisao',
                    endpoint= 'estoque/movestoque/',
                    param = kargs
                )
            
    def listar_movimentos(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarMovimentos',
                    endpoint= 'financas/mf/',
                    param = kargs
                )
            
    def alterar_local_estoque(self, **kargs) -> dict:
                """ Alterar local de Estoque """
                return self._chamar_api(
                    call= 'AlterarLocalEstoque',
                    endpoint= 'estoque/local/',
                    param = kargs
                )
            
    def incluir_local_estoque(self, **kargs) -> dict:
                """ Adiciona um local de estoque """
                return self._chamar_api(
                    call= 'IncluirLocalEstoque',
                    endpoint= 'estoque/local/',
                    param = kargs
                )
            
    def listar_locais_estoque(self, **kargs) -> dict:
                """ Lista os Locais de Estoque encontrados. """
                return self._chamar_api(
                    call= 'ListarLocaisEstoque',
                    endpoint= 'estoque/local/',
                    param = kargs
                )
            
    def obter_estoque_produto(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterEstoqueProduto',
                    endpoint= 'estoque/resumo/',
                    param = kargs
                )
            
    def adicionar_pedido(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AdicionarPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def alterar_item_pedido(self, **kargs) -> dict:
                """ Altera um item no pedido de venda. """
                return self._chamar_api(
                    call= 'AlterarItemPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def excluir_item_pedido(self, **kargs) -> dict:
                """ Exclui um item no pedido de venda. """
                return self._chamar_api(
                    call= 'ExcluirItemPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def excluir_itens_pedido(self, **kargs) -> dict:
                """ Exclui todos os itens do pedido de venda. """
                return self._chamar_api(
                    call= 'ExcluirItensPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def incluir_item_pedido(self, **kargs) -> dict:
                """ Inclui um item no pedido de venda. """
                return self._chamar_api(
                    call= 'IncluirItemPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def totalizar_pedido(self, **kargs) -> dict:
                """ Recalcula os totais do pedido de venda. """
                return self._chamar_api(
                    call= 'TotalizarPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def alterar_ped_faturado(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarPedFaturado',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def alterar_pedido_venda(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarPedidoVenda',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def consultar_pedido(self, **kargs) -> dict:
                """ Consulta de Pedido de Venda de Produto """
                return self._chamar_api(
                    call= 'ConsultarPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def excluir_pedido(self, **kargs) -> dict:
                """ Excluir pedido de venda de produto """
                return self._chamar_api(
                    call= 'ExcluirPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def incluir_pedido(self, **kargs) -> dict:
                """ Inclui um pedido de venda de produto """
                return self._chamar_api(
                    call= 'IncluirPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def listar_pedidos(self, **kargs) -> dict:
                """ Listar os pedidos de venda de produto """
                return self._chamar_api(
                    call= 'ListarPedidos',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def simular_impostos(self, **kargs) -> dict:
                """ Simula os impostos de um pedido de venda. """
                return self._chamar_api(
                    call= 'SimularImpostos',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def status_pedido(self, **kargs) -> dict:
                """ Consulta do Status do Pedido """
                return self._chamar_api(
                    call= 'StatusPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def trocar_etapa_pedido(self, **kargs) -> dict:
                """ Troca etapa do pedido. """
                return self._chamar_api(
                    call= 'TrocarEtapaPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def associar_cod_int_pedido_venda(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AssociarCodIntPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def cancelar_pedido_venda(self, **kargs) -> dict:
                """ Cancela um pedido de venda de produto. """
                return self._chamar_api(
                    call= 'CancelarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def duplicar_pedido_venda(self, **kargs) -> dict:
                """ Duplica um pedido de venda de produto. """
                return self._chamar_api(
                    call= 'DuplicarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def faturar_pedido_venda(self, **kargs) -> dict:
                """ Fatura um pedido de venda de produto. """
                return self._chamar_api(
                    call= 'FaturarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def obter_pedidos_venda(self, **kargs) -> dict:
                """ Retorna a lista de pedidos de venda a serem faturados. """
                return self._chamar_api(
                    call= 'ObterPedidosVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def validar_pedido_venda(self, **kargs) -> dict:
                """ Valida um pedido de venda de produto para faturamento. """
                return self._chamar_api(
                    call= 'ValidarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def listar_etapas_pedido(self, **kargs) -> dict:
                """ Lista as etapas do Pedido de Venda de Produtos. """
                return self._chamar_api(
                    call= 'ListarEtapasPedido',
                    endpoint= 'produtos/pedidoetapas/',
                    param = kargs
                )
            
    def averbacao_c_te(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AverbacaoCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def cancelar_c_te(self, **kargs) -> dict:
                """ Cancela um CT-e. """
                return self._chamar_api(
                    call= 'CancelarCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def carta_correcao_c_te(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'CartaCorrecaoCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def excluir_c_te(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def excluir_fatura_c_te(self, **kargs) -> dict:
                """ Exclui uma fatura de um grupo de CT-es. """
                return self._chamar_api(
                    call= 'ExcluirFaturaCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def faturar_c_te(self, **kargs) -> dict:
                """ Gera uma fatura para um grupo de CT-es. """
                return self._chamar_api(
                    call= 'FaturarCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def faturar_lote_c_te(self, **kargs) -> dict:
                """ Gera uma fatura por lote para um grupo de CT-es. """
                return self._chamar_api(
                    call= 'FaturarLoteCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def importar_c_te(self, **kargs) -> dict:
                """ Importar o XML de um CT-e. """
                return self._chamar_api(
                    call= 'ImportarCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def listar_n_fe_transp(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarNFeTransp',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def status_fatura(self, **kargs) -> dict:
                """ Retorna o Status da Fatura inclusa. """
                return self._chamar_api(
                    call= 'StatusFatura',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def alterar_remessa(self, **kargs) -> dict:
                """ Altera uma remessa """
                return self._chamar_api(
                    call= 'AlterarRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def consultar_remessa(self, **kargs) -> dict:
                """ Consulta uma remessa. """
                return self._chamar_api(
                    call= 'ConsultarRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def incluir_remessa(self, **kargs) -> dict:
                """ Inclui uma nova remessa """
                return self._chamar_api(
                    call= 'IncluirRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def listar_remessas(self, **kargs) -> dict:
                """ Lista as remessas cadastradas. """
                return self._chamar_api(
                    call= 'ListarRemessas',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def status_remessa(self, **kargs) -> dict:
                """ Retorna o status da remessa """
                return self._chamar_api(
                    call= 'StatusRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def cancelar_remessa(self, **kargs) -> dict:
                """ Cancelar remessa de produto """
                return self._chamar_api(
                    call= 'CancelarRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def concluir_remessa(self, **kargs) -> dict:
                """ Concluir remessa de produto """
                return self._chamar_api(
                    call= 'ConcluirRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def conferir_remessa(self, **kargs) -> dict:
                """ Conferir remessa de produto """
                return self._chamar_api(
                    call= 'ConferirRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def duplicar_remessa(self, **kargs) -> dict:
                """ Duplicar remessa de produto """
                return self._chamar_api(
                    call= 'DuplicarRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def obter_demonst(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterDemonst',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_n_f_se(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterNFSe',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def obter_r_p_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterRPS',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_recibo(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterRecibo',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_via_unica(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterViaUnica',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def fechar_caixa(self, **kargs) -> dict:
                """ Efetua o fechamento de um determinado caixa. """
                return self._chamar_api(
                    call= 'FecharCaixa',
                    endpoint= 'produtos/cupomfiscalincluir/',
                    param = kargs
                )
            
    def inutilizar_nfce(self, **kargs) -> dict:
                """ Inutiliza um lote de NFC-e. """
                return self._chamar_api(
                    call= 'InutilizarNfce',
                    endpoint= 'produtos/cupomfiscalincluir/',
                    param = kargs
                )
            
    def cancelar_cupom(self, **kargs) -> dict:
                """ Cancela um cupom Fiscal """
                return self._chamar_api(
                    call= 'CancelarCupom',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def cancelar_n_f_c_e(self, **kargs) -> dict:
                """ Cancelar NFC-e. """
                return self._chamar_api(
                    call= 'CancelarNFCE',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def cancelar_s_a_t(self, **kargs) -> dict:
                """ Cancelar CF-e-SAT. """
                return self._chamar_api(
                    call= 'CancelarSAT',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def devolver_cupom(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'DevolverCupom',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def excluir_cupom(self, **kargs) -> dict:
                """ Exclui um Cupom Fiscal. """
                return self._chamar_api(
                    call= 'ExcluirCupom',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def excluir_cupons_por_numero(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirCuponsPorNumero',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def excluir_lote(self, **kargs) -> dict:
                """ Excluir o lote """
                return self._chamar_api(
                    call= 'ExcluirLote',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def listar_cupons(self, **kargs) -> dict:
                """ Lista os Cupons Fiscais. """
                return self._chamar_api(
                    call= 'ListarCupons',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def obter_proximo_lote(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterProximoLote',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def cupons_fiscais(self, **kargs) -> dict:
                """ Listagem dos cupons fiscais. """
                return self._chamar_api(
                    call= 'CuponsFiscais',
                    endpoint= 'produtos/cupomfiscalconsultar/',
                    param = kargs
                )
            
    def cupons_itens(self, **kargs) -> dict:
                """ Listagem dos itens dos cupons fiscais """
                return self._chamar_api(
                    call= 'CuponsItens',
                    endpoint= 'produtos/cupomfiscalconsultar/',
                    param = kargs
                )
            
    def cupons_pagamentos(self, **kargs) -> dict:
                """ Listagem dos pagamentos dos cupons fiscais """
                return self._chamar_api(
                    call= 'CuponsPagamentos',
                    endpoint= 'produtos/cupomfiscalconsultar/',
                    param = kargs
                )
            
    def importar_n_f_ce(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ImportarNFCe',
                    endpoint= 'produtos/nfce/',
                    param = kargs
                )
            
    def importar_cfe_sat(self, **kargs) -> dict:
                """ Importa o XML de um CF-e SAT. """
                return self._chamar_api(
                    call= 'ImportarCfeSat',
                    endpoint= 'produtos/sat/',
                    param = kargs
                )
            
    def alterar_preco_item(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarPrecoItem',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def alterar_tabela_preco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def ativar_tabela_preco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AtivarTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def atualizar_produtos(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AtualizarProdutos',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def consultar_tabela_preco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def excluir_tabela_preco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def incluir_tabela_preco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def listar_tabela_itens(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarTabelaItens',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def listar_tabelas_preco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarTabelasPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def suspender_tabela_preco(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'SuspenderTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def alterar_caracteristica(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def consultar_caracteristica(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def excluir_caracteristica(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def incluir_caracteristica(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def listar_caracteristicas(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarCaracteristicas',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def listar_etapas_faturamento(self, **kargs) -> dict:
                """ Lista as etapas do faturamento """
                return self._chamar_api(
                    call= 'ListarEtapasFaturamento',
                    endpoint= 'produtos/etapafat/',
                    param = kargs
                )
            
    def listar_meios_pagamento(self, **kargs) -> dict:
                """ Listagem de meios de pagamento """
                return self._chamar_api(
                    call= 'ListarMeiosPagamento',
                    endpoint= 'geral/meiospagamento/',
                    param = kargs
                )
            
    def listar_origem(self, **kargs) -> dict:
                """ Lista Origem de pedidos. """
                return self._chamar_api(
                    call= 'ListarOrigem',
                    endpoint= 'geral/origempedido/',
                    param = kargs
                )
            
    def listar_motivos_devol(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarMotivosDevol',
                    endpoint= 'geral/motivodevolucao/',
                    param = kargs
                )
            
    def listar_n_f_s_es(self, **kargs) -> dict:
                """ Lista de NFS-es. """
                return self._chamar_api(
                    call= 'ListarNFSEs',
                    endpoint= 'servicos/nfse/',
                    param = kargs
                )
            
    def get_url_danfe(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'GetUrlDanfe',
                    endpoint= 'produtos/notafiscalutil/',
                    param = kargs
                )
            
    def get_url_logo(self, **kargs) -> dict:
                """ Retorna a URL do Logotipo """
                return self._chamar_api(
                    call= 'GetUrlLogo',
                    endpoint= 'produtos/notafiscalutil/',
                    param = kargs
                )
            
    def get_url_nota_fiscal(self, **kargs) -> dict:
                """ Retorna a URL da Nota Fiscal """
                return self._chamar_api(
                    call= 'GetUrlNotaFiscal',
                    endpoint= 'produtos/notafiscalutil/',
                    param = kargs
                )
            
    def excluir_n_fe(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirNFe',
                    endpoint= 'produtos/nfe/',
                    param = kargs
                )
            
    def importar_canc_n_fe(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ImportarCancNFe',
                    endpoint= 'produtos/nfe/',
                    param = kargs
                )
            
    def listar_n_fe(self, **kargs) -> dict:
                """ Lista as NFes importadas. """
                return self._chamar_api(
                    call= 'ListarNFe',
                    endpoint= 'produtos/nfe/',
                    param = kargs
                )
            
    def associar_cod_int_servico(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AssociarCodIntServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def consultar_cadastro_servico(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def excluir_cadastro_servico(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def listar_cadastro_servico(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def alterar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AlterarOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def consultar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def excluir_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def incluir_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def listar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def status_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'StatusOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def trocar_etapa_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'TrocarEtapaOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def associar_cod_int_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'AssociarCodIntOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def cancelar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'CancelarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def duplicar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'DuplicarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def faturar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'FaturarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def reenviar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ReenviarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def validar_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ValidarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def faturar_lote_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'FaturarLoteOS',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def listar_lote_nfse(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarLoteNfse',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def listar_lotes_o_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarLotesOS',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def status_lote_o_s(self, **kargs) -> dict:
                """ Status do lote faturado a partir do ID. """
                return self._chamar_api(
                    call= 'StatusLoteOS',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def alterar_contrato(self, **kargs) -> dict:
                """ Alterar um Contrato """
                return self._chamar_api(
                    call= 'AlterarContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def consultar_contrato(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ConsultarContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def excluir_item(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ExcluirItem',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def incluir_contrato(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'IncluirContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def listar_contratos(self, **kargs) -> dict:
                """ Lista os contratos cadastrados. """
                return self._chamar_api(
                    call= 'ListarContratos',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def upsert_contrato(self, **kargs) -> dict:
                """ Inclui / Altera um contrato """
                return self._chamar_api(
                    call= 'UpsertContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def ativar_contrato(self, **kargs) -> dict:
                """ Ativa um contrato """
                return self._chamar_api(
                    call= 'AtivarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def cancelar_contrato(self, **kargs) -> dict:
                """ Cancela contrato """
                return self._chamar_api(
                    call= 'CancelarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def faturar_contrato(self, **kargs) -> dict:
                """ Fatura um contrato. """
                return self._chamar_api(
                    call= 'FaturarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def obter_contratos(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ObterContratos',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def reativar_contrato(self, **kargs) -> dict:
                """ Reativar contrato """
                return self._chamar_api(
                    call= 'ReativarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def suspender_contrato(self, **kargs) -> dict:
                """ Suspende contrato """
                return self._chamar_api(
                    call= 'SuspenderContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def validar_contrato(self, **kargs) -> dict:
                """ Valida os dados de um contrato para faturamento. """
                return self._chamar_api(
                    call= 'ValidarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def faturar_lote_contrato(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'FaturarLoteContrato',
                    endpoint= 'servicos/contratolote/',
                    param = kargs
                )
            
    def listar_lotes_contrato(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarLotesContrato',
                    endpoint= 'servicos/contratolote/',
                    param = kargs
                )
            
    def status_lote_contrato(self, **kargs) -> dict:
                """ Status do lote faturado a partir do ID. """
                return self._chamar_api(
                    call= 'StatusLoteContrato',
                    endpoint= 'servicos/contratolote/',
                    param = kargs
                )
            
    def listar_serv_munic(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarServMunic',
                    endpoint= 'servicos/listaservico/',
                    param = kargs
                )
            
    def listar_tipos_trib(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarTiposTrib',
                    endpoint= 'servicos/tipotrib/',
                    param = kargs
                )
            
    def listar_l_c116(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarLC116',
                    endpoint= 'servicos/lc116/',
                    param = kargs
                )
            
    def listar_n_b_s(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarNBS',
                    endpoint= 'servicos/nbs/',
                    param = kargs
                )
            
    def listar_produtos_i_b_p_t(self, **kargs) -> dict:
                """ Lista os produtos da Tabela do IBPT. """
                return self._chamar_api(
                    call= 'ListarProdutosIBPT',
                    endpoint= 'servicos/ibpt/',
                    param = kargs
                )
            
    def listar_servicos_i_b_p_t(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarServicosIBPT',
                    endpoint= 'servicos/ibpt/',
                    param = kargs
                )
            
    def listar_tipo_fat_contrato(self, **kargs) -> dict:
                """ Lista os tipos de faturamento de contrato. """
                return self._chamar_api(
                    call= 'ListarTipoFatContrato',
                    endpoint= 'servicos/contratotpfat/',
                    param = kargs
                )
            
    def listar_tipo_utilizacao(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarTipoUtilizacao',
                    endpoint= 'servicos/tipoutilizacao/',
                    param = kargs
                )
            
    def listar_classificacao_servico(self, **kargs) -> dict:
                """  """
                return self._chamar_api(
                    call= 'ListarClassificacaoServico',
                    endpoint= 'servicos/classificacaoservico/',
                    param = kargs
                )
            
    def listar_documentos(self, **kargs) -> dict:
                """ Lista de XMLs de Documentos Fiscais. """
                return self._chamar_api(
                    call= 'ListarDocumentos',
                    endpoint= 'contador/xml/',
                    param = kargs
                )
    def listar_todos_movimentos(self, **kargs) -> dict:
                """ 	
                Solicitação de Listagem da movimentação financeira (Contas a Pagar, Contas a Receber e Lançamentos do Conta Corrente).
                """
                return self._chamar_api(
                    call= 'ListarMovimentos',
                    endpoint= 'financas/mf',
                    param = kargs
                )
            
