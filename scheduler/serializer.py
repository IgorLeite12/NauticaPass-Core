import passage
import ticket
import user
from scheduler.services import genera_micro_program_seaman
from scheduler.models import Schedule

# Após criar o ticket:
cronograma = genera_micro_program_seaman(passage, user)
Schedule.objects.create(ticket=ticket, content=cronograma)