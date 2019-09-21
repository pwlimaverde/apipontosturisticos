from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def descricao_completa(self):
        aprovado = self.aprovado
        if aprovado == True:
            aprovado = 'aprovado'
        else:
            aprovado = 'reprovado'

        return '%s - %s - %s' %(self.nome, self.descricao, aprovado)

    def __str__(self):
        return self.nome
