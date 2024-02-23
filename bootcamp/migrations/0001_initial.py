# Generated by Django 4.2 on 2024-02-23 17:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BootCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("sub_title", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.TextField()),
                ("instructor", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="itie_img/"),
                ),
                (
                    "video",
                    models.FileField(blank=True, null=True, upload_to="itie_videos/"),
                ),
                ("price", models.FloatField(blank=True, null=True)),
                (
                    "discount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("duration_field", models.DurationField(default=datetime.timedelta)),
                ("watch_percent", models.FloatField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("inactive", "Inactive"),
                            ("draft", "Draft"),
                        ],
                        default="draft",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("carriculum_title", models.CharField(default=False, max_length=100)),
                ("carriculum_desc", models.TextField(default=False)),
                (
                    "brochure",
                    models.FileField(
                        blank=True, null=True, upload_to="bootcamp_brochure"
                    ),
                ),
                ("is_wep_main", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("mobile", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="itie_testimonials"
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                ("designation", models.CharField(max_length=100, null=True)),
                ("text", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="BootBatch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("batch_name", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bootcamp.bootcourse",
                    ),
                ),
            ],
        ),
    ]
