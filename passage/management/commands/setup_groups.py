from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Configura grupos e permissões iniciais'

    def handle(self, *args, **options):
        usuario_group, _ = Group.objects.get_or_create(name='Usuario')
        proprietario_group, _ = Group.objects.get_or_create(name='Proprietario')
        admin_group, _ = Group.objects.get_or_create(name='Administrador')

        # Permissões para o grupo Usuario
        try:
            perms_usuario = [
                'add_ticket', 'view_ticket',
                'add_user', 'view_user', 'change_user', 'delete_user',
                'view_passage',
                'view_vessel',
            ]
            usuario_group.permissions.clear()
            for codename in perms_usuario:
                perm = Permission.objects.get(codename=codename)
                usuario_group.permissions.add(perm)
        except ObjectDoesNotExist as e:
            self.stdout.write(self.style.WARNING(f'Permissão não encontrada: {e}'))

        try:
            perms_proprietario = [
                'view_user', 'change_user', 'delete_user',
                'add_vessel', 'view_vessel','change_vessel', 'delete_vessel',
                'add_passage', 'view_passage', 'change_passage', 'delete_passage',
            ]
            proprietario_group.permissions.clear()
            for codename in perms_proprietario:
                perm = Permission.objects.get(codename=codename)
                proprietario_group.permissions.add(perm)
        except ObjectDoesNotExist as e:
            self.stdout.write(self.style.WARNING(f'Permissão não encontrada: {e}'))

        self.stdout.write(self.style.SUCCESS('Grupos e permissões configurados.'))