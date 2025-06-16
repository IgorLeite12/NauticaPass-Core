from django.core.management.base import BaseCommand
from passage.models import City

class Command(BaseCommand):
    help = 'Popula o banco com a lista de cidades'

    def handle(self, *args, **options):
        cities = [
            "Abaetetuba - PA", "Alenquer - PA", "Almeirim - PA",
            "Alvarães - AM", "Amaturá - AM", "Anamã - AM",
            "Anori - AM", "Apuí - AM", "Atalaia do Norte - AM",
            "Autazes - AM", "Barcarena - PA", "Barcelos - AM",
            "Barreirinha - AM", "Belém - PA", "Benjamin Constant - AM",
            "Beruri - AM", "Boa Vista do Ramos - AM", "Boca do Acre - AM",
            "Borba - AM", "Caapiranga - AM", "Cametá - PA",
            "Canutama - AM", "Careiro - AM", "Careiro da Várzea - AM",
            "Carauari - AM", "Chaves - PA", "Codajás - AM",
            "Coari - AM", "Envira - AM", "Eirunepé - AM",
            "Fonte Boa - AM", "Guajará - AM", "Humaitá - AM",
            "Ipixuna - AM", "Iranduba - AM", "Itacoatiara - AM",
            "Itaituba - PA", "Itamarati - AM", "Itapiranga - AM",
            "Japurá - AM", "Juruá - AM", "Jutaí - AM",
            "Lábrea - AM", "Manaquiri - AM", "Manaus - AM",
            "Manacapuru - AM", "Manicoré - AM", "Maraã - AM",
            "Maués - AM", "Monte Alegre - PA", "Nhamundá - AM",
            "Nova Airão - AM", "Nova Olinda do Norte - AM", "Novo Aripuanã - AM",
            "Óbidos - PA", "Oriximiná - PA", "Parintins - AM",
            "Pauini - AM", "Santarém - PA", "Santa Isabel do Rio Negro - AM",
            "Santo Antônio do Içá - AM", "São Gabriel da Cachoeira - AM", "São Paulo de Olivença - AM",
            "São Sebastião do Uatumã - AM", "Silves - AM", "Tabatinga - AM",
            "Tapauá - AM", "Tefé - AM", "Tonantins - AM",
            "Uarini - AM", "Urucará - AM", "Urucurituba - AM"
        ]

        cities.sort()

        for name in cities:
            City.objects.get_or_create(name=name)

        self.stdout.write(self.style.SUCCESS('Cidades populadas em ordem alfabética com sucesso!'))