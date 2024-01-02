import dados

# Caderno de IA

class Coisa:
    def __init__(self, estado =None):
        self.estado = estado

    def __repr__(self):
        # representação do objeto na fora de string
        return '<{}>'.format(getattr(self,'__name__',self.__class__.__name__))
    
    def mostraEstado(self):
        # mostra o esstado do agente
        return str(self.estado)
    
    def vivo(self):
        return hasattr(self, 'vivo') and self.vivo
    

class Agente(Coisa):
    def __init__(self,estado = None, funcaoAgente = None):
        super().__init__(estado)
        if funcaoAgente == None:
            def funcaoAgente(*entradas):  #toma a decição para o agente
                return "Acao Default"
        self.funcaoAgente = funcaoAgente
        self.historicoPercepcoes = []

    def percepcao(self):
        entrada = input("Entre com dados")
        self.historicoPercepcoes.append(eval(entrada))

    def saida(self):
        return self.funcaoAgente(self.historicoPercepcoes)
    
class Ambiente:
    def __init__(self,estadoInicial = None):
        self.estado = estadoInicial
        self.objetosNoAmbiente = []
        self.agentes = []
    
    def percepcao(self,agente):
        #define as percepções do agente
        return None
    
    def adicionaAgente(self,agente):
        self.agentes.append(agente)

    def adicionaObjeto(self,obj):
        self.objetosNoAmbiente.append(obj)


# Agente vai decidir quando o nível dos rios está ficando perigoso

def funcaoAgenteDecidePerigo(media,valor):
    if valor >= media:
        return False,valor,media
    else:
        return True,valor,media


class AgenteEnchente(Agente):
    def __init__(self, estadoInicial=None, funcaoAgente=None):
        super().__init__(estadoInicial, funcaoAgente)
        self.observacao = 0
        self.mediaAtual = 0
        self.medias = []

    def atualizaEstado(self,valor):
        self.observacao += 1
        if self.observacao == 1:
            self.mediaAtual = valor
        else:
            self.mediaAtual = self.mediaAtual + (valor - self.mediaAtual)/(self.observacao + 1)
        self.estado.append(valor)
        self.medias.append(self.mediaAtual)

    def percepcao(self,valorAtual):
        self.atualizaEstado(valorAtual)

    def saida(self):
        return self.funcaoAgente(self.medias[-1],self.estado[-1])
    
ac = AgenteEnchente([],funcaoAgenteDecidePerigo)
for i in dados.y[:10]:
    ac.percepcao(i)
    print(ac.saida(),end=",")