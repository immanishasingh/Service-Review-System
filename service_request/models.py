from django.db import models

# Create your models here.
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    srtype = [('Technical Support', 'Technical Support'), ('Billing & Account Support', 'Billing & Account Support'), ('Product/Service Request', 'Product/Service Request'), ('General Queries', 'General Queries')]
    stype = models.CharField(max_length=100, choices=srtype)
    description = models.TextField()
    image = models.ImageField(upload_to='request/')
    st = [('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Not Resolved', 'Not Resolved')]
    status = models.CharField(max_length=100, choices=st, default='In Progress')
    comment = models.CharField(max_length=100, default='No Comments')
    
    def __str__(self):
        return self.name
