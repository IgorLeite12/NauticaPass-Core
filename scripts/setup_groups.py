# scripts/setup_groups.py
from django.contrib.auth.models import Group, Permission

usuario_group, _ = Group.objects.get_or_create(name='Usuario')
proprietario_group, _ = Group.objects.get_or_create(name='Proprietario')
admin_group, _ = Group.objects.get_or_create(name='Administrador')

add_ticket_perm = Permission.objects.get(codename='add_ticket')
usuario_group.permissions.clear()
usuario_group.permissions.add(add_ticket_perm)

add_vessel = Permission.objects.get(codename='add_vessel')
change_vessel = Permission.objects.get(codename='change_vessel')
add_passage = Permission.objects.get(codename='add_passage')
change_passage = Permission.objects.get(codename='change_passage')
proprietario_group.permissions.clear()
proprietario_group.permissions.add(add_vessel, change_vessel, add_passage, change_passage)

print('Grupos e permissões configurados.')