from django.db import models

class Chapters(models.Model):
  TRILOGY = [
    ('OG','Original Trilogy'),
    ('SQ','Sequels Trilogy'),
    ('PQ','Prequels Trilogy')
  ]
  
  title = models.CharField(max_length=50)
  trilogy = models.CharField(max_length=2,choices=TRILOGY)
  translation_PTBR = models.CharField(max_length=50)


class SequelsPros(models.Model):
  IRONY_TOGGLE = [
    ('I','Ironic'),
    ('R','For real')
  ]
  
  PRO_CATEGORY = [
    ('CH','Chracters'),
    ('CA','Cast'),
    ('N','Nostalgia'),
    ('L', 'Lore'),
    ('P', 'Plot'),
    ('RD', 'Random')
  ]
  
  content = models.CharField(max_length=250)
  irony = models.CharField(max_length=1, choices=IRONY_TOGGLE)
  category = models.CharField(max_length=2, choices=PRO_CATEGORY)

class TableInfo(models.Model):
  num = models.CharField(max_length=4)
  newName = models.CharField(max_length=50)
  reason = models.CharField(max_length=250)