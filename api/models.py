from django.db import models
# import datetime
from datetime import datetime
# Create your models here.


class BasePrice(models.Model):

    base_distance = models.IntegerField(default=0)
    dbp = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    tbp = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    created = models.DateTimeField(default=datetime.now)
    dap = models.DecimalField(decimal_places=1, max_digits=3, default=0)




