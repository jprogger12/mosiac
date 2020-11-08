from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class ContactInfomation(models.Model):
    address = models.CharField(max_length=255, verbose_name='Kompaniyaning Manzili')
    phone = models.CharField(max_length=13, verbose_name='Telefon')
    email = models.EmailField(verbose_name='e-mail')
    website = models.CharField(max_length=255, verbose_name="Qo'shimcha website manzili")
    googleApi = models.CharField(max_length=500, verbose_name="Google kartadagi manzil")

    def __str__(self):
        return f'Firma manzili haqidagi malumotlar {self.id}'


class Message(models.Model):
    name = models.CharField(max_length=30, verbose_name="Xat jonatuvchining ismi")
    email = models.EmailField(verbose_name="e-mail")
    subject = models.CharField(max_length=255, verbose_name='Mavzu')
    message = models.TextField(verbose_name="Murojat Xati")

    def __str__(self):
        return f"{self.name}ning '{self.subject}' mavzudagi murojati"


class TeamPerson(models.Model):
    img = models.ImageField(verbose_name="Hodimning rasmi")
    fullName = models.CharField(max_length=100, verbose_name="Hodimning ismi va Familiyasi")
    profession = models.CharField(max_length=100, verbose_name="Hodimning vazifasi")
    about = models.TextField(verbose_name="Hodim haqida qisqacha malumot")

    def __str__(self):
        return f"{self.fullName} haqidagi malumot"


class TeamPersonContact(models.Model):
    personId = models.ForeignKey(TeamPerson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Pochta yoki ichtimoiy tarmoq nomi")
    url = models.URLField(verbose_name="Pochtaning manzili")

    def __str__(self):
        # ism = str(self.personId)[:-17]
        ism = self.personId.fullName
        return f"{ism}ning {self.name}dagi pochtasi"


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Dizayn turi")

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Dizayn turi")
    about = models.CharField(max_length=255, verbose_name="Dizayn haqidagi malumot")
    img = models.ImageField(verbose_name='Dizayn rasmi', upload_to='images')

    def __str__(self):
        return f'{self.category.name} {self.about} id = {self.id}'


class Customer(models.Model):
    img = models.ImageField(verbose_name="Klientning rasmi", upload_to='images/customer')
    text = models.TextField(verbose_name="klientning fikri")
    fullName = models.CharField(max_length=150, verbose_name='Klientning ism-sharifi')
    companyName = models.CharField(max_length=255, verbose_name="klientning firmasi")

    def __str__(self):
        return self.fullName + 'ning fikri'


class About(models.Model):
    text = models.TextField(verbose_name="About qismiga matn")
    img = models.ImageField(verbose_name='About qismiga rasm', upload_to='images/about')


class BlogLetter(models.Model):
    img = models.ImageField(verbose_name='Maqola uchun rasm', upload_to='images/blog')
    title = models.CharField(max_length=255, verbose_name='Maqolaning mavzusi')
    slug = models.SlugField(max_length=160, verbose_name="Ssilka uchun")
    letter = models.TextField(verbose_name='Maqola')
    user = models.ForeignKey(TeamPerson, on_delete=models.CASCADE, verbose_name='Maqola muallifi')
    date = models.DateField(verbose_name='Maqola yozilgan sana', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug':self.slug})

    # def get_url(self):
    #     def get_absolute_url(get):
    #         return reverse('blog-d', kwargs={'category': get.category})
    #     print("SSSSSAAAAAAAAAAAAALLLLLLLLLLLLLLLLOOOOOOOOOOOOOOOOMMMMMMMMMMMMMMMMMMMMMMMM")
    #     return get_absolute_url(self)

    def get_review(self):
        return self.comment_set.filter(parent__isnull=True)

    def __str__(self):
        return f'{self.title}, {self.date}'


class Comment(models.Model):
    blogId = models.ForeignKey(BlogLetter, on_delete=models.CASCADE, verbose_name='Maqola mavzusi')
    name = models.CharField(max_length=100, verbose_name='Izoh qoldiruvchining ismi')
    email = models.EmailField(max_length=100, verbose_name='Izoh qoldiruvchining e-maili')
    text = models.TextField(verbose_name="Izoh")
    parent = models.ForeignKey('self',verbose_name='Javob yozilgan izoh Parenti', on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(verbose_name='Izoh yozilgan sana', auto_now=True)


class OurService(models.Model):
    name = models.CharField(max_length=255, verbose_name='Xizmat nomi')
    about = models.TextField(verbose_name='Xizmat haqida')

    def __str__(self):
        return self.name
class HomeHeader(models.Model):
    title = models.CharField(max_length=255, verbose_name="Mavzu")
    sidetitle = models.CharField(max_length=255, verbose_name="Yon tomondagi Mavzu")
    text = models.TextField(verbose_name="Matn")
    img = models.ImageField(verbose_name="rasm", upload_to='images/homeheader/')

    def __str__(self):
        return self.title


class EmailSend(models.Model):
    email = models.EmailField(verbose_name="Klientning emaili")

    def __str__(self):
        return self.email