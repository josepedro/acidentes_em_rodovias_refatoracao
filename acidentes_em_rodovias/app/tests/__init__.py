

#------------Controller---------
# Index
from tests_controller_index import TestControllerIndex
# Consulta basica
from tests_controller_consultabasica_periodo import Test_Periodo
from tests_controller_consultabasica_regiao import Test_Regiao
# Estatisticas
from tests_controller_estatistica_causa import TestCausa
from tests_controller_estatistica_sexo import Test_Sexo
from tests_controller_estatistica_envolvidos import Test_Envolvidos
from tests_controller_estatistica_br import TestEstatisticaBR
from tests_controller_estatistica_tipo import TestControllerEstatisticaTipo
from tests_controller_estatistica_uf import Test_Estatisticas_UF
# ------------DAO---------
from tests_dao import TestDAO
from tests_dao_municipio import TestMunicipio
from tests_dao_UF import TestUF
from tests_dao_ocorrencia import TestOcorrencia
from tests_dao_causas_acidentes import TestCausasAcidentes
from tests_dao_tiposacidentes import TestTiposAcidentes
from tests_dao_envolvidosacidentes import TestEnvolvidosAcidentes
from tests_dao_br_acidentes import Test_BR_Acidentes
from tests_dao_uf_acidentes import Test_UF_Acidentes
# Util
from tests_util_validacao import Test_Valida
from tests_util_estatisticas import Test_Estatisticas