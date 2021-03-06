# Generated by Django 3.1.4 on 2020-12-17 11:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='wceworkshops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('domain', models.CharField(default='CSE', max_length=30)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('place', models.CharField(default='Sangli', max_length=50)),
                ('mode', models.BooleanField()),
                ('role', models.CharField(default='Head', max_length=50)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('numberOfParticipants', models.IntegerField()),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='wcewebinars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('location', models.CharField(default='Sangli', max_length=50)),
                ('mode', models.BooleanField()),
                ('role', models.CharField(default='Head', max_length=50)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('numberOfParticipants', models.IntegerField()),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='wcesttp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('domain', models.CharField(default='CSE', max_length=30)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('place', models.CharField(default='Sangli', max_length=50)),
                ('mode', models.BooleanField()),
                ('role', models.CharField(default='Head', max_length=50)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('numberOfParticipants', models.IntegerField()),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='wceguestlectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='Cyber Security', max_length=60)),
                ('domain', models.CharField(default='CSE', max_length=50)),
                ('resourcepersonname', models.CharField(default='NA', max_length=80)),
                ('resourcepersonprofession', models.CharField(default='Industry', max_length=80)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('beneficiaries', models.CharField(default='Student', max_length=30)),
                ('numberOfParticipants', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='wcefdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('domain', models.CharField(default='CSE', max_length=40)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('place', models.CharField(default='Sangli', max_length=50)),
                ('mode', models.BooleanField()),
                ('role', models.CharField(default='Head', max_length=50)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('numberOfParticipants', models.IntegerField()),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='wceconferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confname', models.CharField(default='No Title', max_length=100)),
                ('domain', models.CharField(default='CSE', max_length=30)),
                ('mode', models.BooleanField()),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(default='Sangli', max_length=100)),
                ('place', models.CharField(default='Sangli', max_length=50)),
                ('numberOfParticipants', models.IntegerField()),
                ('level', models.BooleanField()),
                ('index', models.CharField(default='888888888', max_length=30)),
                ('publicationPorR', models.BooleanField()),
                ('publicationtype', models.CharField(default='Book Chapter', max_length=100)),
                ('publicationSupport', models.CharField(default='IEEE', max_length=28)),
                ('role', models.CharField(default='Head', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='subhighestdegreecerti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namefaculty', models.CharField(default='James Bond', max_length=50)),
                ('namedegree', models.CharField(default='Phd', max_length=50)),
                ('namecllg', models.CharField(default='Harvard Bussiness School', max_length=80)),
                ('yearpassing', models.IntegerField()),
                ('certification', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='subcoursebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Operating System', max_length=80)),
                ('coursecode', models.CharField(default='4CS203', max_length=40)),
                ('coursetype', models.CharField(default='Theory', max_length=25)),
                ('acaclass', models.IntegerField()),
                ('acayear', models.IntegerField(default=2020, validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='year')),
                ('semester', models.IntegerField()),
                ('coursebook', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ioworkshops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('domain', models.CharField(default='CSE', max_length=30)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('location', models.CharField(default='Sangli', max_length=50)),
                ('mode', models.BooleanField()),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('inorout', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='iowebinars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('location', models.CharField(default='Sangli', max_length=50)),
                ('domain', models.CharField(default='CSE', max_length=40)),
                ('mode', models.BooleanField()),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('inorout', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='iosttp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('domain', models.CharField(default='CSE', max_length=30)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('location', models.CharField(default='Sangli', max_length=50)),
                ('mode', models.BooleanField()),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('inorout', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='iopaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('papertitle', models.CharField(default='Research Paper', max_length=100)),
                ('mode', models.BooleanField()),
                ('confname', models.CharField(default='No Title', max_length=100)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(default='Sangli', max_length=100)),
                ('level', models.BooleanField()),
                ('publicationPorR', models.BooleanField()),
                ('publicationtype', models.CharField(default='Book Chapter', max_length=100)),
                ('index', models.CharField(default='8888888888', max_length=30)),
                ('volumenumber', models.IntegerField()),
                ('issuenumber', models.IntegerField()),
                ('isbnissndoi', models.CharField(default='ISBN', max_length=20)),
                ('pagefrom', models.IntegerField()),
                ('pageto', models.IntegerField()),
                ('month', models.CharField(default='September', max_length=15)),
                ('year', models.IntegerField(default=2020, validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='year')),
                ('paperurl', models.URLField(default='http://www.sciencedirect.com/science/article/pii/S0747563216304411')),
                ('inorout', models.BooleanField(default=True)),
                ('coauthor', models.CharField(default='Simon Lulla', max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='iofdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kala', max_length=30)),
                ('organizer', models.CharField(default='WCE', max_length=30)),
                ('location', models.CharField(default='Sangli', max_length=50)),
                ('mode', models.BooleanField()),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('domain', models.CharField(default='CSE', max_length=40)),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('inorout', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='iocourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='C++', max_length=30)),
                ('domain', models.CharField(default='CSE', max_length=30)),
                ('platform', models.CharField(default='Udemy', max_length=30)),
                ('durationweeks', models.IntegerField(default=4, null=True)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('certification', models.URLField()),
                ('certBool', models.BooleanField()),
                ('inorout', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='CSE', max_length=10)),
                ('degree', models.CharField(default='Bachelors', max_length=50)),
                ('desig', models.CharField(default='Professor', max_length=50)),
                ('profile', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
