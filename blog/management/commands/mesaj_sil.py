from django.core.management.base import BaseCommand
from blog.models import IletisimModel

class Command(BaseCommand):
    help = 'Verilen email adresine göre gelen mesajları sil.'

    def add_arguments(self, parser):
        parser.add_argument('--email', help='Email adresi giriniz.')

    def handle(self, **options):
        if options.get('email') is None:
            IletisimModel.objects.all().delete()
            self.stdout.write('Tüm mesajlar silindi.')
        else:
            IletisimModel.objects.filter(email=options.get('email')).delete()
            self.stdout.write('Mesajları silindi:' + options.get('email'))