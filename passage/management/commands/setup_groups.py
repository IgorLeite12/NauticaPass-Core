from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Configura grupos e permissões iniciais'

    def handle(self, *args, **options):
        usuario_group, _ = Group.objects.get_or_create(name='Usuario')
        proprietario_group, _ = Group.objects.get_or_create(name='Proprietario')
        admin_group, _ = Group.objects.get_or_create(name='Administrador')

        try:
            add_ticket_perm = Permission.objects.get(codename='add_ticket')
            usuario_group.permissions.clear()
            usuario_group.permissions.add(add_ticket_perm)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.WARNING('Permissão "add_ticket" não encontrada.'))

        try:
            add_vessel = Permission.objects.get(codename='add_vessel')
            change_vessel = Permission.objects.get(codename='change_vessel')
            add_passage = Permission.objects.get(codename='add_passage')
            change_passage = Permission.objects.get(codename='change_passage')
            proprietario_group.permissions.clear()
            proprietario_group.permissions.add(add_vessel, change_vessel, add_passage, change_passage)
        except ObjectDoesNotExist as e:
            self.stdout.write(self.style.WARNING(f'Permissão não encontrada: {e}'))

        self.stdout.write(self.style.SUCCESS('Grupos e permissões configurados.'))