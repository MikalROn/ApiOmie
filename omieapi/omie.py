from omieapi.core.omiebase import OmieBase
from omieapi.omie_geral import Geral
from omieapi.omie_financas import Financas
from omieapi.omie_estoque import Estoque


class Omie(OmieBase):
    """
    Classe que carrega todos os metodos da api
    :param omie_app_key:              Chave api da omie
    :param omie_app_secret:           APi Secret da omie
    """
    def Geral(self) -> Geral:
        return Geral(self._appkey, self._appsecret)

    def Financas(self) -> Financas:
        return Financas(self._appkey, self._appsecret)

    def Estoque(self) -> Estoque:
        return Estoque(self._appkey, self._appsecret)