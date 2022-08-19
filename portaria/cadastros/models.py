from django.db import models

# Create your models here.

class Casa(models.Model):
    bloco_numero = models.CharField(max_length=7, help_text="Exemplo: G-36", verbose_name="Bloco e número")
    endereco = models.CharField(max_length=300, verbose_name="Endereço")
    
    def __str__(self):
        return "{}" .format(self.bloco_numero)

class Morador(models.Model):
    nome_completo = models.CharField(max_length=256)
    cpf = models.CharField(max_length=14, blank=True, null=True, verbose_name="CPF")
    data_de_moradia = models.DateField(auto_now=False, auto_now_add=False, help_text="Exemplo: 01/10/1998", verbose_name="Morando desde")
    telefone = models.CharField(max_length=16, blank=True, null=True)
    casa = models.ForeignKey(Casa, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - ({})" .format(self.nome_completo, self.casa.bloco_numero)

class Visitante(models.Model):
    nome_completo = models.CharField(max_length=256)
    identidade = models.CharField(max_length=14, verbose_name="CPF ou RG")
    data_de_entrada = models.DateTimeField(blank=True, null=True, max_length=10, help_text="Exemplo: 19/08/2022 19:30", verbose_name="Data de Entrada/Horário")
    placa_veiculo = models.CharField(max_length=8, blank=True, null=True, verbose_name="Placa do veículo")
    casa = models.ForeignKey(Casa, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - ({})" .format(self.nome_completo, self.casa.bloco_numero)

class PrestadorServico(models.Model):
    nome_completo = models.CharField(max_length=256)
    identidade = models.CharField(max_length=14, verbose_name="CPF ou RG")
    data_de_entrada = models.DateTimeField(blank=True, null=True, max_length=10, help_text="Exemplo: 19/08/2022 19:30", verbose_name="Data de Entrada/Horário")
    placa_veiculo = models.CharField(max_length=8, blank=True, null=True, verbose_name="Placa do veículo")
    casa = models.ForeignKey(Casa, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - ({})" .format(self.nome_completo, self.casa.bloco_numero)