from django.core.management.base import BaseCommand
from passage.models import City

class Command(BaseCommand):
    help = 'Popula o banco com a lista de cidades'

    def handle(self, *args, **options):
        cities = [
            "Manaus", "Itacoatiara", "Manacapuru", "Parintins", "Tefé", "Coari", "Tabatinga", "Maués",
            "Iranduba", "Humaitá", "Manicoré", "São Gabriel da Cachoeira", "Lábrea", "Autazes",
            "Benjamin Constant", "Boca do Acre", "Eirunepé", "Borba", "São Paulo de Olivença",
            "Barreirinha", "Careiro", "Carauari", "Santo Antônio do Içá", "Nova Olinda do Norte",
            "Fonte Boa", "Jutaí", "Ipixuna", "Urucurituba", "Novo Aripuanã", "Boa Vista do Ramos",
            "Codajás", "Beruri", "Apuí", "Nhamundá", "Careiro da Várzea", "Tapauá", "Pauini", "Tonantins",
            "Barcelos", "Urucará", "Anori", "Envira", "Manaquiri", "Canutama", "Alvarães", "Novo Airão",
            "Maraã", "Atalaia do Norte", "Uarini", "Santa Isabel do Rio Negro", "Guajará", "Caapiranga",
            "São Sebastião do Uatumã", "Silves", "Itamarati", "Amaturá", "Juruá", "Itapiranga", "Anamã",
            "Japurá", "Belém", "Santarém", "Barcarena", "Altamira", "Itaituba", "Abaetetuba", "Cametá",
            "Oriximiná", "Óbidos", "Alenquer", "Almeirim", "Chaves", "Monte Alegre"
        ]

        cities.sort()

        for name in cities:
            City.objects.get_or_create(name=name)

        self.stdout.write(self.style.SUCCESS('Cidades populadas em ordem alfabética com sucesso!'))