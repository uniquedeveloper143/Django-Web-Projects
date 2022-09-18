from django.db import models


class Customer(models.Model):
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    password = models.CharField(max_length=256)

    def regis(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False