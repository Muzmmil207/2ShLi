from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.


class short_url(models.Model):
    short_url = models.CharField(max_length=200, unique=True)
    long_url = models.URLField('URL', null=True)
    qr_code = models.ImageField(upload_to='qe_code', blank=True)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    link_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.long_url)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make('http://127.0.0.1:8000/' + self.short_url)
        canvas = Image.new('RGB', (350, 350), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.user}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('LinksView')


# , args=(str(self.id))'
