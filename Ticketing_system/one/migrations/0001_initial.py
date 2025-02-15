# Generated by Django 4.2.7 on 2023-11-30 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('ManagerID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Name', models.CharField(max_length=255)),
                ('Role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('SectionID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Department', models.CharField(choices=[('CS', 'Computer Science'), ('CYS', 'Cybersecurity'), ('SE', 'Software Engineering'), ('AI', 'Artificial Intelligence')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Name', models.CharField(max_length=255)),
                ('Department', models.CharField(choices=[('CS', 'Computer Science'), ('CYS', 'Cybersecurity'), ('SE', 'Software Engineering'), ('AI', 'Artificial Intelligence')], max_length=3)),
                ('Batch', models.IntegerField()),
                ('Section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.section')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('SubjectID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('SubjectName', models.CharField(max_length=255)),
                ('Department', models.CharField(choices=[('CS', 'Computer Science'), ('CYS', 'Cybersecurity'), ('SE', 'Software Engineering'), ('AI', 'Artificial Intelligence')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAdvising',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('issues_explanation', models.TextField()),
                ('status', models.CharField(choices=[('submitted', 'Submitted'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('in_progress', 'In Progress'), ('pending', 'Pending')], default='submitted', max_length=20)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='one.manager')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.service')),
                ('student_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='one.student')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('ReportID', models.IntegerField(primary_key=True, serialize=False)),
                ('ReportContent', models.TextField()),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('NotificationID', models.IntegerField(primary_key=True, serialize=False)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('NotificationContent', models.TextField()),
                ('Status', models.CharField(max_length=10)),
                ('Manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.manager')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='services_overseen',
            field=models.ManyToManyField(to='one.service'),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('FacultyID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Name', models.CharField(max_length=255)),
                ('Department', models.CharField(choices=[('CS', 'Computer Science'), ('CYS', 'Cybersecurity'), ('SE', 'Software Engineering'), ('AI', 'Artificial Intelligence')], max_length=4)),
                ('Role', models.CharField(max_length=50)),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('AppointmentID', models.IntegerField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Status', models.CharField(max_length=20)),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.service')),
                ('Staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.manager')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.student')),
            ],
        ),
    ]
