from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from passage.models import Passage
from ticket.models import Ticket


class Command(BaseCommand):
    help = 'Cria grupos de usuários e define suas permissões'

    def handle(self, *args, **options):
        user_group, created = Group.objects.get_or_create(name='Usuario')
        if created:
            content_type_ticket = ContentType.objects.get_for_model(Ticket)
            permission_add_ticket = Permission.objects.get(codename='add_ticket', content_type=content_type_ticket)
            permission_view_ticket = Permission.objects.get(codename='view_ticket', content_type=content_type_ticket)

            user_group.permissions.add(permission_add_ticket)
            user_group.permissions.add(permission_view_ticket)

            self.stdout.write(self.style.SUCCESS('Grupo "Usuario" criado e permissões de ticket adicionadas.'))
        else:
            self.stdout.write('Grupo "Usuario" já existe.')

        proprietary_group, created = Group.objects.get_or_create(name='Proprietario')
        if created:
            content_type_passage = ContentType.objects.get_for_model(Passage)
            permission_add_passage = Permission.objects.get(codename='add_passage', content_type=content_type_passage)
            permission_change_passage = Permission.objects.get(codename='change_passage', content_type=content_type_passage)
            permission_delete_passage = Permission.objects.get(codename='delete_passage', content_type=content_type_passage)
            permission_view_passage = Permission.objects.get(codename='view_passage', content_type=content_type_passage)

            proprietary_group.permissions.add(
                permission_add_passage,
                permission_change_passage,
                permission_delete_passage,
                permission_view_passage
            )

            self.stdout.write(self.style.SUCCESS('Grupo "Proprietario" criado e permissões de passagem adicionadas.'))
        else:
            self.stdout.write('Grupo "Proprietario" já existe.')

        admin_group, created = Group.objects.get_or_create(name='Administrador')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Administrador" criado.'))
        else:
            self.stdout.write('Grupo "Administrador" já existe.')

        all_permissions = Permission.objects.all()
        admin_group.permissions.set(all_permissions)

        self.stdout.write(self.style.SUCCESS('Todas as permissões foram concedidas ao grupo "Administrador".'))